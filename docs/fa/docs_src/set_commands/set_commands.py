import requests

data = {
    "bot_commands": [
        {
            "command": "command1",
            "description": "description1"
        },
        {
            "command": "command2",
            "description": "description2"
        },
    ]
}
url = f'https://messengerg2b1.iranlms.ir/v3/{token}/setCommands'
response = requests.post(url, data=data)

print(response.text)
