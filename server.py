import os, threading, time, logging, schedule
from fastapi import FastAPI
from settings import KEYWORDS, POLL_INTERVAL_MIN, TZ_LABEL
from naver_news import search_news
from storage import init_db, insert_if_new
from notifier import notify_slack, notify_telegram

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok", "tz": TZ_LABEL, "keywords": KEYWORDS, "interval_min": POLL_INTERVAL_MIN}

def job():
    logging.info("Polling... (%s)", TZ_LABEL)
    all_new = []
    for kw in KEYWORDS:
        try:
            items = search_news(kw)
            new_items = insert_if_new(items)
            if new_items:
                logging.info("New articles for '%s': %d", kw, len(new_items))
            all_new.extend(new_items)
        except Exception as e:
            logging.exception("Error while fetching '%s': %s", kw, e)
    if all_new:
        notify_slack(all_new)
        notify_telegram(all_new)

def scheduler_loop():
    init_db()
    job()
    schedule.every(POLL_INTERVAL_MIN).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target=scheduler_loop, daemon=True)
    t.start()
    import uvicorn
    port = int(os.getenv("PORT", "10000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
