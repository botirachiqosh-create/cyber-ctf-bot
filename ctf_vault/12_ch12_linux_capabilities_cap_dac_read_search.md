---
id: 12
title: "CH12: Linux Capabilities cap_dac_read_search"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 8
tags: ['capabilities', 'cap_dac_read', 'privesc', 'shadow']
flag: "HD{cap_dac_read_search_arbitrary_read_912}"
---

# 🎯 Topshiriq #12: CH12: Linux Capabilities cap_dac_read_search

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #capabilities, #cap_dac_read, #privesc, #shadow

---

## 📝 Topshiriq Senariysi (Scenario):
/opt/audit/log_reader binar fayli 'cap_dac_read_search+ep' qobiliyatiga ega. Ushbu ruxsat fayl tizimidagi istalgan ruxsatsiz fayllarni o'qish imkonini beradi. /etc/shadow va /root/flag.txt ni o'qing.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> /opt/audit/log_reader /root/flag.txt

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
/opt/audit/log_reader /root/flag.txt
```

---

## 🚩 Maxfiy Flag:
`HD{cap_dac_read_search_arbitrary_read_912}`
