import requests

data = {
    "chat_id": chat_id,
    "latitude": latitude,
    "longitude": longitude,
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/sendLocation'
response = requests.post(url, data=data)

print(response.text)
