
import time, logging, schedule
from naver_news import search_news
from storage import init_db, insert_if_new
from notifier import notify_telegram
from settings import KEYWORDS, POLL_INTERVAL_MIN

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

def job():
    logging.info("Polling news...")
    all_new = []
    for kw in KEYWORDS:
        try:
            items = search_news(kw)
            new = insert_if_new(items)
            if new:
                logging.info("New articles for %s: %d", kw, len(new))
                all_new.extend(new)
        except Exception as e:
            logging.exception("Error fetching %s: %s", kw, e)
    if all_new:
        notify_telegram(all_new)

def main():
    init_db()
    job()
    schedule.every(POLL_INTERVAL_MIN).minutes.do(job)
    logging.info("Started. Interval=%d min, keywords=%s", POLL_INTERVAL_MIN, ", ".join(KEYWORDS))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
