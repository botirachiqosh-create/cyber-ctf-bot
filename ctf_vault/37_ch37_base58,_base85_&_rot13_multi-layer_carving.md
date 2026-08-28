---
id: 37
title: "CH37: Base58, Base85 & Rot13 Multi-Layer Carving"
module: "Modul 4: Log Forensics & Filters"
difficulty: Hard
points: 7
tags: ['base58', 'rot13', 'base85', 'crypto']
flag: "HD{multilayer_base58_rot13_pipeline_carver_937}"
---

# 🎯 Topshiriq #37: CH37: Base58, Base85 & Rot13 Multi-Layer Carving

## 📌 Metama'lumotlar:
* **Modul:** `Modul 4: Log Forensics & Filters`
* **Qiyinlik darajasi:** `🔴 Hard`
* **Maksimal Ball:** `⭐ 7 ball`
* **Teglar:** #base58, #rot13, #base85, #crypto

---

## 📝 Topshiriq Senariysi (Scenario):
Fayldagi ma'lumot avval Rot13, keyin Base58, so'ng Base85 bilan shifrlangan. Bitta quvur liniyasi (One-liner) orqali barcha qatlamlarni yeching.

---

## 💡 Kichik Maslahat (Hint):
> [!TIP]
> cat payload.enc | tr 'A-Za-z' 'N-ZA-Mn-za-m' | python3 -c 'import base58, base64, sys; ...'

---

## 🛠️ Professional Yechim Ko'rsatmasi:
```bash
# Topshiriqni yechish bo'yicha ko'rsatma:
cat payload.enc | tr 'A-Za-z' 'N-ZA-Mn-za-m' | python3 -c 'import base58, base64, sys; ...'
```

---

## 🚩 Maxfiy Flag:
`HD{multilayer_base58_rot13_pipeline_carver_937}`
