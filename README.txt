Render Web Service Fix Pack

Render settings:
- Build Command: pip install -r requirements.txt
- Start Command: python server.py
- Env Vars: NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, KEYWORDS, POLL_INTERVAL_MINUTES

After deploy, open service URL '/'. Logs should show 'Polling...' periodically.
