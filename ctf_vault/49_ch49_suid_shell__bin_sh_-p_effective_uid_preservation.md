---
id: 49
title: "CH49: SUID Shell /bin/sh -p Effective UID Preservation"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 8
tags: ['suid', 'bash-p', 'euid', 'privesc']
flag: "HD{suid_bin_sh_privileged_mode_euid_949}"
---

# 🎯 Topshiriq #49: CH49: SUID Shell /bin/sh -p Effective UID Preservation

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #suid, #bash-p, #euid, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
Dastur `/bin/sh` ni chaqiradi, lekin bash real UID va effective UID teng bo'lmaganda imtiyozni tashlab yuboradi. `-p` (privileged mode) parametrini kiritib haqiqiy root bo'ling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> /opt/tools/launcher -p

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
/opt/tools/launcher -p
```

---

## 🚩 Maxfiy Flag:
`HD{suid_bin_sh_privileged_mode_euid_949}`
