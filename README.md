# 🤖 FoxPlanner – Bot de Lembretes no Telegram

FoxPlanner é um bot do Telegram que entende mensagens como "Reunião 10:30", salva a tarefa e envia um lembrete automático 30 minutos antes do horário agendado. O projeto é um assistente pessoal simples, desenvolvido com Python e a biblioteca `python-telegram-bot`.

> ⚠️ Atenção: O projeto ainda está em fase inicial e possui bugs conhecidos (veja abaixo). Sinta-se à vontade para colaborar!

---

## ✨ Funcionalidades atuais

- ✅ Interpretação de mensagens com tarefas e horários (ex: `"Consulta 14:30"`)
- ✅ Armazenamento local da tarefa com horário associado
- ✅ Envio automático de lembrete 30 minutos antes da tarefa
- ✅ Ajuste automático para o próximo dia, caso o horário enviado já tenha passado

---

## 🧠 Tecnologias utilizadas

- Python 3.10+
- [python-telegram-bot v20+](https://docs.python-telegram-bot.org/)
- dotenv (para variáveis de ambiente)
- JobQueue (agendamento interno do bot)

---

## 🚀 Como rodar o projeto localmente

1. Clone este repositório:
```bash
git clone https://github.com/nascimentodeveloper/foxplanner.git
cd foxplanner
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo .env com seu token do bot:
```bash
TELEGRAM_TOKEN=seu_token_aqui
```

5. Execute o bot:
```bash
python bot.py
```
## 📁 Estrutura do projeto

```bash
foxplanner/
├── bot.py               # Lógica principal do bot
├── parser.py            # Interpreta mensagens para extrair tarefa e horário
├── scheduler.py         # Agenda os lembretes
├── storage.py           # Salva as tarefas (atualmente apenas localmente)
├── .env                 # Token do bot
├── requirements.txt     # Bibliotecas necessárias
```

## 🐞 Bugs e limitações atuais

- O agendamento pode falhar silenciosamente se o horário estiver em formato inesperado
- Tarefas são armazenadas apenas em memória (não persistem após reiniciar)
- Agendamentos para horários muito próximos (ex: 1 minuto depois) não funcionam corretamente
- O bot não responde comandos como /start, /ajuda ou /listar
- Ainda não há controle de múltiplas tarefas por usuário

## 💡 Ideias futuras

- 🔒 Persistência com banco de dados local (SQLite ou Firebase)
- 📆 Comando /listar para ver tarefas agendadas
- 🧹 Comando /limpar para remover tarefas antigas
- ⏱ Permitir configurar lembrete com outros intervalos (ex: 10 min antes)
- 🌍 Suporte a diferentes fusos horários
- ☁️ Hospedagem em nuvem (Railway, Render, etc.)

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você encontrar bugs ou quiser implementar algo novo, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📜 Licença

Este projeto está licenciado sob a MIT License.
