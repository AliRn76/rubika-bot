## Requirements
<div class="termy">

```console
python 3.10+
```
</div>

<hr/>

## Installation

<div class="termy">

```console
$ pip install rubika-bot
```

<hr/>

## Introduction

You will receive updates in <b>receiveUpdate</b> and <b>receiveInlineMessage</b> urls

- ### receiveUpdate:
    You'll get a request whenever user <b>send text</b> or tap a <b>keypad</b>
  - #### sample request body:
    ```json
    {
        "inline_message": {
            "sender_id": "u0QFtn01dd26d72abc5c77b8e116cd79",
            "text": "custom text",
            "location": null,
            "aux_data": {
                "start_id": null,
                "button_id": "61f674bd0abcd57b5b816a7c"
            },
            "message_id": "204216801381244279",
            "chat_id": "b0QFtabc1I02214b529f1d60c9ce5b08"
        }
    }
    ```
    - <b>sender_id</b> is the unique ID of user
    - <b>text</b> is the text of button
    - <b>button_id</b> is the ID that you set for the button
    - <b>message_id</b> is the unique ID of this message 
    - <b>chat_id</b> is the unique ID of this chat with user <b>(You should use this value when you want to send him back anything)</b>

    
- ### receiveInlineMessage:
    You'll get a request whenever user tap an <b>inline keypad</b>
  - #### sample request body:
      ```json
      {
          "update": {
              "type": "NewMessage",
              "chat_id": "b0QFtn0C1I022abcd29f1d60c9ce5b08",
              "new_message": {
                  "message_id": 204215121115944300,
                  "text": "custom text",
                  "time": "1643122902",
                  "is_edited": false,
                  "sender_type": "User",
                  "sender_id": "u0QFtn0abcded727585c77b8e116cd79",
                  "aux_data": {
                      "start_id": null,
                      "button_id": "61f674bd0abcd57b5b816a7c"
                  }
              }
          }
      }
      ``` 
    - <b>type: </b> can be <b>NewMessage</b>, <b>StartedBot</b>, <b>StoppedBot</b>
    - <b>text</b> is the text of button
    - <b>button_id</b> is the ID that you set for the button
    - <b>message_id</b> is the unique ID of this message 
    - <b>chat_id</b> is the unique ID of this chat with user <b>(You should use this value when you want to send him back anything)</b>

And when you get request, you can use methods below for sending request to bot.
<hr/>

## Usage

- #### Get Your Bot Information

```python
from rubika_bot.requests import get_me
from rubika_bot.schemas import Bot

bot: Bot = get_me(token=...)
```

- #### Send Start Keypad

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

- #### Send Inline Keypad

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

- #### Send Message

```python
from rubika_bot.requests import send_message

send_message(
    token=...,
    chat_id=...,
    text='Hello World',
)
```

- #### Send Poll

```python
from rubika_bot.requests import send_poll

send_poll(
    token=...,
    chat_id=...,
    question='Do you have any question?',
    options=['yes', 'no']
)
```

- #### Send Location

```python
from rubika_bot.requests import send_location

send_location(
    token=...,
    chat_id=...,
    latitude='35.759662741892626',
    longitude='51.4036344416759'
)
```

- #### Send Sticker

```python
from rubika_bot.requests import send_sticker

send_sticker(
    token=...,
    chat_id=...,
    sticker_id=...,
)
```

- #### Send Sticker

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

- #### Get Chat Information

```python
from rubika_bot.requests import get_chat
from rubika_bot.schemas import Chat

chat: Chat = get_chat(
    token=...,
    chat_id=...,
)   
```

- #### Get Last 10 Updates

```python
from rubika_bot.requests import get_updates
from rubika_bot.schemas import Update

updates, _ = get_updates(
    token=...,
    limit=10,
)
```

- #### Forward Message

```python
from rubika_bot.requests import forward_message

forward_message(
    token=...,
    from_chat_id=...,
    message_id=...,
    to_chat_id=...
)
```

- #### Edit Message Text

```python
from rubika_bot.requests import edit_message_text

edit_message_text(
    token=...,
    chat_id=...,
    message_id=...,
    text='New Message Text'
)
```

- #### Edit Inline Keypad

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

- #### Delete Message

```python
from rubika_bot.requests import delete_message

delete_message(
    token=...,
    chat_id=...,
    message_id=...,
)
```

</div>

## TODO:
- [ ] Change the required python version from 3.10 to 3.8