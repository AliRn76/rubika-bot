

### Get Your Bot Information
- Input

    | Field        | Type   | Description       |
    |--------------|--------|-------------------|
    | `token`      | `str`  | Token of your bot |

- Output

    | Field  | Type   | Description |
    |--------|--------|-------------|
    | `bot`  | `Bot`  | Bot Object  |

- Example

    ```python
    from rubika_bot.requests import get_me
    from rubika_bot.models import Bot
      
    bot: Bot = get_me(token='SUPER_SECRET_TOKEN')
    ```

### Send Keypad
- Input

    | Field                   | Type            | Description                                     |
    |-------------------------|-----------------|-------------------------------------------------|
    | `token`                 | `str`           | Token of your bot                               |
    | `chat_id`               | `str`           | Unique ID of Chat                               |
    | `text`                  | `str`           | Text of Message                                 |
    | `chat_keypad_type`      | `str`           | can be(None, New, Remove)<br/>default is None   |
    | `chat_keypad`           | `Keypad`        | Bot Object                                      |
    | `disable_notification`  | `bool`          | Default is False                                |
    | `reply_to_message_id`   | `Optional[str]` | ID of Message                                   |

- Output

    | Field         | Type   | Description              |
    |---------------|--------|--------------------------|
    | `message_id`  | `str`  | New unique ID of message |

- Example
 
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
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        text='Welcome',
        chat_keypad_type='New',
        chat_keypad=keypad
    )
    ```

### Send Inline Keypad
- Input

    | Field                   | Type             | Description        |
    |-------------------------|------------------|--------------------|
    | `token`                 | `str`            | Token of your bot  |
    | `chat_id`               | `str`            | Unique ID of Chat  |
    | `text`                  | `str`            | Text of Message    |
    | `disable_notification`  | `bool`           | Default is False   |
    | `reply_to_message_id`   | `Optional[str]`  | ID of Message      |
    | `inline_keypad`         | `Keypad`         | ...                |

- Output

    | Field         | Type   | Description              |
    |---------------|--------|--------------------------|
    | `message_id`  | `str`  | New unique ID of message |

- Example

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
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        text='Welcome',
        inline_keypad=keypad
    )
    ```

### Send Message
- Input

    | Field                   | Type             | Description       |
    |-------------------------|------------------|-------------------|
    | `token`                 | `str`            | Token of your bot |
    | `chat_id`               | `str`            | Unique ID of Chat |
    | `text`                  | `str`            | Text of Message   |
    | `disable_notification`  | `bool`           | Default is False  |
    | `reply_to_message_id`   | `Optional[str]`  | ID of Message     |

- Output

    | Field         | Type   | Description              |
    |---------------|--------|--------------------------|
    | `message_id`  | `str`  | New unique ID of message |

- Example

    ```python
    from rubika_bot.requests import send_message
    
    send_message(
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        text='Hello World',
    )
    ```

### Send Poll
- Input

    | Field      | Type         | Description          |
    |------------|--------------|----------------------|
    | `token`    | `str`        | Token of your bot    |
    | `chat_id`  | `str`        | Unique ID of Chat    |
    | `question` | `str`        | Text of Question     |
    | `options`  | `list[str]`  | Options of Question  |

- Output

    | Field        | Type   | Description              |
    |--------------|--------|--------------------------|
    | `message_id` | `str`  | New unique ID of Message |

- Example

    ```python
    from rubika_bot.requests import send_poll
    
    send_poll(
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        question='Do you have any question?',
        options=['yes', 'no']
    )
    ```

### Send Location

- Example

    ```python
    from rubika_bot.requests import send_location
    
    send_location(
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        latitude='35.759662741892626',
        longitude='51.4036344416759'
    )
    ```

### Send Sticker

- Example

    ```python
    from rubika_bot.requests import send_sticker
    
    send_sticker(
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        sticker_id='STICKER_ID',
    )
    ```

### Send Sticker

- Example

    ```python
    from rubika_bot.requests import send_contact
    
    send_contact(
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        first_name='Ali',
        last_name='Rn',
        phone_number='09038754321'
    )
    ```

### Get Chat Information

- Example

    ```python
    from rubika_bot.requests import get_chat
    from rubika_bot.models import Chat
    
    chat: Chat = get_chat(
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
    )   
    ```

### Get Last 10 Updates

- Example 

    ```python
    from rubika_bot.requests import get_updates
    from rubika_bot.models import Update
    
    updates, _ = get_updates(
        token='SUPER_SECRET_TOKEN',
        limit=10,
    )
    ```

### Forward Message

- Example

    ```python
    from rubika_bot.requests import forward_message
    
    forward_message(
        token='SUPER_SECRET_TOKEN',
        from_chat_id='FIRST_CHAT_ID',
        message_id='MESSAGE_ID',
        to_chat_id='SECOND_CHAT_ID'
    )
    ```

### Edit Message Text

- Example

    ```python
    from rubika_bot.requests import edit_message_text
    
    edit_message_text(
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        message_id='MESSAGE_ID',
        text='New Message Text'
    )
    ```

### Edit Inline Keypad

- Example

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
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        message_id='MESSAGE_ID',
        inline_keypad=new_keypad
    )
    ```

### Delete Message

- Example

    ```python
    from rubika_bot.requests import delete_message
    
    delete_message(
        token='SUPER_SECRET_TOKEN',
        chat_id='CHAT_ID',
        message_id='MESSAGE_ID',
    )
    ```
