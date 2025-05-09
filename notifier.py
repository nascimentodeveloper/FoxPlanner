from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)

async def send_reminder(task, chat_id):
    await bot.send_message(chat_id=chat_id, text=f"⏰ Lembrete: *{task}* em 30 minutos!", parse_mode="Markdown")