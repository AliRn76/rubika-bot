import requests

data = {
    'url': 'https://example.com',
    'type': 'GetSelectionItem',
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/updateBotEndpoints'
response = requests.post(url, data=data)

print(response.text)
