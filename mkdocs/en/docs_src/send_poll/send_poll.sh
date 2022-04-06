curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/sendPoll' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "chat_id": "{chat_id}",
            "question": "Do you have any question?",
            "options": ["yes", "no"]
        }'