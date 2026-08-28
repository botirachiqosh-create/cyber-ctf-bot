---
id: 26
title: "CH26: Bidirectional Pipeline with Subshells"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 8
tags: ['redirection', 'stderr', 'stdout', 'descriptors']
flag: "HD{bidirectional_stderr_redirection_pipeline_926}"
---

# 🎯 Topshiriq #26: CH26: Bidirectional Pipeline with Subshells

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #redirection, #stderr, #stdout, #descriptors

---

## 📝 Topshiriq Senariysi (Scenario):
Dastur faqat stdin va stderr orqali interaktiv ishlaydi. Stdout ni /dev/null ga yo'naltirib, stderr dagi xatolik kodlarini filtrlash orqali flagni oling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> ./validator 2>&1 >/dev/null | grep 'FLAG_PART'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
./validator 2>&1 >/dev/null | grep 'FLAG_PART'
```

---

## 🚩 Maxfiy Flag:
`HD{bidirectional_stderr_redirection_pipeline_926}`
