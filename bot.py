import asyncio
import os
import time
import logging
from pathlib import Path
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, 
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardRemove
)
from google import genai
from google.genai import types as genai_types
from ctf_database import (
    register_user, get_user_stats, get_leaderboard, 
    verify_flag, get_db
)
from instance_orchestrator import spawn_challenge_instance, destroy_user_instances

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv("/app/.env" if os.path.exists("/app/.env") else "/home/fara/.gemini/antigravity/scratch/telegram_video_bot/.env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment")

gemini_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else genai.Client()
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

TEMP_DIR = Path("/tmp")

# Main Keyboard
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎯 50 ta Hard CTF"), KeyboardButton(text="🚀 Yangi Lab IP")],
        [KeyboardButton(text="⏹️ Labni O'chirish"), KeyboardButton(text="📊 Reyting")],
        [KeyboardButton(text="👤 Profilim")]
    ],
    resize_keyboard=True
)

def get_challenge_by_id(chal_id: int):
    with get_db() as conn:
        return conn.execute("SELECT * FROM challenges WHERE id = ?", (chal_id,)).fetchone()

def get_total_challenges_count():
    with get_db() as conn:
        return conn.execute("SELECT COUNT(*) as count FROM challenges").fetchone()["count"]

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user = message.from_user
    u_name = f"@{user.username}" if user.username else f"user_{user.id}"
    register_user(user.id, u_name, user.first_name)
    
    text = (
        f"Salom, <b>{u_name}</b>! ⚡\n\n"
        f"<b>50 ta Hard CTF & 1-ga-1 SSH Lab Platformasi</b>\n\n"
        f"• Har bir topshiriq uchun alohida unikal IP beriladi.\n"
        f"• Ishlatilgach, avtomatik o'chadi.\n\n"
        f"Boshlash uchun quyidagi tugmalardan birini bosing:"
    )
    await message.answer(text, reply_markup=main_keyboard, parse_mode="HTML")

@dp.message(F.text.contains("50 ta Hard CTF") | F.text.contains("CTF"))
@dp.message(Command("ctf"))
async def ctf_list_handler(message: types.Message):
    user_id = message.from_user.id
    stats = get_user_stats(user_id)
    cur_id = stats["current_challenge_id"] if stats else 1
    
    chal = get_challenge_by_id(cur_id)
    if not chal:
        await message.answer("🎉 Barcha 50 ta Hard topshiriqni yakunladingiz!")
        return
        
    text = (
        f"🎯 <b>TOPSHIRIQ #{chal['id']} / 50:</b> {chal['title']}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📂 <b>Modul:</b> {chal['module']}\n"
        f"⚡ <b>Qiyinlik:</b> 🔴 Hard ({chal['points']} ball)\n\n"
        f"📝 <b>Vazifa:</b>\n{chal['description']}\n\n"
        f"🚩 <b>Flag:</b> <code>HD{{...}}</code>"
    )
    
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Labni Ochish (IP)", callback_data=f"spawn_{chal['id']}"),
            InlineKeyboardButton(text="💡 Kichik Hint", callback_data=f"hint_{chal['id']}")
        ],
        [
            InlineKeyboardButton(text="⏭️ Keyingi topshiriq", callback_data=f"next_{chal['id']}")
        ]
    ])
    await message.answer(text, reply_markup=inline_kb, parse_mode="HTML")

