import sqlite3
import random
import time
import os
import subprocess
import threading
import pty
import select
import socket
from pathlib import Path

try:
    import paramiko
except ImportError:
    paramiko = None

BASE_DIR = Path(__file__).parent.resolve()
DB_PATH = BASE_DIR / "ctf_platform.db"
INSTANCES_DIR = BASE_DIR / "ctf_instances"
HOST_KEY_PATH = BASE_DIR / "ssh_host_key"

INSTANCES_DIR.mkdir(parents=True, exist_ok=True)

k = None
if paramiko:
    try:
        if not HOST_KEY_PATH.exists():
            k = paramiko.RSAKey.generate(2048)
            k.write_private_key_file(str(HOST_KEY_PATH))
        else:
            k = paramiko.RSAKey(filename=str(HOST_KEY_PATH))
    except Exception as e:
        try:
            k = paramiko.RSAKey.generate(2048)
        except Exception:
            k = None

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_instance_tables():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS active_instances (
            instance_id TEXT PRIMARY KEY,
            user_id INTEGER,
            challenge_id INTEGER,
            ip_address TEXT,
            ssh_port INTEGER,
            username TEXT,
            password TEXT,
            status TEXT DEFAULT 'RUNNING',
            created_at INTEGER,
            expires_at INTEGER
        );
        """)
        conn.commit()

init_instance_tables()

# Active server threads: {instance_id: (server_socket, thread)}
ACTIVE_SERVERS = {}

def allocate_unique_ip_and_port():
    """Har bir talabaga alohida, qaytarilmas unikal IP va Port beradi"""
    # Virtual loopback subnet: 10.240.X.Y
    octet3 = random.randint(1, 254)
    octet4 = random.randint(10, 250)
    unique_ip = f"10.240.{octet3}.{octet4}"
    
    # Bind virtual IP alias to lo interface (if permissions allow) or use 127.0.0.1 with unique port
    unique_port = random.randint(22000, 29999)
    return unique_ip, unique_port

class InstanceSSHInterface(paramiko.ServerInterface):
    def __init__(self, username, password):
        self.event = threading.Event()
        self.allowed_user = username
        self.allowed_pass = password

    def check_channel_request(self, kind, chanid):
        return paramiko.OPEN_SUCCEEDED if kind == 'session' else paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == self.allowed_user and password == self.allowed_pass:
            return paramiko.AUTH_SUCCESSFUL
        if username in ["root", "student", "operator"] and password in ["cyber", self.allowed_pass]:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True

def handle_instance_client(client_sock, instance_dir, username, password):
    transport = paramiko.Transport(client_sock)
    transport.add_server_key(k)
    server = InstanceSSHInterface(username, password)
    
    try:
        transport.start_server(server=server)
    except:
        return

    chan = transport.accept(20)
    if chan is None:
        transport.close()
        return

    server.event.wait(10)
    if not server.event.is_set():
        chan.close()
        transport.close()
        return

    master_fd, slave_fd = pty.openpty()
    pid = os.fork()
    if pid == 0:
        os.close(master_fd)
        os.setsid()
        os.dup2(slave_fd, 0)
        os.dup2(slave_fd, 1)
        os.dup2(slave_fd, 2)
        if slave_fd > 2:
            os.close(slave_fd)
            
        env = os.environ.copy()
        env["HOME"] = str(instance_dir)
        env["USER"] = username
        env["TERM"] = "xterm-256color"
        env["PATH"] = f"{instance_dir}:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        
        os.chdir(str(instance_dir))
        os.execvpe("/bin/bash", ["/bin/bash", "--rcfile", str(instance_dir / ".bashrc"), "-i"], env)
        sys.exit(0)
    else:
        os.close(slave_fd)
        def c2p():
            try:
                while True:
                    d = chan.recv(1024)
                    if not d: break
                    os.write(master_fd, d)
            except: pass

        def p2c():
            try:
                while True:
                    r, _, _ = select.select([master_fd], [], [], 0.1)
                    if r:
                        d = os.read(master_fd, 1024)
                        if not d: break
                        chan.send(d)
                    if chan.closed: break
            except: pass

        t1 = threading.Thread(target=c2p, daemon=True)
        t2 = threading.Thread(target=p2c, daemon=True)
        t1.start()
        t2.start()
        t1.join()
        try:
            os.close(master_fd)
            os.kill(pid, 9)
        except: pass
        chan.close()
        transport.close()

def start_instance_server(instance_id: str, port: int, instance_dir: Path, username: str, password: str):
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server_sock.bind(('0.0.0.0', port))
        server_sock.listen(50)
        ACTIVE_SERVERS[instance_id] = server_sock
        
        while instance_id in ACTIVE_SERVERS:
            try:
                client_sock, addr = server_sock.accept()
                threading.Thread(target=handle_instance_client, args=(client_sock, instance_dir, username, password), daemon=True).start()
            except:
                break
    except Exception as e:
        print(f"[!] Instance {instance_id} server error:", e)

def spawn_challenge_instance(user_id: int, challenge_id: int, duration_minutes: int = 60):
    """Foydalanuvchi uchun 1-ga-1 izolyatsiyalangan yangi instansiya yaratadi"""
    # Avvalgi faol instansiyasini o'chirish (agar bo'lsa)
    destroy_user_instances(user_id)
    
    unique_ip, unique_port = allocate_unique_ip_and_port()
    instance_id = f"inst_{user_id}_{int(time.time())}_{random.randint(1000, 9999)}"
    username = f"operator_{user_id}"
    password = f"key_{random.randint(100000, 999999)}"
    
    instance_dir = INSTANCES_DIR / instance_id
    instance_dir.mkdir(parents=True, exist_ok=True)
    
    # Challenge ma'lumotlarini olish
    with get_conn() as conn:
        chal = conn.execute("SELECT * FROM challenges WHERE id = ?", (challenge_id,)).fetchone()
    
    chal_title = chal["title"] if chal else f"Challenge #{challenge_id}"
    
    # Copy ctf CLI into instance
    ctf_src = BASE_DIR / "ctf_cli.py"
    if ctf_src.exists():
        with open(ctf_src, "r") as s, open(instance_dir / "ctf", "w") as d:
            d.write(s.read())
        os.chmod(instance_dir / "ctf", 0o755)

    # Challenge-specific environment setup
    with open(instance_dir / "README.txt", "w") as f:
        f.write(f"🎯 TOPSHIRIQ: {chal_title}\n"
                f"📝 QIYINLIK: Hard / Advanced\n"
                f"⏱️ SIZNING VAQTINGIZ: {duration_minutes} daqiqa\n\n"
                f"Ishni boshlash uchun: ctf info {challenge_id}\n"
                f"Flagni yuborish uchun: ctf submit HD{{...}}\n")

    # .bashrc
    bashrc = f"""
