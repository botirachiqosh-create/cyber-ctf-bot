---
id: 22
title: "CH22: Pure Bash Raw /dev/tcp Packet Crafting"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 7
tags: ['dev-tcp', 'bash-sockets', 'http', 'networking']
flag: "HD{pure_bash_dev_tcp_packet_crafting_922}"
---

# 🎯 Topshiriq #22: CH22: Pure Bash Raw /dev/tcp Packet Crafting

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 7 ball`
* **Teglar:** #dev-tcp, #bash-sockets, #http, #networking

---

## 📝 Topshiriq Senariysi (Scenario):
Tizimda curl, wget va netcat mavjud emas. Faqat bash ichki /dev/tcp/127.0.0.1/8080 orqali HTTP POST so'rovini yasab, 'Auth: CyberRelay' headeri bilan yuboring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> exec 3<>/dev/tcp/127.0.0.1/8080; echo -e 'GET /flag HTTP/1.1\r\nHost: 127.0.0.1\r\nAuth: CyberRelay\r\n\r\n' >&3; cat <&3

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
exec 3<>/dev/tcp/127.0.0.1/8080; echo -e 'GET /flag HTTP/1.1\r\nHost: 127.0.0.1\r\nAuth: CyberRelay\r\n\r\n' >&3; cat <&3
```

---

## 🚩 Maxfiy Flag:
`HD{pure_bash_dev_tcp_packet_crafting_922}`