@dp.message(F.text == "🚀 Yangi Lab IP")
@dp.message(Command("spawn"))
async def spawn_instance_cmd(message: types.Message):
    user_id = message.from_user.id
    stats = get_user_stats(user_id)
    cur_id = stats["current_challenge_id"] if stats else 1
    
    inst = spawn_challenge_instance(user_id, cur_id, 60)
    
    text = (
        f"⚡ <b>SHAXSIY LAB INSTANSIYANGIZ:</b>\n\n"
        f"🎯 <b>Topshiriq:</b> #{cur_id} — {inst['challenge_title']}\n"
        f"🌐 <b>IP:</b> <code>127.0.0.1</code> (Virtual: <code>{inst['ip_address']}</code>)\n"
        f"🔌 <b>Port:</b> <code>{inst['ssh_port']}</code>\n"
        f"👤 <b>Login:</b> <code>{inst['username']}</code>\n"
        f"🔒 <b>Parol:</b> <code>{inst['password']}</code>\n\n"
        f"💻 <b>Ulanish buyrug'i:</b>\n"
        f"<code>ssh {inst['username']}@127.0.0.1 -p {inst['ssh_port']}</code>\n\n"
        f"⏱️ <i>60 daqiqadan so'ng avtomatik o'chadi.</i>"
    )
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⏹️ Labni O'chirish", callback_data="destroy_inst")]
    ])
    await message.answer(text, reply_markup=inline_kb, parse_mode="HTML")

@dp.callback_query(F.data.startswith("spawn_"))
async def spawn_callback(callback: types.CallbackQuery):
    chal_id = int(callback.data.split("_")[1])
    user_id = callback.from_user.id
    
    inst = spawn_challenge_instance(user_id, chal_id, 60)
    text = (
        f"⚡ <b>SHAXSIY LAB INSTANSIYANGIZ:</b>\n\n"
        f"🎯 <b>Topshiriq:</b> #{chal_id} — {inst['challenge_title']}\n"
        f"🌐 <b>IP:</b> <code>127.0.0.1</code> (Virtual: <code>{inst['ip_address']}</code>)\n"
        f"🔌 <b>Port:</b> <code>{inst['ssh_port']}</code>\n"
        f"👤 <b>Login:</b> <code>{inst['username']}</code>\n"
        f"🔒 <b>Parol:</b> <code>{inst['password']}</code>\n\n"
        f"💻 <b>Ulanish buyrug'i:</b>\n"
        f"<code>ssh {inst['username']}@127.0.0.1 -p {inst['ssh_port']}</code>"
    )
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⏹️ Labni O'chirish", callback_data="destroy_inst")]
    ])
    await callback.message.answer(text, reply_markup=inline_kb, parse_mode="HTML")
    await callback.answer()

@dp.message(F.text == "⏹️ Labni O'chirish")
@dp.callback_query(F.data == "destroy_inst")
async def destroy_cmd(event: types.Message | types.CallbackQuery):
    user_id = event.from_user.id
    destroy_user_instances(user_id)
    text = "🗑️ <b>Lab instansiyasi va IP butunlay o'chirildi!</b>"
    if isinstance(event, types.CallbackQuery):
        await event.message.answer(text, parse_mode="HTML")
        await event.answer()
    else:
        await event.answer(text, parse_mode="HTML")

@dp.callback_query(F.data.startswith("hint_"))
async def hint_callback(callback: types.CallbackQuery):
    chal_id = int(callback.data.split("_")[1])
    user_id = callback.from_user.id
    
    with get_db() as conn:
        conn.execute("INSERT OR IGNORE INTO hints_used (user_id, challenge_id) VALUES (?, ?)", (user_id, chal_id))
        conn.commit()
        chal = conn.execute("SELECT hint FROM challenges WHERE id = ?", (chal_id,)).fetchone()
        
    hint_text = chal["hint"] if chal else "Maslahat mavjud emas."
    await callback.message.answer(f"💡 <b>Topshiriq #{chal_id} Hint:</b>\n\n<code>{hint_text}</code>", parse_mode="HTML")
    await callback.answer()

