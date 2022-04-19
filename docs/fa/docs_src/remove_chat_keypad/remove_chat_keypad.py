import requests

data = {
    "chat_id": chat_id,
    "chat_keypad_type": "Removed",
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/editChatKeypad'
response = requests.post(url, data=data)

print(response.text)
