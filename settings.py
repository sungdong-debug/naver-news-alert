import os
from dotenv import load_dotenv
load_dotenv()
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID", "")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET", "")
KEYWORDS = [k.strip() for k in os.getenv("KEYWORDS", "한화손해보험,한화손보").split(",") if k.strip()]
POLL_INTERVAL_MIN = int(os.getenv("POLL_INTERVAL_MINUTES", "2"))
TZ_LABEL = os.getenv("TZ_LABEL", "Asia/Seoul")
NAVER_DISPLAY = max(1, min(int(os.getenv("NAVER_DISPLAY", "20")), 100))
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "").strip()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()
