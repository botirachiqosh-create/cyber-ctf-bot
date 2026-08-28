---
id: 38
title: "CH38: PCAP Dump SMB File Stream Extraction"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 9
tags: ['pcap', 'tshark', 'smb', 'packet-analysis']
flag: "HD{tshark_pcap_smb_file_carver_master_938}"
---

# 🎯 Topshiriq #38: CH38: PCAP Dump SMB File Stream Extraction

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #pcap, #tshark, #smb, #packet-analysis

---

## 📝 Topshiriq Senariysi (Scenario):
/tmp/capture.pcap faylida SMB2 protokoli orqali uzatilgan fayl oqimi saqlangan. `tshark` yordamida uzatilgan faylni to'liq ajratib oling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> tshark -r /tmp/capture.pcap --export-objects smb,/tmp/extracted/

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
tshark -r /tmp/capture.pcap --export-objects smb,/tmp/extracted/
```

---

## 🚩 Maxfiy Flag:
`HD{tshark_pcap_smb_file_carver_master_938}`
