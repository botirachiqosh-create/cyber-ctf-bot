---
id: 2
title: "CH02: Null-Byte Process Environ Injection"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 7
tags: ['environ', 'proc', 'null-bytes', 'reverse']
flag: "HD{environ_null_byte_process_inspection_902}"
---

# 🎯 Topshiriq #2: CH02: Null-Byte Process Environ Injection

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 7 ball`
* **Teglar:** #environ, #proc, #null-bytes, #reverse

---

## 📝 Topshiriq Senariysi (Scenario):
Yashirin ishlayotgan 'vault_watcher' jarayonining muhit o'zgaruvchilari (environ) ichida maxfiy parol va flag qoldirilgan. Process xotirasidagi null-bayt bilan ajratilgan o'zgaruvchilarni filtrlash orqali flagni oling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> cat /proc/<PID>/environ | tr '\0' '\n' | grep 'SECRET_FLAG'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
cat /proc/<PID>/environ | tr '\0' '\n' | grep 'SECRET_FLAG'
```

---

## 🚩 Maxfiy Flag:
`HD{environ_null_byte_process_inspection_902}`
