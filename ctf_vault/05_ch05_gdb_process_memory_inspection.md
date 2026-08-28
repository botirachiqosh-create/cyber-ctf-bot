---
id: 5
title: "CH05: GDB Process Memory Inspection"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 9
tags: ['gdb', 'heap', 'reverse', 'debugging']
flag: "HD{gdb_process_heap_inspection_master_905}"
---

# 🎯 Topshiriq #5: CH05: GDB Process Memory Inspection

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #gdb, #heap, #reverse, #debugging

---

## 📝 Topshiriq Senariysi (Scenario):
Fonda pauza qilingan (stopped state 'T') jarayon /tmp/crypto_agent xotirasida AES kalitini saqlab turibdi. GDB yordamida jarayonga ulanib (attach), heap xotirasidan flagni o'qing.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> gdb -p <PID> -batch -ex 'x/s 0x555555558000' yoki 'dump memory /tmp/mem.dump 0x555555558000 0x555555559000'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
gdb -p <PID> -batch -ex 'x/s 0x555555558000' yoki 'dump memory /tmp/mem.dump 0x555555558000 0x555555559000'
```

---

## 🚩 Maxfiy Flag:
`HD{gdb_process_heap_inspection_master_905}`
