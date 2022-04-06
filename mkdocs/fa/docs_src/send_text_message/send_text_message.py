import requests

data = {
    "chat_id": chat_id,
    "text": "Hello user, this is my text",
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/sendMessage'
response = requests.post(url, data=data)

print(response.text)
