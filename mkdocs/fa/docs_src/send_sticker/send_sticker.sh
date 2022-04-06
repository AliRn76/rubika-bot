curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/sendSticker' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "chat_id": "{chat_id}",
            "sticker_id": "{sticker_id}"
        }'