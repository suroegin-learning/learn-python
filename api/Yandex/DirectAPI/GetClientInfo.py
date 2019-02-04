import json
import requests

url = 'https://api.direct.yandex.ru/v4/json/'

token = 'AQAAAAASC_cmAARZxEy1CEYO30UktGI_JgXUJU0'

#логин в Директе
login = 'edgard.gomes'

#структура входных данных (словарь)
data = {
   'method': 'GetClientInfo',
   'token': token,
   'locale': 'ru',
   'param': [login]
}

#конвертировать словарь в JSON-формат и перекодировать в UTF-8
jdata = json.dumps(data, ensure_ascii=False).encode('utf8')

#выполнить запрос
response = requests.post(url, data=data)

#вывести результат
print(response.text)
