curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/editChatKeypad' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "chat_id": "{chat_id}",
            "chat_keypad_type": "Removed"
        }'