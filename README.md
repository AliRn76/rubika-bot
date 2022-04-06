Rubika has created APIs for you that you can use to build your own "bot".

## Requirements
```
python3.8 +
```

## Installation
```
$ pip install rubika-bot
```

## Steps of use
- First you have to create a bot for yourself with <b/>Bot Father</b>.
- Hold the token it gives you and use it in the rest of the steps.
- Using your desired method and token, create your URL in the following format and request POST.

```python
https://messengerg2b1.iranlms.ir/v3/{token}/{method}
```

* If you use the `` python`` language, you can also use the [rubika-bot](https://pypi.org/project/rubika-bot/) package.

## Description

After you have built your bot in Bot Father and defined your endpoint, the system will send any event or message sent to your bot to your Endpoint in one of the following two ways.
 
- Endpoint/``receiveUpdate``
- Endpoint/``receiveInlineMessage``

<br/>

### <u>receiveUpdate</u>

Whenever a user <b> sends a message </b> or taps on a <b> keypad </b>, you will receive this type of request.

<br/>
<i>sample body :</i>

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

  - <b> sender_id: </b> Unique identifier assigned to the user.
  - <b> text: </b> The text of the sent button.
  - <b> button_id: </b> The ID you set for the button.
  - <b> message_id: </b> The unique identifier assigned to the message.
  - <b> chat_id: </b> Unique identifier for the conversation between the user and the bot <b> (you must continue to use this identifier.) </b>


<br/>

### <u>receiveInlineMessage</u>
Whenever the user taps on the <b>inline keypad</b>, you receive this type of request.

<br/>
<i>sample body :</i>

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

  - <b> type: </b> can be <b> NewMessage </b>, <b> StartedBot </b>, <b> StoppedBot </b> and ....
  - <b> text: </b> The text of the sent button.
  - <b> button_id: </b> is the identifier you set for the button.
  - <b> message_id: </b> The unique identifier assigned to the message.
  - <b> chat_id: </b> Unique identifier for the conversation between the user and the bot <b> (you must continue to use this identifier.) </b>

## Usage

- #### Get Your Bot Information

```python
from rubika_bot.requests import get_me
from rubika_bot.models import Bot

bot: Bot = get_me(token=...)
```

- #### Send Start Keypad

```python
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
from rubika_bot.models import Chat

chat: Chat = get_chat(
    token=...,
    chat_id=...,
)   
```

- #### Get Last 10 Updates

```python
from rubika_bot.requests import get_updates
from rubika_bot.models import Update

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
- [x] Change the required python version from 3.10 to 3.8 
