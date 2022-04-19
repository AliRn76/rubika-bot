import requests

data = {
    "chat_id": chat_id,
    "message_id": chat_id
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/deleteMessage'
response = requests.post(url, data=data)

print(response.text)