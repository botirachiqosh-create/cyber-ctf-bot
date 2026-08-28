---
id: 32
title: "CH32: Sed Multi-line Pattern Space Decode"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 7
tags: ['sed', 'pattern-space', 'regex', 'filters']
flag: "HD{sed_multiline_pattern_space_decoder_932}"
---

# 🎯 Topshiriq #32: CH32: Sed Multi-line Pattern Space Decode

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 7 ball`
* **Teglar:** #sed, #pattern-space, #regex, #filters

---

## 📝 Topshiriq Senariysi (Scenario):
Maxfiy ma'lumot faylida flag bir nechta qatorlarga bo'lingan va har bir juft qatordan keyin shifrlangan bayt joylashgan. `sed -n 'N; ...'` yordamida flagni tiklang.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> sed -n 'N;s/\n//;p' /tmp/split_flag.txt | tr -d ' '

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
sed -n 'N;s/\n//;p' /tmp/split_flag.txt | tr -d ' '
```

---

## 🚩 Maxfiy Flag:
`HD{sed_multiline_pattern_space_decoder_932}`
