import requests
import json
response_API = requests.get('https://fpmir.azurewebsites.net/api/AZFMIR?AZFNUM=Semana4')


data = response_API.text
print(data)

