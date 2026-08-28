---
id: 48
title: "CH48: PAM Authentication Module Backdoor Analysis"
module: "Modul 5: Automation, Systemd & Kernel"
difficulty: Hard
points: 8
tags: ['pam', 'authentication', 'backdoor', 'security']
flag: "HD{pam_authentication_module_backdoor_hunter_948}"
---

# 🎯 Topshiriq #48: CH48: PAM Authentication Module Backdoor Analysis

## 📌 Metama'lumotlar:
* **Modul:** `Modul 5: Automation, Systemd & Kernel`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #pam, #authentication, #backdoor, #security

---

## 📝 Topshiriq Senariysi (Scenario):
/etc/pam.d/common-auth faylida kiber-hujumchi tomonidan 'pam_permit.so' yoki maxfiy master-parol moduli joylashtirilgan. PAM konfiguratsiyasini tahlil qilib universal parolni toping.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> grep -rn 'pam_exec' /etc/pam.d/ yoki /etc/security/

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
grep -rn 'pam_exec' /etc/pam.d/ yoki /etc/security/
```

---

## 🚩 Maxfiy Flag:
`HD{pam_authentication_module_backdoor_hunter_948}`
