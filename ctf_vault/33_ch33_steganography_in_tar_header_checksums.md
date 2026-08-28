---
id: 33
title: "CH33: Steganography in Tar Header Checksums"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 9
tags: ['tar', 'steganography', 'hexdump', 'forensics']
flag: "HD{tar_header_checksum_steganography_933}"
---

# 🎯 Topshiriq #33: CH33: Steganography in Tar Header Checksums

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 9 ball`
* **Teglar:** #tar, #steganography, #hexdump, #forensics

---

## 📝 Topshiriq Senariysi (Scenario):
/tmp/archive.tar faylidagi har bir fayl sarlavhasining (Header Checksum) 8-baytlik maydoniga maxfiy xabar bitlari yashirilgan. Hexdump orqali sarlavhalarni tahlil qiling.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> hexdump -C /tmp/archive.tar | grep -B1 '00000000'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
hexdump -C /tmp/archive.tar | grep -B1 '00000000'
```

---

## 🚩 Maxfiy Flag:
`HD{tar_header_checksum_steganography_933}`
