curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/sendMessage' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "chat_id": "{chat_id}",
            "text": "Welcome",
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
                "resize_keyboard": true,
                "on_time_keyboard": false
            }
        }'