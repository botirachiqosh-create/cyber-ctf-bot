---
id: 34
title: "CH34: Auditd Linux Kernel Event Forensics"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 8
tags: ['auditd', 'kernel-events', 'execve', 'syscalls']
flag: "HD{auditd_kernel_event_execve_forensics_934}"
---

# 🎯 Topshiriq #34: CH34: Auditd Linux Kernel Event Forensics

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #auditd, #kernel-events, #execve, #syscalls

---

## 📝 Topshiriq Senariysi (Scenario):
/var/log/audit/audit.log ichida root huquqida bajarilgan va syscall=59 (execve) chaqirgan barcha binar fayllarni ajratib, o'chirilgan binar nomini toping.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> ausearch -sc execve -i | grep 'comm=' | sort | uniq

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
ausearch -sc execve -i | grep 'comm=' | sort | uniq
```

---

## 🚩 Maxfiy Flag:
`HD{auditd_kernel_event_execve_forensics_934}`
