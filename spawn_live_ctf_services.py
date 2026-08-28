import asyncio
import socket
import threading
import time
import os
import sys
from pathlib import Path

# 1. Background daemon with unlinked open file in /proc/fd
def run_unlinked_file_daemon():
    file_path = "/tmp/audit_key.token"
    with open(file_path, "w") as f:
        f.write("CONFIDENTIAL_SYSTEM_TOKEN\nFLAG: HD{proc_fd_memory_recovery_unlinked_991}\n")
    
    # Open file descriptor
    fd = os.open(file_path, os.O_RDONLY)
    # Unlink (delete from disk) while keeping FD open
    os.unlink(file_path)
    print(f"[*] Unlinked daemon running with FD {fd} (PID: {os.getpid()})")
    while True:
        time.sleep(3600)

# 2. Local Socket streaming Base64 & Hex on 127.0.0.1:9999
def run_hex_stream_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind(('127.0.0.1', 9999))
        server.listen(10)
        print("[*] Hex Stream Server running on 127.0.0.1:9999")
        while True:
            client, addr = server.accept()
            def stream_data(c):
                try:
                    import base64
                    flag = "HD{socket_stream_hex_base64_pipeline_440}"
                    b64 = base64.b64encode(flag.encode()).decode()
                    hex_payload = b64.encode().hex()
                    
                    for _ in range(5):
                        c.sendall(f"BEACON_PACKET:{hex_payload}\n".encode())
                        time.sleep(0.5)
                except:
                    pass
                finally:
                    c.close()
            threading.Thread(target=stream_data, args=(client,), daemon=True).start()
    except Exception as e:
        print("[!] Socket server error:", e)

# 3. Named Pipe (FIFO) 2-way daemon
def run_fifo_daemon():
    pipe_in = "/tmp/auth_in"
    pipe_out = "/tmp/auth_out"
    for p in [pipe_in, pipe_out]:
        if os.path.exists(p):
            os.unlink(p)
        os.mkfifo(p, 0o666)
    print("[*] Named Pipes /tmp/auth_in and /tmp/auth_out initialized")

def main():
    threading.Thread(target=run_hex_stream_server, daemon=True).start()
    run_fifo_daemon()
    run_unlinked_file_daemon()

if __name__ == "__main__":
    main()
