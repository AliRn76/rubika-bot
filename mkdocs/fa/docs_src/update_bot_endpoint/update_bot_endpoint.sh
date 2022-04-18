curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/updateBotEndpoints' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "url": "https://example.com",
            "type": "GetSelectionItem"
        }'