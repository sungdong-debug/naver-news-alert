import hashlib
from typing import List, Dict, Any
import requests
from settings import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, NAVER_DISPLAY

BASE_URL = "https://openapi.naver.com/v1/search/news.json"
HEADERS = {"X-Naver-Client-Id": NAVER_CLIENT_ID, "X-Naver-Client-Secret": NAVER_CLIENT_SECRET}

def _hash_item(item: Dict[str, Any]) -> str:
    src = "|".join([item.get("originallink") or "", item.get("link") or "", item.get("title") or "", item.get("pubDate") or ""])
    return hashlib.sha256(src.encode("utf-8")).hexdigest()

def search_news(keyword: str, start: int = 1) -> List[Dict[str, Any]]:
    params = {"query": keyword, "display": NAVER_DISPLAY, "start": start, "sort": "date"}
    r = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    items = data.get("items", [])
    cleaned = []
    for it in items:
        cleaned.append({
            "keyword": keyword,
            "title": it.get("title"),
            "originallink": it.get("originallink"),
            "link": it.get("link"),
            "description": it.get("description"),
            "pubDate": it.get("pubDate"),
            "id": _hash_item(it),
        })
    return cleaned
