import json
from urllib.request import urlopen
import requests

# LOGIN = "PG-RU-Baby-Pampers"
LOGIN = "breedermarket-yn-top5zaoruskan"
TOKEN = "AQAAAAASC_cmAARZxEy1CEYO30UktGI_JgXUJU0"
REPORTS_URL = 'https://api.direct.yandex.ru/v4/json/'

headers = {
    "Authorization": "Bearer " + TOKEN,
    "Client-Login": LOGIN,
    "Accept-Language": "ru",
    "precessingMode": "auto"
}

body = {
    # "method": "CreateNewWordstatReport",
    # "method": "get",
    "method": "GetWordstatReportList",
    # "param": {
    #     "Phrases": [
    #         "купить авиабилеты"
    #     ],
    #     "GeoID": [
    #         213
    #     ]
    # },
    "param": 1276225471,
    "token": TOKEN,
    "locale": "ru",
    # "param": ["ClientId"]
}

body = json.dumps(body, ensure_ascii=False).encode("utf-8")

# req = requests.post(reports_url, json.dumps(body, ensure_ascii=False).encode('utf-8'))
# req.encoding = 'utf-8'
# print(req.text)

response = urlopen(REPORTS_URL, body)

print(response.read().decode("utf-8"))
