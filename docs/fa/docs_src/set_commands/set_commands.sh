curl --location -g --request POST 'https://messengerg2b1.iranlms.ir/v3/{{token}}/setCommands' \
        --header 'Content-Type: application/json' \
        --data-raw '{
            "bot_commands": [
                {
                    "command": "command1",
                    "description": "description1"
                },
                {
                    "command": "command2",
                    "description": "description2"
                },
            ]
        }'