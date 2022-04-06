from rubika_bot.requests import send_message
from rubika_bot.models import Keypad, KeypadRow, Button

b1 = Button(id='100', type='Simple', button_text='Add Account')
b2 = Button(id='101', type='Simple', button_text='Edit Account')
b3 = Button(id='102', type='Simple', button_text='Remove Account')
keypad = Keypad(
    rows=[
        KeypadRow(buttons=[b1]),
        KeypadRow(buttons=[b2, b3])
    ],
)
send_message(
    token='SUPER_SECRET_TOKEN',
    chat_id='CHAT_ID',
    text='Welcome',
    inline_keypad=keypad
)
