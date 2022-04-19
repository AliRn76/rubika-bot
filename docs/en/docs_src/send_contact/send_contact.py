import requests

data = {
    "chat_id": chat_id,
    "first_name": first_name,
    "last_name": last_name,
    "phone_number": phone_number,
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/sendContact'
response = requests.post(url, data=data)

print(response.text)
