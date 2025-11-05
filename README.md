
# Naver News Alert

NAVER 뉴스 검색 API를 이용해 지정한 키워드(예: 한화손해보험, 한화손보)의 최신 기사를 2분마다 조회하고,
새로운 기사만 텔레그램으로 알림을 보내는 파이썬 프로그램입니다.

## macOS 설치 및 실행
```bash
# 1. 가상환경 생성 및 실행
python3 -m venv .venv
source .venv/bin/activate

# 2. 라이브러리 설치
pip install -r requirements.txt

# 3. .env 파일 작성
cp .env.example .env
open -e .env  # TextEdit으로 열기

# 4. 실행
python3 app.py
```
