---
id: 1
title: "CH01: Unlinked Secret in /proc/fd"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 8
tags: ['proc', 'file-descriptors', 'memory-forensics', 'unlinked']
flag: "HD{proc_fd_unlinked_memory_recovery_901}"
---

# 🎯 Topshiriq #1: CH01: Unlinked Secret in /proc/fd

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #proc, #file-descriptors, #memory-forensics, #unlinked

---

## 📝 Topshiriq Senariysi (Scenario):
Tizimda fonda ishlayotgan 'audit_daemon' maxfiy 'audit_key.token' faylini xotiraga yuklab, darhol diskdan o'chirib yuborgan (unlink). /proc fayl deskriptorlari orqali o'chirilgan faylni RAM dan tiklang.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> ps aux | grep audit_daemon orqali PID ni toping, so'ng /proc/<PID>/fd/ katalogidagi (deleted) yozuvli deskriptorni o'qing: cat /proc/<PID>/fd/<NUM>

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
ps aux | grep audit_daemon orqali PID ni toping, so'ng /proc/<PID>/fd/ katalogidagi (deleted) yozuvli deskriptorni o'qing: cat /proc/<PID>/fd/<NUM>
```

---

## 🚩 Maxfiy Flag:
`HD{proc_fd_unlinked_memory_recovery_901}`
