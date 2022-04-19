curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/deleteMessage' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "chat_id": "{chat_id}",
            "message_id": "{message_id}"
        }'