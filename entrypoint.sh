#!/bin/bash
set -e

echo "🚀 [1/4] CTF Ma'lumotlar bazasi initsializatsiya qilinmoqda..."
python /app/populate_50_hard_challenges.py

echo "🚀 [2/4] Jonli CTF Target xizmatlari (sockets, named pipes) ishga tushmoqda..."
python /app/spawn_live_ctf_services.py &

echo "🚀 [3/4] Multi-User SSH Server (Port 2222) ishga tushmoqda..."
python /app/pty_ssh_server.py &

echo "🚀 [4/4] Telegram Bot (@fara_ai_vision_bot) 24/7 rejimda ishga tushmoqda..."
exec python /app/bot.py
