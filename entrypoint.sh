#!/bin/bash

echo "🚀 [1/4] CTF Ma'lumotlar bazasi initsializatsiya qilinmoqda..."
python /app/populate_50_hard_challenges.py || true

echo "🚀 [2/4] Jonli CTF Target xizmatlari ishga tushmoqda..."
python /app/spawn_live_ctf_services.py > /tmp/services.log 2>&1 &

echo "🚀 [3/4] Multi-User SSH Server ishga tushmoqda..."
python /app/pty_ssh_server.py > /tmp/ssh.log 2>&1 &

echo "🚀 [4/4] Telegram Bot 24/7 doimiy avto-tiklanish (Supervised) rejimida..."
while true; do
    echo "[*] Telegram Bot ishga tushirilmoqda..."
    python /app/bot.py
    echo "[!] Bot kodi to'xtadi. 2 soniyadan so'ng avtomatik qayta ishga tushadi..."
    sleep 2
done
