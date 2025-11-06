import logging
import requests
from typing import List, Dict, Any
from settings import SLACK_WEBHOOK_URL, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def notify_slack(items: List[Dict[str, Any]]):
    if not SLACK_WEBHOOK_URL:
        return
    lines = []
    for it in items:
        link = it.get("link") or it.get("originallink") or ""
        title = it.get("title") or ""
        kw = it.get("keyword") or ""
        pub = it.get("pubDate") or ""
        lines.append(f"• [{kw}] {title} ({pub})\n{link}")
    if not lines:
        return
    payload = {"text": "*네이버 뉴스 신규 기사 감지*\n" + "\n".join(lines)}
    try:
        r = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
        r.raise_for_status()
    except Exception as e:
        logging.exception("Slack notify failed: %s", e)

def notify_telegram(items: List[Dict[str, Any]]):
    if not (TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID):
        return
    for it in items:
        link = it.get("link") or it.get("originallink") or ""
        title = it.get("title") or ""
        kw = it.get("keyword") or ""
        pub = it.get("pubDate") or ""
        text = f"[{kw}] {title}\n{pub}\n{link}"
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            r = requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text, "disable_web_page_preview": True}, timeout=10)
            r.raise_for_status()
        except Exception as e:
            logging.exception("Telegram notify failed: %s", e)
