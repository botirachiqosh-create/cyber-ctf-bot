---
id: 40
title: "CH40: Time-based Correlation of wtmp & btmp Logs"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 8
tags: ['utmpdump', 'wtmp', 'btmp', 'timeline']
flag: "HD{utmpdump_wtmp_btmp_timeline_correlation_940}"
---

# 🎯 Topshiriq #40: CH40: Time-based Correlation of wtmp & btmp Logs

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #utmpdump, #wtmp, #btmp, #timeline

---

## 📝 Topshiriq Senariysi (Scenario):
/var/log/btmp va /var/log/wtmp binar loglarini `utmpdump` orqali taqqoslab, tizim o'chirilishidan roppa-rosa 3 soniya oldin kirgan foydalanuvchini aniqlang.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> utmpdump /var/log/wtmp | grep 'reboot' -B2

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
utmpdump /var/log/wtmp | grep 'reboot' -B2
```

---

## 🚩 Maxfiy Flag:
`HD{utmpdump_wtmp_btmp_timeline_correlation_940}`
