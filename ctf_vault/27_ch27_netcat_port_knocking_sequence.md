---
id: 27
title: "CH27: Netcat Port Knocking Sequence"
module: "Modul 3: Streams, FIFO & Sockets"
difficulty: Hard
points: 9
tags: ['port-knocking', 'firewall', 'iptables', 'netcat']
flag: "HD{port_knocking_firewall_sequence_bypass_927}"
---

# 🎯 Topshiriq #27: CH27: Netcat Port Knocking Sequence

## 📌 Metama'lumotlar:
* **Modul:** `Modul 3: Streams, FIFO & Sockets`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #port-knocking, #firewall, #iptables, #netcat

---

## 📝 Topshiriq Senariysi (Scenario):
Xavfsizlik devori 1337-portni yopib qo'ygan. Unga ulanish uchun ketma-ket 7000, 8000, 9000 portlariga TCP paket yuborib (Port Knocking), 1337-portdagi flagni oching.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> for p in 7000 8000 9000; do nc -z -w1 127.0.0.1 $p; done; nc 127.0.0.1 1337

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
for p in 7000 8000 9000; do nc -z -w1 127.0.0.1 $p; done; nc 127.0.0.1 1337
```

---

## 🚩 Maxfiy Flag:
`HD{port_knocking_firewall_sequence_bypass_927}`
