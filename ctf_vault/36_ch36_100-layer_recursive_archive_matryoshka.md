---
id: 36
title: "CH36: 100-Layer Recursive Archive Matryoshka"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 8
tags: ['archive', 'matryoshka', 'bash-script', 'automation']
flag: "HD{recursive_archive_matryoshka_unpacker_936}"
---

# 🎯 Topshiriq #36: CH36: 100-Layer Recursive Archive Matryoshka

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 8 ball`
* **Teglar:** #archive, #matryoshka, #bash-script, #automation

---

## 📝 Topshiriq Senariysi (Scenario):
Fayl 100 qatlamli turli xil arxivlar (.tar.gz, .bz2, .xz, .zip, .7z) bilan siqilgan. Avtomatlashtirilgan bash script yozib, eng ichki qatlamdagi flagni chiqaring.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> while true; do 7z x archive.* -y || tar -xf archive.* || unzip archive.* || break; done

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
while true; do 7z x archive.* -y || tar -xf archive.* || unzip archive.* || break; done
```

---

## 🚩 Maxfiy Flag:
`HD{recursive_archive_matryoshka_unpacker_936}`
