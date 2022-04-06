import requests
import json

url = f"https://messengerg2b1.iranlms.ir/v3/{token}/sendMessage"

data = {
    "chat_id": chat_id,
    "text": "Welcome",
    "inline_keypad": {
        "rows": [
            {
                "buttons": [
                    {
                        "id": "100",
                        "type": "Simple",
                        "button_text": "Add Account"
                    }
                ]
            },
            {
                "buttons": [
                    {
                        "id": "101",
                        "type": "Simple",
                        "button_text": "Edit Account"
                    },
                    {
                        "id": "102",
                        "type": "Simple",
                        "button_text": "Remove Account"
                    }
                ]
            }
        ]
    }
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=data)

print(response.text)
