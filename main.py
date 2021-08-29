import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response_1 = requests.get(url)
data = json.loads(response_1.text)
print(data)