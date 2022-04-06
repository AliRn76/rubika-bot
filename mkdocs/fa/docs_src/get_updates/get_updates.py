import requests

data = {
    "limit": limit,
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/getUpdates'
response = requests.post(url, data=data)

print(response.text)
