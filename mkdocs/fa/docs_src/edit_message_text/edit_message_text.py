import requests

data = {
    "chat_id": chat_id,
    "message_id": message_id,
    "text": "this is my new text"
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/editMessageText'
response = requests.post(url, data=data)

print(response.text)
