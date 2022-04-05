from rubika_bot.requests import forward_message

forward_message(
    token='SUPER_SECRET_TOKEN',
    from_chat_id='FIRST_CHAT_ID',
    message_id='MESSAGE_ID',
    to_chat_id='SECOND_CHAT_ID'
)