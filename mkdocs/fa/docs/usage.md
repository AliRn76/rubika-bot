

- #### دریافت اطلاعات ربات


```python
from rubika_bot.requests import get_me
from rubika_bot.schemas import Bot

bot: Bot = get_me(token=...)
```

- #### ارسال Keypad اولیه 

```python
from rubika_bot.requests import send_message
from rubika_bot.schemas import Keypad, KeypadRow, Button

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
send_message(
    token=...,
    chat_id=...,
    text='Welcome',
    chat_keypad_type='New',
    chat_keypad=keypad
)
```

- #### ارسال Inline Keypad 

```python
from rubika_bot.requests import send_message
from rubika_bot.schemas import Keypad, KeypadRow, Button

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
    token=...,
    chat_id=...,
    text='Welcome',
    inline_keypad=keypad
)
```

- #### ارسال پیام 

```python
from rubika_bot.requests import send_message

send_message(
    token=...,
    chat_id=...,
    text='Hello World',
)
```

- #### ارسال نظرسنجی 

```python
from rubika_bot.requests import send_poll

send_poll(
    token=...,
    chat_id=...,
    question='Do you have any question?',
    options=['yes', 'no']
)
```

- #### ارسال موقعیت مکانی 

```python
from rubika_bot.requests import send_location

send_location(
    token=...,
    chat_id=...,
    latitude='35.759662741892626',
    longitude='51.4036344416759'
)
```

- #### ارسال استیکر 

```python
from rubika_bot.requests import send_sticker

send_sticker(
    token=...,
    chat_id=...,
    sticker_id=...,
)
```

- #### ارسال مخاطب 

```python
from rubika_bot.requests import send_contact

send_contact(
    token=...,
    chat_id=...,
    first_name='Ali',
    last_name='Rn',
    phone_number='09038754321'
)
```

- #### دریافت اطلاعات یک مکالمه 

```python
from rubika_bot.requests import get_chat
from rubika_bot.schemas import Chat

chat: Chat = get_chat(
    token=...,
    chat_id=...,
)   
```

- #### دریافت آخرین ۱۰ آپدیت 

```python
from rubika_bot.requests import get_updates
from rubika_bot.schemas import Update

updates, _ = get_updates(
    token=...,
    limit=10,
)
```

- #### فوروارد کردن پیام 

```python
from rubika_bot.requests import forward_message

forward_message(
    token=...,
    from_chat_id=...,
    message_id=...,
    to_chat_id=...
)
```

- #### ویرایش متن پیام 

```python
from rubika_bot.requests import edit_message_text

edit_message_text(
    token=...,
    chat_id=...,
    message_id=...,
    text='New Message Text'
)
```

- #### ویرایش Inline Keypad 

```python
from rubika_bot.requests import edit_message_keypad
from rubika_bot.schemas import Button, Keypad, KeypadRow

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
    token=...,
    chat_id=...,
    message_id=...,
    inline_keypad=new_keypad
)
```

- #### حذف پیام 

```python
from rubika_bot.requests import delete_message

delete_message(
    token=...,
    chat_id=...,
    message_id=...,
)
```
