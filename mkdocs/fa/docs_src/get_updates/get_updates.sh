curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/getUpdates' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "limit": "{limit}"
        }'