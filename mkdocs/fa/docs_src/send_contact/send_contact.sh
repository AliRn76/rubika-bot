curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/getUpdates' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "chat_id": "{chat_id}",
            "first_name": "{first_name}",
            "last_name": "{last_name}",
            "phone_number": "{phone_number}"
        }'