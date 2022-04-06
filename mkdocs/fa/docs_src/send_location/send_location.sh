curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/sendLocation' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "chat_id": "{chat_id}",
            "latitude": "{latitude}",
            "longitude": "{longitude}"
        }'