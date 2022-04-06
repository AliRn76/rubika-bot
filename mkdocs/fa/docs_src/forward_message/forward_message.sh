curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/forwardMessage' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "from_chat_id": "{chat_id}",
            "message_id": "{message_id}",
            "to_chat_id": "{to_chat_id}"
        }'