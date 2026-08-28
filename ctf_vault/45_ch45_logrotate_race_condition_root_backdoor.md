---
id: 45
title: "CH45: Logrotate Race Condition Root Backdoor"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 10
tags: ['logrotate', 'race-condition', 'privesc', 'logrotten']
flag: "HD{logrotate_race_condition_root_exploit_945}"
---

# 🎯 Topshiriq #45: CH45: Logrotate Race Condition Root Backdoor

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 10 ball`
* **Teglar:** #logrotate, #race-condition, #privesc, #logrotten

---

## 📝 Topshiriq Senariysi (Scenario):
/etc/logrotate.d/nginx konfiguratsiyasi 'create 0644 root root' qoidasiga ega va 'prerotate' da foydalanuvchi papkasidagi faylni ko'chiradi. Logrotate race condition orqali root bo'ling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> logrotten poygasi orqali /etc/passwd ni almashtiring.

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
logrotten poygasi orqali /etc/passwd ni almashtiring.
```

---

## 🚩 Maxfiy Flag:
`HD{logrotate_race_condition_root_exploit_945}`
