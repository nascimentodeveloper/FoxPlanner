import re

def parse_with_ai(user_message: str):
    # Usar regex para extrair tarefa e hora
    pattern = re.compile(r"(\D+)\s*(\d{1,2}:\d{2})|(\d{1,2}h|\d{1,2}H)\s*(\D+)")
    match = pattern.search(user_message)

    if match:
        if match.group(1) and match.group(2):  # Caso da hora no formato HH:MM
            task = match.group(1).strip().title()
            time_str = match.group(2).strip()
        elif match.group(3) and match.group(4):  # Caso da hora no formato HHh
            task = match.group(4).strip().title()
            time_str = match.group(3).replace('h', ':00').strip()
        return task, time_str
    
    return None, None
