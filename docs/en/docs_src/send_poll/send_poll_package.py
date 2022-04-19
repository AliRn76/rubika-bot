from rubika_bot.requests import send_poll

send_poll(
    token='SUPER_SECRET_TOKEN',
    chat_id='CHAT_ID',
    question='Do you have any question?',
    options=['yes', 'no']
)