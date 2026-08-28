import sqlite3
from pathlib import Path

DB_PATH = Path("/home/fara/.gemini/antigravity/scratch/telegram_video_bot/ctf_platform.db")

HARD_MEDIUM_CHALLENGES = [
    # --- MODUL 1: LINUX INTERNALS, PROC & FORENSICS ---
    (
        "Modul 1: Linux Internals & /proc",
        "CH01: Deleted File in Memory (/proc/fd)",
        "Hard",
        6,
        "Tizimda bir jarayon (process) maxfiy 'audit_key.token' faylini ochgan va darhol diskdan o'chirib yuborgan (unlink). Lekin jarayon fonda hali ham ishlamoqda. Diskda yo'q, lekin RAM va /proc fayl deskriptorlarida saqlanib qolgan flagni tiklang.",
        "💡 Hint: 'ps aux | grep daemon' orqali jarayon PID sini toping, so'ng '/proc/<PID>/fd/' katalogini tekshirib, o'chirilgan fayl deskriptorini (fd) o'qing: cat /proc/<PID>/fd/<FD_NUM>",
        "HD{proc_fd_memory_recovery_unlinked_991}"
    ),
    (
        "Modul 1: Linux Internals & /proc",
        "CH02: Environment Injection & Process Args",
        "Medium",
        4,
        "Tizimda yashirin ishlayotgan 'vault_watcher' jarayonining muhit o'zgaruvchilari (environ) ichida maxfiy parol qoldirilgan. Process xotirasidan null-bayt bilan ajratilgan o'zgaruvchilarni ajratib oling.",
        "💡 Hint: '/proc/<PID>/environ' faylini 'strings' yoki 'tr \"\\0\" \"\\n\"' buyrug'i bilan o'qing.",
        "HD{process_environ_nullbyte_inspector_882}"
    ),

    # --- MODUL 2: PRIVILEGE ESCALATION & SUID / CAPABILITIES ---
    (
        "Modul 2: PrivEsc & Permissions",
        "CH03: SUID Path Hijacking (Relative Path Bug)",
        "Hard",
        7,
        "/usr/local/bin/backup_service dasturi root ruxsati bilan (SUID) ishlaydi va ichida 'cat' buyrug'ini to'liq yo'lsiz (masalan: '/bin/cat' o'rniga shunchaki 'cat') chaqiradi. PATH o'zgaruvchisini manipulyatsiya qilib (PATH Hijacking), root imtiyozidagi flagni qo'lga kiriting.",
        "💡 Hint: O'zingizning papkangizda 'cat' nomli qobiq skripti yarating (ichiga flagni o'qish buyrug'ini yozing), 'chmod +x cat' qiling va 'export PATH=.:$PATH' qilib backup_service ni ishga tushiring.",
        "HD{suid_path_hijacking_escalation_773}"
    ),
    (
        "Modul 2: PrivEsc & Permissions",
        "CH04: Linux Capabilities (cap_setuid)",
        "Hard",
        7,
        "Tizim administrator xavfsizlik tekshiruvida /opt/tools/custom_reader binar fayliga 'cap_setuid+ep' ruxsatini berib qo'ygan. Ushbu qobiliyatdan (Capability) foydalanib, /root/confidential.flag faylini o'qing.",
        "💡 Hint: 'getcap -r / 2>/dev/null' orqali capabilities ni tekshiring va binary orqali UID 0 ga o'tib faylni o'qing.",
        "HD{linux_capabilities_cap_setuid_664}"
    ),

    # --- MODUL 3: ADVANCED STREAMS, FIFO & SOCKETS ---
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH05: Named Pipe (FIFO) Intercept & Response",
        "Hard",
        6,
        "/tmp/auth_in va /tmp/auth_out nomli kanallar (Named Pipes) orqali fonda ishlayotgan demon bilan ikki tomonlama aloqa o'rnating. U bergan 3 ta matematik savolga 1 soniya ichida to'g'ri javob qaytaring.",
        "💡 Hint: 'mkfifo' yoki 'cat /tmp/auth_out & echo 'javob' > /tmp/auth_in' orqali zanjir quring yoki bash file descriptor (exec 3<>/tmp/auth_in) dan foydalaning.",
        "HD{named_pipe_fifo_twoway_stream_551}"
    ),
    (
        "Modul 3: Streams, FIFO & Sockets",
        "CH06: Local Socket Hex Stream Decoder",
        "Medium",
        5,
        "Lokal 127.0.0.1:9999 portida doimiy ravishda Base64 va Hex aralash kiber-signal oqimi o'tmoqda. Netcat va konveyer (pipeline) yordamida ushbu oqimni ushlab, filtrlash va dekodlash orqali flagni oling.",
        "💡 Hint: 'nc 127.0.0.1 9999 | cut -d: -f2 | xxd -r -p | base64 -d' zanjirini sinab ko'ring.",
        "HD{socket_stream_hex_base64_pipeline_440}"
    ),

    # --- MODUL 4: LOG FORENSICS, AWK & REGEX ---
    (
        "Modul 4: Log Forensics & Filters",
        "CH07: Multi-tier Log Anomaly Detection (AWK)",
        "Hard",
        6,
        "/var/log/traffic/ katalogida 500,000 ta HTTP so'rovlar logi saqlangan. Ular ichidan faqat HTTP 403 status qaytargan, POST so'rov yuborgan va uzatilgan bayt hajmi 1337 dan katta bo'lgan IP manzillar sonini aniqlab, ./verify_threat <IP> ga yuboring.",
        "💡 Hint: 'awk '$6==\"POST\" && $9==\"403\" && $10>1337 {print $1}' /var/log/traffic/*.log | sort | uniq -c | sort -nr' filtridan foydalaning.",
        "HD{awk_multitier_forensics_anomaly_339}"
    ),

    # --- MODUL 5: CRON, WILDCARDS & AUTOMATION ---
    (
        "Modul 5: Cron & Automation",
        "CH08: Tar Wildcard Injection in Root Cronjob",
        "Hard",
        8,
        "/etc/cron.d/backup_job har daqiqada 'tar -czf /backup/data.tar.gz *' buyrug'ini root nomidan ishga tushiradi. Tar dasturining '--checkpoint-action' buyruq parametrlaridan foydalangan holda Wildcard Injection orqali root flagini oling.",
        "💡 Hint: Papkada '--checkpoint=1' va '--checkpoint-action=exec=sh run.sh' nomli maxsus fayllar yarating. Tar ularni parametr deb o'ylab, run.sh skriptingizni root nomidan bajaradi!",
        "HD{tar_wildcard_injection_cron_root_228}"
    )
]

def update_challenges():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM challenges;")
    for chal in HARD_MEDIUM_CHALLENGES:
        cursor.execute("""
        INSERT INTO challenges (module, title, difficulty, points, description, hint, flag)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, chal)
    conn.commit()
    conn.close()
    print(f"✅ {len(HARD_MEDIUM_CHALLENGES)} ta haqiqiy HARD/MEDIUM CTF topshiriqlari bazaga yuklandi!")

if __name__ == "__main__":
    update_challenges()
