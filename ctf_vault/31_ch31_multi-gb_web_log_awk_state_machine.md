---
id: 31
title: "CH31: Multi-GB Web Log AWK State Machine"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 8
tags: ['awk', 'log-analysis', 'sqli', 'forensics']
flag: "HD{awk_state_machine_multigb_log_forensics_931}"
---

# 🎯 Topshiriq #31: CH31: Multi-GB Web Log AWK State Machine

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #awk, #log-analysis, #sqli, #forensics

---

## 📝 Topshiriq Senariysi (Scenario):
/var/log/traffic/access.log (1.5 GB) ichida bir xil User-Agent bilan 3 ta turli xil IP dan SQL Injection payload yuborgan hujumchi IP larini AWK state machine bilan toping.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> awk -F'"' '{print $6}' /var/log/traffic/access.log | sort | uniq -c | sort -nr

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
awk -F'"' '{print $6}' /var/log/traffic/access.log | sort | uniq -c | sort -nr
```

---

## 🚩 Maxfiy Flag:
`HD{awk_state_machine_multigb_log_forensics_931}`
