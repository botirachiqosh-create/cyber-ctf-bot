import socket
import sys
import threading
import os
import pty
import select
import paramiko
from pathlib import Path

BASE_DIR = Path("/app" if os.path.exists("/app") else "/home/fara/.gemini/antigravity/scratch/telegram_video_bot")
LAB_BASE = Path("/app/ctf_lab" if os.path.exists("/app") else "/home/fara/.gemini/antigravity/scratch/ctf_lab")
USERS_DIR = LAB_BASE / "users"
HOST_KEY_PATH = BASE_DIR / "ssh_host_key"

USERS_DIR.mkdir(parents=True, exist_ok=True)

if not HOST_KEY_PATH.exists():
    key = paramiko.RSAKey.generate(2048)
    key.write_private_key_file(str(HOST_KEY_PATH))
else:
    key = paramiko.RSAKey(filename=str(HOST_KEY_PATH))

def setup_user_sandbox(user_id: int):
    user_home = USERS_DIR / f"user_{user_id}"
    bin_dir = user_home / "bin"
    logs_dir = user_home / "logs"
    
    for d in [user_home, bin_dir, logs_dir]:
        d.mkdir(parents=True, exist_ok=True)
        
    # Copy ctf CLI
    ctf_src = Path("/home/fara/.gemini/antigravity/scratch/telegram_video_bot/ctf_cli.py")
    if ctf_src.exists():
        with open(ctf_src, "r") as src, open(user_home / "ctf", "w") as dst:
            dst.write(src.read())
        os.chmod(user_home / "ctf", 0o755)

    # CH03: Backup service binary (simulated SUID relative path bug)
    backup_bin_code = """#!/bin/sh
echo "=== AUTOMATED BACKUP SERVICE V2.1 ==="
echo "Executing system cataloging..."
# Bug: uses relative 'cat' instead of /bin/cat
cat /etc/hostname 2>/dev/null || cat .secret 2>/dev/null
echo "Backup catalog complete."
"""
    with open(user_home / "backup_service", "w") as f:
        f.write(backup_bin_code)
    os.chmod(user_home / "backup_service", 0o755)

    # .bashrc with Cyber Hacker interface
    bashrc = f"""
export PS1='\\[\\033[01;32m\\]operator@cyber-ctf\\[\\033[00m\\]:\\[\\033[01;34m\\]\\w\\[\\033[00m\\]\\$ '
export PATH="{user_home}:$PATH"
cd {user_home}
ctf banner
"""
    with open(user_home / ".bashrc", "w") as f:
        f.write(bashrc)
    return user_home

class CTFServerInterface(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
        self.username = None

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        self.username = username
        if username == "student" and password in ["cyber", "student"]:
            return paramiko.AUTH_SUCCESSFUL
        if username.startswith("user_"):
            try:
                tg_id = username.split("_")[1]
                expected = f"pass_{tg_id[:6]}"
                if password == expected or password == "cyber":
                    return paramiko.AUTH_SUCCESSFUL
            except:
                pass
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True

    def check_channel_exec_request(self, channel, command):
        self.event.set()
        return True

def handle_client_connection(client_sock):
    transport = paramiko.Transport(client_sock)
    transport.add_server_key(key)
    server = CTFServerInterface()
    
    try:
        transport.start_server(server=server)
    except paramiko.SSHException:
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

    user = server.username or "student"
    try:
        user_id = int(user.split("_")[1]) if "_" in user else 6895259303
    except:
        user_id = 6895259303
        
    user_home = setup_user_sandbox(user_id)
    
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
        env["HOME"] = str(user_home)
        env["USER"] = user
        env["TERM"] = "xterm-256color"
        env["PATH"] = f"{user_home}:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        
        os.chdir(str(user_home))
        os.execvpe("/bin/bash", ["/bin/bash", "--rcfile", str(user_home / ".bashrc"), "-i"], env)
        sys.exit(0)
    else:
        os.close(slave_fd)
        
        def chan_to_pty():
            try:
                while True:
                    data = chan.recv(1024)
                    if not data:
                        break
                    os.write(master_fd, data)
            except:
                pass

        def pty_to_chan():
            try:
                while True:
                    r, _, _ = select.select([master_fd], [], [], 0.1)
                    if r:
                        data = os.read(master_fd, 1024)
                        if not data:
                            break
                        chan.send(data)
                    if chan.closed:
                        break
            except:
                pass

        t1 = threading.Thread(target=chan_to_pty, daemon=True)
        t2 = threading.Thread(target=pty_to_chan, daemon=True)
        t1.start()
        t2.start()
        
        t1.join()
        try:
            os.close(master_fd)
            os.kill(pid, 9)
        except:
            pass
        chan.close()
        transport.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 2222))
    server_socket.listen(100)
    print("🚀 PTY SSH CTF Server 0.0.0.0:2222 da ishga tushdi...", flush=True)

    while True:
        try:
            client_sock, addr = server_socket.accept()
            t = threading.Thread(target=handle_client_connection, args=(client_sock,), daemon=True)
            t.start()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("Accept error:", e, flush=True)

if __name__ == "__main__":
    main()
