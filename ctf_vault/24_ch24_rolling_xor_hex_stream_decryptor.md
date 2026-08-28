---
id: 24
title: "CH24: Rolling XOR Hex Stream Decryptor"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 9
tags: ['xor', 'sockets', 'hex', 'crypto']
flag: "HD{rolling_xor_hex_socket_stream_decryptor_924}"
---

# 🎯 Topshiriq #24: CH24: Rolling XOR Hex Stream Decryptor

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #xor, #sockets, #hex, #crypto

---

## 📝 Topshiriq Senariysi (Scenario):
127.0.0.1:9001 portida har soniyada aylanma (rolling) XOR kaliti bilan shifrlangan hex oqimi uzatilmoqda. Konveyer orqali har bir baytni 0x5A bilan XOR qilib flagni o'qing.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> nc 127.0.0.1 9001 | xxd -r -p | python3 -c 'import sys; [sys.stdout.write(chr(b ^ 0x5A)) for b in sys.stdin.buffer.read()]'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
nc 127.0.0.1 9001 | xxd -r -p | python3 -c 'import sys; [sys.stdout.write(chr(b ^ 0x5A)) for b in sys.stdin.buffer.read()]'
```

---

## 🚩 Maxfiy Flag:
`HD{rolling_xor_hex_socket_stream_decryptor_924}`
