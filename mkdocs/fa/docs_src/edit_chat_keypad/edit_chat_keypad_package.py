from rubika_bot.requests import edit_chat_keypad
from rubika_bot.models import Keypad, KeypadRow, Button

b1 = Button(id='100', type='Simple', button_text='Add Account')
b2 = Button(id='101', type='Simple', button_text='Edit Account')
b3 = Button(id='102', type='Simple', button_text='Remove Account')
keypad = Keypad(
    rows=[
        KeypadRow(buttons=[b1]),
        KeypadRow(buttons=[b2, b3])
    ],
    resize_keyboard=True,
    on_time_keyboard=False
)

edit_chat_keypad(token='SUPER_SECRET_TOKEN', chat_id='CHAT_ID', chat_keypad=keypad)
