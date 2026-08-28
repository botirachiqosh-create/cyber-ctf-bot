---
id: 7
title: "CH07: LD_PRELOAD Stealth Hook Detection"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 9
tags: ['ld_preload', 'rootkit', 'evasion', 'hooks']
flag: "HD{ld_preload_stealth_rootkit_bypass_907}"
---

# 🎯 Topshiriq #7: CH07: LD_PRELOAD Stealth Hook Detection

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #ld_preload, #rootkit, #evasion, #hooks

---

## 📝 Topshiriq Senariysi (Scenario):
Tizimda '/etc/ld.so.preload' orqali yashirin rootkit o'rnatilgan bo'lib, u 'ls' va 'ps' buyruqlaridan maxfiy fayllarni yashirmoqda. Boshqa tizim chaqiruvlari (syscalls) orqali yashirilgan faylni toping.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> LD_PRELOAD='' /bin/ls -la yoki strace /bin/ls /tmp orqali preload hookni chetlab o'ting.

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
LD_PRELOAD='' /bin/ls -la yoki strace /bin/ls /tmp orqali preload hookni chetlab o'ting.
```

---

## 🚩 Maxfiy Flag:
`HD{ld_preload_stealth_rootkit_bypass_907}`
