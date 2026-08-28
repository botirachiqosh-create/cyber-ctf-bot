---
id: 35
title: "CH35: SSH auth.log Brute-Force Password Anomaly"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 8
tags: ['auth-log', 'ssh', 'bruteforce', 'triage']
flag: "HD{ssh_auth_log_compromised_session_hunter_935}"
---

# 🎯 Topshiriq #35: CH35: SSH auth.log Brute-Force Password Anomaly

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #auth-log, #ssh, #bruteforce, #triage

---

## 📝 Topshiriq Senariysi (Scenario):
SSH audit logida (/var/log/auth.log) 100,000 ta kirish urinishlari orasidan yagona 'Accepted password' ga erishgan muvaffaqiyatli sessiyani toping.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> grep 'Accepted password' /var/log/auth.log

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
grep 'Accepted password' /var/log/auth.log
```

---

## 🚩 Maxfiy Flag:
`HD{ssh_auth_log_compromised_session_hunter_935}`
