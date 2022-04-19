curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/editMessageText' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "chat_id": "{chat_id}",
            "message_id": "{message_id}",
            "text": "this is my new text"
        }'