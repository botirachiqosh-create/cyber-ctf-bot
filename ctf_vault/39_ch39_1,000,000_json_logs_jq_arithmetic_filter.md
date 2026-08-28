---
id: 39
title: "CH39: 1,000,000 JSON Logs JQ Arithmetic Filter"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 8
tags: ['jq', 'json', 'big-data', 'filters']
flag: "HD{jq_json_million_log_arithmetic_filter_939}"
---

# 🎯 Topshiriq #39: CH39: 1,000,000 JSON Logs JQ Arithmetic Filter

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #jq, #json, #big-data, #filters

---

## 📝 Topshiriq Senariysi (Scenario):
/var/log/cloud_events.json ichida 1 millionta JSON hodisa mavjud. `response_time > 4500` va `status == 500` bo'lgan, `user_id` juft son bo'lgan barcha yozuvlarni toping.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> jq -r '.[] | select(.response_time > 4500 and .status == 500 and .user_id % 2 == 0) | .flag' /var/log/cloud_events.json

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
jq -r '.[] | select(.response_time > 4500 and .status == 500 and .user_id % 2 == 0) | .flag' /var/log/cloud_events.json
```

---

## 🚩 Maxfiy Flag:
`HD{jq_json_million_log_arithmetic_filter_939}`
