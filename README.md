# Dockerizing sample app

## Configuration
Python : 3.8.10
DB : mysql
Redis


## How to Run
```
pip install -r requirements.txt
pytest ./tests
uvicorn app.main:app --reload
```

## API Doc
서버 실행시킨 후 http://127.0.0.1:8000/docs 를 통해 확인 할 수 있습니다.

### POST /log
로그를 추가합니다
```
curl -X 'POST' \
  'http://127.0.0.1:8000/log' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "log_level": "info",
  "log_msg": "info message"
}'
```


## level1 python application docker packaging
- python 3.8 docker image를 사용해 application을 빌드 해주고 포트를 9000번 으로 열어주세요
