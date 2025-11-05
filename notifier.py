
import requests, logging
from typing import List, Dict, Any
from settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def notify_telegram(items: List[Dict[str, Any]]):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        logging.warning("Telegram info missing.")
        return
    for it in items:
        title = it.get("title","")
        link = it.get("link") or it.get("originallink") or ""
        msg = f"📰 [{it['keyword']}] {title}\n{it['pubDate']}\n{link}"
        try:
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "disable_web_page_preview": True},
                timeout=10
            )
        except Exception as e:
            logging.exception("Telegram send failed: %s", e)
