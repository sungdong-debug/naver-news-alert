
import hashlib, requests
from typing import List, Dict, Any
from settings import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, NAVER_DISPLAY

BASE_URL = "https://openapi.naver.com/v1/search/news.json"
HEADERS = {
    "X-Naver-Client-Id": NAVER_CLIENT_ID,
    "X-Naver-Client-Secret": NAVER_CLIENT_SECRET,
}

def _hash(item: Dict[str, Any]) -> str:
    text = "|".join([
        item.get("originallink",""),
        item.get("link",""),
        item.get("title",""),
        item.get("pubDate","")
    ])
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def search_news(keyword: str) -> List[Dict[str, Any]]:
    params = {"query": keyword, "display": NAVER_DISPLAY, "sort": "date"}
    r = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    items = data.get("items", [])
    result = []
    for it in items:
        result.append({
            "keyword": keyword,
            "title": it.get("title"),
            "originallink": it.get("originallink"),
            "link": it.get("link"),
            "description": it.get("description"),
            "pubDate": it.get("pubDate"),
            "id": _hash(it)
        })
    return result
