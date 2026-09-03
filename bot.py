import asyncio
import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.default import DefaultBotProperties
from google import genai
from google.genai import types as genai_types

# Log sozlamalari
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

BASE_DIR = Path(__file__).parent.resolve()
load_dotenv(BASE_DIR / ".env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

DOWNLOADS_DIR = BASE_DIR / "downloads"
DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

# Gemini Client
gemini_client = None
if GEMINI_API_KEY:
    try:
        gemini_client = genai.Client(api_key=GEMINI_API_KEY)
        logging.info("✅ Gemini AI mijozi muvaffaqiyatli ulandi.")
    except Exception as e:
        logging.error(f"⚠️ Gemini client ulanishda xato: {e}")

# Proxy sozlamasi (agar kerak bo'lsa)
proxy_url = os.environ.get("http_proxy") or os.environ.get("https_proxy")
if proxy_url:
    session = AiohttpSession(proxy=proxy_url)
    bot = Bot(token=TELEGRAM_BOT_TOKEN, session=session, default=DefaultBotProperties(parse_mode=None))
else:
    bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=None))

dp = Dispatcher()

# Bir vaqtning o'zida serverni va tarmoqni band qilmaslik uchun cheklov
ai_semaphore = asyncio.Semaphore(2)

SYSTEM_INSTRUCTION = """
Sen foydalanuvchining shaxsiy universal bilimdoni va repetitorisan.
Senga foydalanuvchi turli materiallarni yuboradi:
- Qo'lyozma konspektlar, darslik sahifalari, testlar, qoidalar va misollar;
- Ona tili va adabiyot, matematika, fizika, tarix yoki boshqa fanlardan mavzular;
- PDF kitoblar va matnli savollar.

SENING ASOSIY VAZIFANG:
1. Yuborilgan rasm, matn yoki hujjatni juda diqqat bilan o'qib chiqish.
2. Rasmdagi qo'lyozmani to'liq o'qib, mavzuni tartibli, chiroyli va tushunarli qilib konspekt/tahlil qilib berish.
3. Agar bu qoidalar bo'lsa (masalan, Tarixizmlar, Arxaizmlar, Neologizmlar, Yordamchi so'zlar va h.k.):
   - Har bir tushunchaning ma'nosi va misollarini aniq ko'rsat;
   - Imtihonda yoki testda qanday savollar tushishi mumkinligini ayt;
   - Yodlash uchun qulay qisqa xulosa ber.
4. Javoblarni o'zbek tilida (lotin alifbosida), juda samimiy va chiroyli tartibda taqdim et.
"""

def sync_gemini_call(contents):
    """Sinxron Gemini chaqiruvi (thread ichida ishlaydi)"""
    models_to_try = ["gemini-3.5-flash-lite", "gemini-3.5-flash", "gemini-3.6-flash"]
    last_err = None
    for model_name in models_to_try:
        try:
            res = gemini_client.models.generate_content(
                model=model_name,
                contents=contents
            )
            if res and res.text:
                return res.text
        except Exception as e:
            last_err = e
            logging.warning(f"Model {model_name} ogohlantirish: {e}")
    raise Exception(f"Barcha modellar xato berdi: {last_err}")

async def call_gemini(contents):
    """Event loopni to'xtatib qo'ymaslik uchun alohida thread'da chaqirish"""
    async with ai_semaphore:
        return await asyncio.to_thread(sync_gemini_call, contents)