@dp.callback_query(F.data.startswith("next_"))
async def next_callback(callback: types.CallbackQuery):
    current_id = int(callback.data.split("_")[1])
    user_id = callback.from_user.id
    total = get_total_challenges_count()
    
    next_id = current_id + 1 if current_id < total else 1
    with get_db() as conn:
        conn.execute("UPDATE users SET current_challenge_id = ? WHERE user_id = ?", (next_id, user_id))
        conn.commit()
        
    chal = get_challenge_by_id(next_id)
    text = (
        f"🎯 <b>TOPSHIRIQ #{chal['id']} / 50:</b> {chal['title']}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📂 <b>Modul:</b> {chal['module']}\n"
        f"⚡ <b>Qiyinlik:</b> 🔴 Hard ({chal['points']} ball)\n\n"
        f"📝 <b>Vazifa:</b>\n{chal['description']}\n\n"
        f"🚩 <b>Flag:</b> <code>HD{{...}}</code>"
    )
    
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Labni Ochish (IP)", callback_data=f"spawn_{chal['id']}"),
            InlineKeyboardButton(text="💡 Kichik Hint", callback_data=f"hint_{chal['id']}")
        ],
        [
            InlineKeyboardButton(text="⏭️ Keyingi topshiriq", callback_data=f"next_{chal['id']}")
        ]
    ])
    await callback.message.edit_text(text, reply_markup=inline_kb, parse_mode="HTML")
    await callback.answer()

@dp.message(F.text == "📊 Reyting")
@dp.message(Command("leaderboard"))
async def leaderboard_handler(message: types.Message):
    leaders = get_leaderboard(10)
    if not leaders:
        await message.answer("🏆 Hozircha hech kim flag topshirmagan.")
        return
        
    text = "🏆 <b>TOP-10 CTF REYTINGI:</b>\n━━━━━━━━━━━━━━━━━━━━\n"
    medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    
    for i, row in enumerate(leaders):
        medal = medals[i] if i < len(medals) else f"{i+1}."
        u_handle = row["username"] if row["username"].startswith("@") else f"@{row['username']}"
        text += f"{medal} <b>{u_handle}</b> — ⭐ {row['score']} ball ({row['solved_count']} ta flag)\n"
        
    await message.answer(text, parse_mode="HTML")

@dp.message(F.text == "👤 Profilim")
@dp.message(Command("stats"))
async def stats_handler(message: types.Message):
    user_id = message.from_user.id
    stats = get_user_stats(user_id)
    if not stats:
        await message.answer("Siz hali topshiriq bajarmadingiz.")
        return
        
    u_handle = stats["username"] if stats["username"].startswith("@") else f"@{stats['username']}"
    text = (
        f"👤 <b>PROFIL:</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>User:</b> {u_handle}\n"
        f"⭐ <b>Ball:</b> {stats['score']} ball\n"
        f"🚩 <b>Yechilgan:</b> {stats['solved_count']} / 50 ta\n"
        f"🎯 <b>Joriy topshiriq:</b> #{stats['current_challenge_id']}\n"
    )
    await message.answer(text, parse_mode="HTML")

# Flag submission detector
@dp.message(F.text.startswith("HD{") & F.text.endswith("}"))
async def flag_submission_handler(message: types.Message):
    user_id = message.from_user.id
    flag = message.text.strip()
    
    res = verify_flag(user_id, flag)
    if res["status"] == "correct":
        destroy_user_instances(user_id)
        stats = get_user_stats(user_id)
        cur_id = stats["current_challenge_id"]
        next_id = cur_id + 1
        with get_db() as conn:
            conn.execute("UPDATE users SET current_challenge_id = ? WHERE user_id = ?", (next_id, user_id))
            conn.commit()
            
        next_chal = get_challenge_by_id(next_id)
        next_msg = f"\n\n👉 <b>Keyingi topshiriq:</b> #{next_chal['id']} — {next_chal['title']}" if next_chal else "\n\n🏆 50 TA TOPSHIRIQ YAKUNLANDI!"
        await message.answer(f"🎉 <b>TO'G'RI! +{res['points']} ball!</b>\n🗑️ <i>Lab instansiyasi o'chirildi.</i>" + next_msg, parse_mode="HTML")
    else:
        await message.answer(res["msg"])

# Generic text / questions with Gemini
@dp.message(F.text)
async def generic_text_handler(message: types.Message):
    if message.text.startswith("/"):
        return
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    prompt = f"Talabaning savoli: {message.text}\nQisqa, aniq va lo'nda javob bering."
    resp = gemini_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    await message.answer(resp.text)

async def main():
    print("🤖 1-ga-1 CTF Bot 24/7 ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
