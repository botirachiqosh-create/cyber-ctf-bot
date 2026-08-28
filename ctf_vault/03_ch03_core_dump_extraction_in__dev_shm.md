---
id: 3
title: "CH03: Core Dump Extraction in /dev/shm"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 8
tags: ['coredump', 'shm', 'strings', 'forensics']
flag: "HD{core_dump_memory_shm_carver_903}"
---

# 🎯 Topshiriq #3: CH03: Core Dump Extraction in /dev/shm

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #coredump, #shm, #strings, #forensics

---

## 📝 Topshiriq Senariysi (Scenario):
/dev/shm xotira katalogida to'satdan qulagan (crashed) server jarayonining core dump fayli ('core.dump.bin') qolgan. Undan xotira torlari va Base64 qatlamlarini ajratib, maxfiy kalitni tiklang.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> strings /dev/shm/core.dump.bin | grep -E '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$' | base64 -d

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
strings /dev/shm/core.dump.bin | grep -E '^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$' | base64 -d
```

---

## 🚩 Maxfiy Flag:
`HD{core_dump_memory_shm_carver_903}`
