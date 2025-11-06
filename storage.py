import sqlite3
from typing import Dict, Any, Iterable, List

DB_PATH = "data.db"
SCHEMA = '''
CREATE TABLE IF NOT EXISTS seen_articles (
    id TEXT PRIMARY KEY,
    keyword TEXT,
    title TEXT,
    link TEXT,
    originallink TEXT,
    pubDate TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(SCHEMA)
        conn.commit()

def insert_if_new(items: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    new_items: List[Dict[str, Any]] = []
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        for it in items:
            try:
                cur.execute(
                    "INSERT INTO seen_articles (id, keyword, title, link, originallink, pubDate) VALUES (?, ?, ?, ?, ?, ?)",
                    (it["id"], it.get("keyword"), it.get("title"), it.get("link"), it.get("originallink"), it.get("pubDate"))
                )
                new_items.append(it)
            except sqlite3.IntegrityError:
                pass
        conn.commit()
    return new_items
