import requests

data = {
    "chat_id": chat_id,
    "question": "Do you have any question?",
    "options": ["yes", "no"],
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/sendPoll'
response = requests.post(url, data=data)

print(response.text)
