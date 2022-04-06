import requests

data = {
    "chat_id": chat_id,
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/getChat'
response = requests.post(url, data=data)

print(response.text)
