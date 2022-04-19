from rubika_bot.requests import edit_message_keypad
from rubika_bot.models import Button, Keypad, KeypadRow

b1 = Button(id='100', type='Simple', button_text='Add Account')
b2 = Button(id='101', type='Simple', button_text='Edit Account')
b3 = Button(id='102', type='Simple', button_text='Remove Account')
new_keypad = Keypad(
    rows=[
        KeypadRow(buttons=[b1]),
        KeypadRow(buttons=[b2, b3])
    ],
)

edit_message_keypad(
    token='SUPER_SECRET_TOKEN',
    chat_id='CHAT_ID',
    message_id='MESSAGE_ID',
    inline_keypad=new_keypad
)