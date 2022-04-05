import requests

url = 'https://messengerg2b1.iranlms.ir/v3/{token}/getMe'

response = requests.post(url)

print(response.text)