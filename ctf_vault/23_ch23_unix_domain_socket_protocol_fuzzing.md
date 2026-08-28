---
id: 23
title: "CH23: Unix Domain Socket Protocol Fuzzing"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 8
tags: ['unix-sockets', 'socat', 'ipc', 'reverse']
flag: "HD{unix_domain_socket_binary_fuzzer_923}"
---

# 🎯 Topshiriq #23: CH23: Unix Domain Socket Protocol Fuzzing

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #unix-sockets, #socat, #ipc, #reverse

---

## 📝 Topshiriq Senariysi (Scenario):
/run/auth_vault.sock Unix Domain Socketi orqali binar protokol o'tmoqda. `socat` yoki `nc -U` yordamida 'GET_TOKEN_V2' binar paketini jo'natib flagni oling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> echo -e '\x01\x00\x08GET_TOKEN_V2' | nc -U /run/auth_vault.sock

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
echo -e '\x01\x00\x08GET_TOKEN_V2' | nc -U /run/auth_vault.sock
```

---

## 🚩 Maxfiy Flag:
`HD{unix_domain_socket_binary_fuzzer_923}`
