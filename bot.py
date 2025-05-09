import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters,
)
from datetime import datetime, timedelta

from parser import parse_with_ai
from storage import save_task
from scheduler import schedule_task  # Atualizado para aceitar context

load_dotenv(".env")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Mensagens recebidas
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.message.chat_id

    task, time_str = parse_with_ai(user_message)
    if not task:
        await update.message.reply_text("❌ Não consegui entender. Tente algo como 'Reunião 10:30'.")
        return

    save_task(task, time_str, chat_id)

    # Convertendo hora de string para datetime
    try:
        time_obj = datetime.strptime(time_str, "%H:%M")
        current_time = datetime.now()

        # Ajustando o time_obj para o mesmo dia do current_time
        time_obj = time_obj.replace(year=current_time.year, month=current_time.month, day=current_time.day)

        if time_obj < current_time:
            # Se o horário já passou hoje, agendamos para amanhã
            time_obj += timedelta(days=1)
            await update.message.reply_text("⚠️ O horário já passou hoje, mas será agendado para amanhã.")

        # Agendar para 30 minutos antes
        reminder_time = time_obj - timedelta(minutes=30)

        agendamento_ok = schedule_task(task, time_str, chat_id, context)

        if agendamento_ok:
            await update.message.reply_text(
                f"✅ Tarefa *{task}* salva para {time_str}. Você será avisado 30 minutos antes!",
                parse_mode="Markdown"
            )
        else:
            await update.message.reply_text("⚠️ Algo deu errado ao tentar agendar sua tarefa.")

    except ValueError:
        await update.message.reply_text("❌ Não consegui entender o horário. Tente novamente.")

# Inicializa o bot
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    app.run_polling()
