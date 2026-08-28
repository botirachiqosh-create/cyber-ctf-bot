---
id: 4
title: "CH04: Intercepting SIGUSR1 Signals"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 8
tags: ['signals', 'sigusr1', 'trap', 'processes']
flag: "HD{linux_signal_trap_interceptor_904}"
---

# 🎯 Topshiriq #4: CH04: Intercepting SIGUSR1 Signals

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #signals, #sigusr1, #trap, #processes

---

## 📝 Topshiriq Senariysi (Scenario):
/tmp/signal_emitter demoni har 2 soniyada o'ziga SIGUSR1 signali yuborilganda navbatdagi flag baytini stdout ga uzatadi. Bash trap yoki signal ushlagich orqali 5 ta signal yuborib to'liq flagni yig'ing.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> for i in {1..5}; do kill -USR1 <PID>; sleep 0.2; done

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
for i in {1..5}; do kill -USR1 <PID>; sleep 0.2; done
```

---

## 🚩 Maxfiy Flag:
`HD{linux_signal_trap_interceptor_904}`
