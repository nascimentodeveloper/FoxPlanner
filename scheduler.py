from datetime import datetime, timedelta

def schedule_task(task, time_str, chat_id, context):
    try:
        now = datetime.now()
        hour, minute = map(int, time_str.split(":"))
        task_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        if task_time <= now:
            task_time += timedelta(days=1)  # Agenda para o próximo dia

        reminder_time = task_time - timedelta(minutes=30)
        if reminder_time <= now:
            return False  # Já passou o tempo de lembrar

        delay = (reminder_time - now).total_seconds()

        print("📌 Debug do agendamento:")
        print(f"  Tarefa: {task}")
        print(f"  Hora original: {time_str}")
        print(f"  Hora para lembrar: {reminder_time.strftime('%H:%M')}")
        print(f"  Chat ID: {chat_id}")
        print(f"  Delay em segundos: {delay}")

        context.job_queue.run_once(
            send_reminder,
            when=delay,
            data={'chat_id': chat_id, 'task': task},
            name=f"reminder_{chat_id}_{time_str}"
        )

        return True

    except Exception as e:
        print("⚠️ Erro no agendamento:", e)
        return False

async def send_reminder(context):
    job_data = context.job.data
    chat_id = job_data['chat_id']
    task = job_data['task']
    await context.bot.send_message(chat_id=chat_id, text=f"⏰ Lembrete: *{task}* em 30 minutos!", parse_mode="Markdown")