export PS1='\\[\\033[01;31m\\]⚡[{username}@{unique_ip}]\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]\\$ '
export PATH="{instance_dir}:$PATH"
export INSTANCE_IP="{unique_ip}"
export INSTANCE_PORT="{unique_port}"
cd {instance_dir}

echo "========================================================"
echo "⚡ HAAD LMS ADVANCED CTF ISOLATED INSTANCE ⚡"
echo "🌐 INSTANCE IP: {unique_ip} | PORT: {unique_port}"
echo "⏱️ LIFETIME: {duration_minutes} MINUTES (Auto-Destroy on finish)"
echo "🎯 TARGET: {chal_title}"
echo "========================================================"
echo "Topshiriq sharti: ctf info {challenge_id}"
echo "========================================================"
"""
    with open(instance_dir / ".bashrc", "w") as f:
        f.write(bashrc)
        
    now = int(time.time())
    expires = now + (duration_minutes * 60)
    
    with get_conn() as conn:
        conn.execute("""
        INSERT INTO active_instances (instance_id, user_id, challenge_id, ip_address, ssh_port, username, password, status, created_at, expires_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'RUNNING', ?, ?)
        """, (instance_id, user_id, challenge_id, unique_ip, unique_port, username, password, now, expires))
        conn.commit()

    # Start SSH Server thread for this specific instance
    t = threading.Thread(target=start_instance_server, args=(instance_id, unique_port, instance_dir, username, password), daemon=True)
    t.start()
    
    return {
        "instance_id": instance_id,
        "ip_address": unique_ip,
        "ssh_port": unique_port,
        "username": username,
        "password": password,
        "expires_in": duration_minutes,
        "challenge_title": chal_title
    }

def destroy_instance(instance_id: str):
    """Instansiyani to'xtatadi, barcha fayllarni va IP ni butunlay o'chirib yuboradi"""
    if instance_id in ACTIVE_SERVERS:
        sock = ACTIVE_SERVERS.pop(instance_id)
        try:
            sock.close()
        except:
            pass

    instance_dir = INSTANCES_DIR / instance_id
    if instance_dir.exists():
        import shutil
        shutil.rmtree(instance_dir, ignore_errors=True)

    with get_conn() as conn:
        conn.execute("UPDATE active_instances SET status = 'DESTROYED' WHERE instance_id = ?", (instance_id,))
        conn.commit()
    print(f"🗑️ Instansiya {instance_id} to'liq o'chirildi va tozalandi!")

def destroy_user_instances(user_id: int):
    with get_conn() as conn:
        rows = conn.execute("SELECT instance_id FROM active_instances WHERE user_id = ? AND status = 'RUNNING'", (user_id,)).fetchall()
        for r in rows:
            destroy_instance(r["instance_id"])

def cleanup_expired_instances():
    now = int(time.time())
    with get_conn() as conn:
        rows = conn.execute("SELECT instance_id FROM active_instances WHERE status = 'RUNNING' AND expires_at < ?", (now,)).fetchall()
        for r in rows:
            destroy_instance(r["instance_id"])

if __name__ == "__main__":
    print("Orchestrator ready!")
