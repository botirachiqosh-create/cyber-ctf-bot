import asyncio
import os
import logging
import sys
from pathlib import Path
from dotenv import load_dotenv
from aiohttp import web
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

# --- Conditionally import google-genai (may be missing on some envs) ---
try:
    from google import genai
except ImportError:
    genai = None

from ctf_database import (
    register_user, get_user_stats, get_leaderboard,
    verify_flag, get_db, init_db
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.resolve()
load_dotenv(BASE_DIR / ".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

if not TELEGRAM_BOT_TOKEN:
    log.critical("TELEGRAM_BOT_TOKEN yo'q! Railway Variables yoki .env'ga qo'shing.")
    sys.exit(1)

gemini_client = None
if genai and GEMINI_API_KEY:
    try:
        gemini_client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        log.warning(f"Gemini client init xatoligi (bot ishlashga davom etadi): {e}")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# --- DB init ---
init_db()

# --- Populate challenges (safe) ---
try:
    from populate_50_hard_challenges import populate_database_and_vault
    populate_database_and_vault()
    log.info("50 ta Hard CTF bazaga yuklandi.")
except Exception as e:
    log.warning(f"Challengelarni yuklashda xatolik (bot ishlayveradi): {e}")

# --- Keyboard ---
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎯 CTF Topshiriqlar"), KeyboardButton(text="📊 Reyting")],
        [KeyboardButton(text="👤 Profilim")],
    ],
    resize_keyboard=True,
)


def get_challenge_by_id(chal_id: int):
    with get_db() as conn:
        return conn.execute("SELECT * FROM challenges WHERE id = ?", (chal_id,)).fetchone()


def get_total_challenges_count():
    with get_db() as conn:
        return conn.execute("SELECT COUNT(*) as cnt FROM challenges").fetchone()["cnt"]


# ===================== HANDLERS =====================

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user = message.from_user
    u_name = f"@{user.username}" if user.username else f"user_{user.id}"
    register_user(user.id, u_name, user.first_name)
    text = (
        f"Salom, <b>{u_name}</b>! ⚡\n\n"
        f"<b>50 ta Hard CTF Platformasi</b>\n\n"
        f"Boshlash uchun quyidagi tugmalardan birini bosing:"
    )
    await message.answer(text, reply_markup=main_keyboard, parse_mode="HTML")


@dp.message(F.text.in_({"🎯 CTF Topshiriqlar", "CTF", "ctf"}))
@dp.message(Command("ctf"))
async def ctf_list_handler(message: types.Message):
    user_id = message.from_user.id
    stats = get_user_stats(user_id)
    cur_id = stats["current_challenge_id"] if stats else 1

    chal = get_challenge_by_id(cur_id)
    if not chal:
        await message.answer("🎉 Barcha 50 ta topshiriqni yakunladingiz!")
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
        [InlineKeyboardButton(text="💡 Hint", callback_data=f"hint_{chal['id']}")],
        [InlineKeyboardButton(text="⏭️ Keyingi", callback_data=f"next_{chal['id']}")],
    ])
    await message.answer(text, reply_markup=inline_kb, parse_mode="HTML")


@dp.callback_query(F.data.startswith("hint_"))
async def hint_callback(callback: types.CallbackQuery):
    chal_id = int(callback.data.split("_")[1])
    user_id = callback.from_user.id
    with get_db() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO hints_used (user_id, challenge_id) VALUES (?, ?)",
            (user_id, chal_id),
        )
        conn.commit()
        chal = conn.execute("SELECT hint FROM challenges WHERE id = ?", (chal_id,)).fetchone()
    hint_text = chal["hint"] if chal else "Maslahat mavjud emas."
    await callback.message.answer(
        f"💡 <b>Topshiriq #{chal_id} Hint:</b>\n\n<code>{hint_text}</code>",
        parse_mode="HTML",
    )
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
        [InlineKeyboardButton(text="💡 Hint", callback_data=f"hint_{chal['id']}")],
        [InlineKeyboardButton(text="⏭️ Keyingi", callback_data=f"next_{chal['id']}")],
    ])
    try:
        await callback.message.edit_text(text, reply_markup=inline_kb, parse_mode="HTML")
    except Exception:
        await callback.message.answer(text, reply_markup=inline_kb, parse_mode="HTML")
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
        text += f"{medal} <b>{row['username']}</b> — ⭐ {row['score']} ball ({row['solved_count']} flag)\n"
    await message.answer(text, parse_mode="HTML")


@dp.message(F.text == "👤 Profilim")
@dp.message(Command("stats"))
async def stats_handler(message: types.Message):
    user_id = message.from_user.id
    stats = get_user_stats(user_id)
    if not stats:
        await message.answer("Avval /start bosing.")
        return
    text = (
        f"👤 <b>PROFIL:</b>\n━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>User:</b> {stats['username']}\n"
        f"⭐ <b>Ball:</b> {stats['score']}\n"
        f"🚩 <b>Yechilgan:</b> {stats['solved_count']} / 50\n"
        f"🎯 <b>Joriy:</b> #{stats['current_challenge_id']}\n"
    )
    await message.answer(text, parse_mode="HTML")


# --- Flag submission ---
@dp.message(F.text.startswith("HD{") & F.text.endswith("}"))
async def flag_submission_handler(message: types.Message):
    user_id = message.from_user.id
    flag = message.text.strip()
    res = verify_flag(user_id, flag)
    if res["status"] == "correct":
        stats = get_user_stats(user_id)
        cur_id = stats["current_challenge_id"]
        next_id = cur_id + 1
        with get_db() as conn:
            conn.execute("UPDATE users SET current_challenge_id = ? WHERE user_id = ?", (next_id, user_id))
            conn.commit()
        next_chal = get_challenge_by_id(next_id)
        next_msg = (
            f"\n\n👉 <b>Keyingi:</b> #{next_chal['id']} — {next_chal['title']}"
            if next_chal
            else "\n\n🏆 50 TA TOPSHIRIQ YAKUNLANDI!"
        )
        await message.answer(
            f"🎉 <b>TO'G'RI! +{res['points']} ball!</b>" + next_msg,
            parse_mode="HTML",
        )
    else:
        await message.answer(res["msg"])


# --- Generic Gemini AI ---
@dp.message(F.text)
async def generic_text_handler(message: types.Message):
    if message.text.startswith("/"):
        return
    try:
        if gemini_client:
            await bot.send_chat_action(chat_id=message.chat.id, action="typing")
            resp = gemini_client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=f"Qisqa javob ber: {message.text}",
            )
            await message.answer(resp.text[:4000])
        else:
            await message.answer("Topshiriqni boshlash uchun /start bosing.")
    except Exception as e:
        log.warning(f"Gemini xatoligi: {e}")
        await message.answer("Topshiriqni boshlash uchun /start bosing.")


# ===================== HEALTH CHECK + MAIN =====================

async def handle_health(request):
    return web.Response(text="OK", status=200)


async def start_web_server():
    port = int(os.environ.get("PORT", "8080"))
    app = web.Application()
    app.router.add_get("/", handle_health)
    app.router.add_get("/health", handle_health)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    log.info(f"Health check server :{port} da ishga tushdi")


async def main():
    log.info("Bot ishga tushmoqda...")
    try:
        await start_web_server()
    except Exception as e:
        log.warning(f"Health server xatoligi (bot ishlayveradi): {e}")

    # Polling — cheksiz qayta urinish
    while True:
        try:
            log.info("Telegram polling boshlanmoqda...")
            await dp.start_polling(bot, handle_signals=False)
        except Exception as e:
            log.error(f"Polling uzildi: {e}")
            await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(main())
