---
id: 50
title: "CH50: FINAL BOSS: Multi-Stage Chain CTF"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 15
tags: ['final-boss', 'chained-exploit', 'full-compromise', 'master']
flag: "HD{cyber_ultimate_grandmaster_chained_exploit_950}"
---

# 🎯 Topshiriq #50: CH50: FINAL BOSS: Multi-Stage Chain CTF

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 15 ball`
* **Teglar:** #final-boss, #chained-exploit, #full-compromise, #master

---

## 📝 Topshiriq Senariysi (Scenario):
Oxirgi Katta Topshiriq: 1-bosqichda tarmoq portidan XOR kalitni oling ➡️ 2-bosqichda `/proc` xotirasidan o'chirilgan faylni tiklang ➡️ 3-bosqichda SUID Path Hijacking orqali root bo'lib yakuniy flagni oling!

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> 1. nc 127.0.0.1 9999 -> 2. cat /proc/<PID>/fd/X -> 3. SUID ./backup_service

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
1. nc 127.0.0.1 9999 -> 2. cat /proc/<PID>/fd/X -> 3. SUID ./backup_service
```

---

## 🚩 Maxfiy Flag:
`HD{cyber_ultimate_grandmaster_chained_exploit_950}`
