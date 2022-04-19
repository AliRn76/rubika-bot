import requests

url = f"https://messengerg2b1.iranlms.ir/v3/{token}/editChatKeypad"

data = {
    "chat_id": chat_id,
    "chat_keypad_type": "New",
    "chat_keypad": {
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
        ],
        "resize_keyboard": True,
        "on_time_keyboard": False
    }
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=data)

print(response.text)
