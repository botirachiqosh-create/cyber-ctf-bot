---
id: 6
title: "CH06: Shared Memory IPC Carving (ipcs -m)"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 8
tags: ['shm', 'ipcs', 'ipc', 'memory']
flag: "HD{sysv_shared_memory_segment_carver_906}"
---

# 🎯 Topshiriq #6: CH06: Shared Memory IPC Carving (ipcs -m)

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #shm, #ipcs, #ipc, #memory

---

## 📝 Topshiriq Senariysi (Scenario):
Tizimda `shmget` orqali yaratilgan maxfiy Shared Memory segmenti (Key: 0x1337) mavjud. `ipcs` va C/Python yordamida ushbu xotira blokiga ulanib, flagni o'qing.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> ipcs -m orqali shmid ni toping, so'ng python sysv_ipc yoki C shmat() orqali segmentdan o'qing.

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
ipcs -m orqali shmid ni toping, so'ng python sysv_ipc yoki C shmat() orqali segmentdan o'qing.
```

---

## 🚩 Maxfiy Flag:
`HD{sysv_shared_memory_segment_carver_906}`
