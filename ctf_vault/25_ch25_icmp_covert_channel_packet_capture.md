---
id: 25
title: "CH25: ICMP Covert Channel Packet Capture"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 8
tags: ['tcpdump', 'icmp', 'covert-channel', 'pcap']
flag: "HD{icmp_ping_covert_channel_exfiltration_925}"
---

# 🎯 Topshiriq #25: CH25: ICMP Covert Channel Packet Capture

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #tcpdump, #icmp, #covert-channel, #pcap

---

## 📝 Topshiriq Senariysi (Scenario):
Lokal interfeysda har 5 soniyada ICMP (Ping) paketlarining Data bo'limida maxfiy flag qismlari yashirin yuborilmoqda. `tcpdump` yordamida paketlarni ushlab flagni tiklang.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> tcpdump -i lo -nnvv -X icmp -c 10

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
tcpdump -i lo -nnvv -X icmp -c 10
```

---

## 🚩 Maxfiy Flag:
`HD{icmp_ping_covert_channel_exfiltration_925}`
