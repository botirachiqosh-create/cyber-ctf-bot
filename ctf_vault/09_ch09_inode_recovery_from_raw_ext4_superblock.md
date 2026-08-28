---
id: 9
title: "CH09: Inode Recovery from Raw Ext4 Superblock"
module: "Modul 1: Memory & /proc Forensics"
difficulty: Hard
points: 10
tags: ['ext4', 'debugfs', 'inodes', 'forensics']
flag: "HD{ext4_inode_raw_superblock_recovery_909}"
---

# 🎯 Topshiriq #9: CH09: Inode Recovery from Raw Ext4 Superblock

## 📌 Metama'lumotlar:
* **Modul:** `Modul 1: Memory & /proc Forensics`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 10 ball`
* **Teglar:** #ext4, #debugfs, #inodes, #forensics

---

## 📝 Topshiriq Senariysi (Scenario):
/tmp/vault_partition.img faylida ext4 tizimi shikastlangan. Inode jadvalini `debugfs` yoki `fls/icat` orqali tahlil qilib, 1337-inodeda saqlangan o'chirilgan faylni tiklang.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> debugfs -R 'cat <1337>' /tmp/vault_partition.img

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
debugfs -R 'cat <1337>' /tmp/vault_partition.img
```

---

## 🚩 Maxfiy Flag:
`HD{ext4_inode_raw_superblock_recovery_909}`
