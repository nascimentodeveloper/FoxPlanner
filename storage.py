import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_task(task, time_str, chat_id):
    tasks = load_tasks()
    tasks[chat_id] = tasks.get(chat_id, [])
    tasks[chat_id].append({"task": task, "time": time_str})
    
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
