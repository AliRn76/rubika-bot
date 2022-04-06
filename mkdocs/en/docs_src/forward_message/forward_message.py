import requests

data = {
    "from_chat_id": chat_id,
    "message_id": message_id,
    "to_chat_id": to_chat_id
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/frowardMessage'
response = requests.post(url, data=data)

print(response.text)
