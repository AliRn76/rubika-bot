curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/sendMessage' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "text": "Hello user, this is my text",
            "chat_id": "{chat_id}"
        }'