async def safe_send_text(message: types.Message, text: str):
    """Telegram limiti (4096 belgi) bo'yicha xavfsiz bo'lib jo'natish"""
    if not text:
        text = "Tahlil natijasi bo'sh."
    
    max_len = 3900
    if len(text) <= max_len:
        try:
            await message.answer(text)
        except Exception as e:
            logging.error(f"Xabar jo'natishda xato: {e}")
        return

    chunks = []
    lines = text.split("\n")
    cur = ""
    for line in lines:
        if len(cur) + len(line) + 1 > max_len:
            chunks.append(cur)
            cur = line + "\n"
        else:
            cur += line + "\n"
    if cur.strip():
        chunks.append(cur)

    for ch in chunks:
        try:
            await message.answer(ch)
            await asyncio.sleep(0.3)
        except Exception as e:
            logging.error(f"Chunk jo'natishda xato: {e}")

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    """Start: eski tugmalarni yo'qotadi va toza rejimga o'tadi"""
    welcome_text = (
        "👋 Assalomu alaykum!\n\n"
        "Bot to'liq tozalandi. Barcha eski tugmalar va xizmatlar olib tashlandi. 🧹✨\n\n"
        "📥 Menga istalgan narsani yuboring:\n"
        "📸 Daftardagi konspekt yoki darslik rasmini (istalgancha rasm yuborishingiz mumkin);\n"
        "📄 PDF kitob yoki hujjatlarni;\n"
        "✍️ Matnli savol yoki misollarni.\n\n"
        "Har birini batafsil o'qib, chiroyli tushuntirib beraman! 👇"
    )
    try:
        await message.answer(welcome_text, reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        logging.error(f"Start xato: {e}")

@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await safe_send_text(
        message,
        "ℹ️ Botdan foydalanish:\n"
        "Daftaringizdagi konspekt rasmini, darslik sahifasini yoki savolingizni yuboring — bot uni o'qib, to'liq tahlilini yozib beradi."
    )

@dp.message(F.photo)
async def photo_handler(message: types.Message):
    """Rasm va konspektlarni o'qish"""
    local_path = None
    status_msg = None
    try:
        status_msg = await message.answer("🔍 Rasm qabul qilindi, o'qilmoqda...")
    except Exception:
        pass

    try:
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        local_path = DOWNLOADS_DIR / f"photo_{message.message_id}_{photo.file_id[:6]}.jpg"
        await bot.download_file(file_info.file_path, local_path)

        image_bytes = local_path.read_bytes()
        user_prompt = message.caption or (
            "Ushbu rasmdagi qo'lyozma konspekt yoki matnni to'liq o'qib ol. "
            "Unda nima yozilganini aniq keltir va mavzuni sodda, tartibli, "
            "misollar va testda tushishi mumkin bo'lgan muhim qoidalari bilan to'liq tushuntirib ber."
        )

        prompt_parts = [
            genai_types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
            f"{SYSTEM_INSTRUCTION}\n\nFoydalanuvchi topshirig'i:\n{user_prompt}"
        ]

        reply_text = await call_gemini(prompt_parts)
        
        if status_msg:
            try:
                await status_msg.delete()
            except Exception:
                pass

        await safe_send_text(message, reply_text)

    except Exception as e:
        logging.error(f"Rasm tahlilida xato: {e}")
        if status_msg:
            try:
                await status_msg.edit_text(f"⚠️ Rasm tahlilida xatolik: {e}")
            except Exception:
                pass
    finally:
        if local_path and local_path.exists():
            try:
                local_path.unlink()
            except Exception:
                pass

@dp.message(F.document)
async def document_handler(message: types.Message):
    """PDF va hujjatlarni tahlil qilish"""
    doc = message.document
    filename = doc.file_name or f"file_{doc.file_id[:8]}"
    local_path = None
    status_msg = None

    try:
        status_msg = await message.answer(f"📥 {filename} qabul qilindi. O'qilmoqda...")
    except Exception:
        pass

    try:
        file_info = await bot.get_file(doc.file_id)
        local_path = DOWNLOADS_DIR / filename
        await bot.download_file(file_info.file_path, local_path)

        user_prompt = message.caption or (
            "Ushbu hujjatni to'liq o'qib chiq va barcha asosiy mavzular, qoidalar "
            "va misollarni qadamma-qadam eng sodda tilda tahlil qilib ber."
        )

        # Upload via Gemini File API
        def upload_and_process():
            uploaded = gemini_client.files.upload(file=str(local_path))
            return sync_gemini_call([uploaded, f"{SYSTEM_INSTRUCTION}\n\nFoydalanuvchi talabi:\n{user_prompt}"])

        async with ai_semaphore:
            reply_text = await asyncio.to_thread(upload_and_process)

        if status_msg:
            try:
                await status_msg.delete()
            except Exception:
                pass

        await safe_send_text(message, reply_text)

    except Exception as e:
        logging.error(f"Hujjat tahlilida xato: {e}")
        if status_msg:
            try:
                await status_msg.edit_text(f"⚠️ Hujjat tahlilida xatolik: {e}")
            except Exception:
                pass
    finally:
        if local_path and local_path.exists():
            try:
                local_path.unlink()
            except Exception:
                pass

@dp.message(F.voice | F.audio)
async def audio_handler(message: types.Message):
    """Ovozli xabarlar"""
    local_path = None
    status_msg = None
    try:
        status_msg = await message.answer("🎙 Ovoz tinglanmoqda...")
    except Exception:
        pass

    try:
        audio_obj = message.voice or message.audio
        file_info = await bot.get_file(audio_obj.file_id)
        local_path = DOWNLOADS_DIR / f"audio_{message.message_id}.ogg"
        await bot.download_file(file_info.file_path, local_path)

        audio_bytes = local_path.read_bytes()
        prompt_parts = [
            genai_types.Part.from_bytes(data=audio_bytes, mime_type="audio/ogg"),
            f"{SYSTEM_INSTRUCTION}\n\nOvozda aytilgan savolni tushunib, unga batafsil va aniq javob ber."
        ]

        reply_text = await call_gemini(prompt_parts)

        if status_msg:
            try:
                await status_msg.delete()
            except Exception:
                pass

        await safe_send_text(message, reply_text)

    except Exception as e:
        logging.error(f"Ovoz xatosi: {e}")
        if status_msg:
            try:
                await status_msg.edit_text(f"⚠️ Ovoz tahlilida xatolik: {e}")
            except Exception:
                pass
    finally:
        if local_path and local_path.exists():
            try:
                local_path.unlink()
            except Exception:
                pass

@dp.message(F.text)
async def text_handler(message: types.Message):
    """Matnli xabarlar"""
    if message.text.startswith("/"):
        return

    status_msg = None
    try:
        status_msg = await message.answer("🧠 Javob tayyorlanmoqda...")
    except Exception:
        pass

    try:
        prompt = f"{SYSTEM_INSTRUCTION}\n\nFoydalanuvchi savoli:\n{message.text}"
        reply_text = await call_gemini(prompt)

        if status_msg:
            try:
                await status_msg.delete()
            except Exception:
                pass

        await safe_send_text(message, reply_text)

    except Exception as e:
        logging.error(f"Matn xatosi: {e}")
        if status_msg:
            try:
                await status_msg.edit_text(f"⚠️ Xatolik: {e}")
            except Exception:
                pass

async def main():
    logging.info("🚀 Bardoshli, toza Universal AI Bot ishga tushirilmoqda...")
    while True:
        try:
            await bot.delete_webhook(drop_pending_updates=False)
            logging.info("⚡ Polling boshlandi...")
            await dp.start_polling(bot, handle_signals=False)
        except (KeyboardInterrupt, SystemExit):
            logging.info("To'xtatildi.")
            break
        except Exception as e:
            logging.error(f"Bot polling xatosi: {e}. 3 soniyadan keyin qayta ulanadi...")
            await asyncio.sleep(3)

if __name__ == "__main__":
    asyncio.run(main())
