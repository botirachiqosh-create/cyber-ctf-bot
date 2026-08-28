---
id: 21
title: "CH21: Multi-stage Named Pipe (FIFO) Handshake"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 8
tags: ['fifo', 'named-pipes', 'file-descriptors', 'ipc']
flag: "HD{named_pipe_fifo_multistage_handshake_921}"
---

# 🎯 Topshiriq #21: CH21: Multi-stage Named Pipe (FIFO) Handshake

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #fifo, #named-pipes, #file-descriptors, #ipc

---

## 📝 Topshiriq Senariysi (Scenario):
/tmp/req_pipe va /tmp/res_pipe kanallarida autentifikatsiya protokoli ishlamoqda. 3 bosqichli SHA256 challenge-response so'roviga to'g'ri javob qaytaring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> exec 3<>/tmp/req_pipe; exec 4<>/tmp/res_pipe; read -u 3 token; echo -n $token | sha256sum >&4

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
exec 3<>/tmp/req_pipe; exec 4<>/tmp/res_pipe; read -u 3 token; echo -n $token | sha256sum >&4
```

---

## 🚩 Maxfiy Flag:
`HD{named_pipe_fifo_multistage_handshake_921}`
