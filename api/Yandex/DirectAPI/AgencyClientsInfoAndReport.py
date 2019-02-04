import requests
from requests.exceptions import ConnectionError
from time import sleep
import json
from datetime import date, timedelta
from time import time

# Метод для корректной обработки строк в кодировке UTF-8 как в Python 3, так и в Python 2
import sys

if sys.version_info < (3,):
    def u(x):
        try:
            return x.encode("utf8")
        except UnicodeDecodeError:
            return x
else:
    def u(x):
        if isinstance(x, bytes):
            return x.decode('utf8')
        else:
            return x

# --- Входные данные ---
# Адрес сервиса AgencyClients для отправки JSON-запросов (регистрозависимый)
AgencyClientsURL = 'https://api.direct.yandex.com/json/v5/agencyclients'

# OAuth-токен представителя агентства, от имени которого будут выполняться запросы
token = 'AQAAAAASC_cmAARZxEy1CEYO30UktGI_JgXUJU0'

# --- Подготовка запроса к сервису AgencyClients ---
# Создание HTTP-заголовков запроса
headers = {
           # OAuth-токен. Использование слова Bearer обязательно
           "Authorization": "Bearer " + token,
           # Язык ответных сообщений
           "Accept-Language": "ru"
           }

AgencyClientsBody = {
    "method": "get",
    "params": {
        "SelectionCriteria": {
            "Archived": "NO"   # Получить только активных клиентов
        },
        "FieldNames": ["Login"],
        "Page": {
            "Limit": 10000,  # Получить не более 10000 клиентов в ответе сервера
            "Offset": 0
        }
    }
}

HasAllClientLoginsReceived = False
ClientList = []

while not HasAllClientLoginsReceived:
    ClientsResult = requests.post(AgencyClientsURL, json.dumps(AgencyClientsBody), headers=headers).json()
    for Client in ClientsResult['result']['Clients']:
        ClientList.append(Client["Login"])
    if ClientsResult['result'].get("LimitedBy", False):
        AgencyClientsBody['Page']['Offset'] = ClientsResult['result']["LimitedBy"]
    else:
        HasAllClientLoginsReceived = True

print(ClientList)
