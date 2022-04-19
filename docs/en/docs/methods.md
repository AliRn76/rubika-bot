
## Get Bot Information
- Method: ``getMe``
- Input

| Field    | Type    | Description |
|----------|---------|-------------|
| `token`  | `str`   | Token       |

- Output

| Field  | Type                     | Description |
|--------|--------------------------|-------------|
| `bot`  | [`Bot`](../models/#bot)  | Bot         |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_me/get_me.sh!}
        ```
        </div>
  
    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_me/get_me.py!}
        ```
        </div>

    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_me/get_me_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/get_me/get_me_node.js!}
        ```
        </div>


## Send Message (Text, Keypad, InlineKeypad)
- Method: ``sendMessage``
- Input

| Field                  | Type                                                  | Description                               |
|------------------------|-------------------------------------------------------|-------------------------------------------|
| `token`                | `str`                                                 | Token                                     |
| `chat_id`              | `str`                                                 | Chat ID                                   |
| `text`                 | `str`                                                 | Message Text                              |
| `chat_keypad`          | `Keypad`                                              | keypad                                    |
| `disable_notification` | `bool`                                                | Disable Notification?  (Default is false) |
| `inline_keypad`        | `Keypad`                                              | Keypad                                    |
| `reply_to_message_id`  | `Optional[str]`                                       | Replying On?                              |
| `chat_keypad_type`     | [`ChatKeypadTypeEnum`](../models/#chatkeypadtypeenum) | Keypad Type                               |

- Output

| Field         | Type   | Description |
|---------------|--------|-------------|
| `message_id`  | `str`  | Message ID  |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_message/send_message.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_message/send_message.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_message/send_message_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/send_message/send_message_node.js!}
        ```
        </div>


## Send Keypad
- Method: ``sendMessage``
- Input

| Field                  | Type                                                  | Description                               |
|------------------------|-------------------------------------------------------|-------------------------------------------|
| `token`                | `str`                                                 | Token                                     |
| `chat_id`              | `str`                                                 | Chat ID                                   |
| `text`                 | `str`                                                 | Message Text                              |
| `chat_keypad_type`     | [`ChatKeypadTypeEnum`](../models/#chatkeypadtypeenum) | Keypad Type                               |
| `chat_keypad`          | `Keypad`                                              | Keypad                                    |
| `disable_notification` | `bool`                                                | Disable Notification?  (Default is false) |
| `reply_to_message_id`  | `Optional[str]`                                       | Replying On?                              |

- Output

| Field         | Type   | Description  |
|---------------|--------|--------------|
| `message_id`  | `str`  | Message ID   |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_keypad/send_keypad.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_keypad/send_keypad.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_keypad/send_keypad_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/send_keypad/send_keypad_node.js!}
        ```
        </div>


## Send Text Message
- Method: ``sendMessage``
- Input

| Field                  | Type            | Description                               |
|------------------------|-----------------|-------------------------------------------|
| `token`                | `str`           | Token                                     |
| `chat_id`              | `str`           | Chat ID                                   |
| `text`                 | `str`           | Message Text                              |
| `disable_notification` | `bool`          | Disable Notification?  (Default is false) |
| `reply_to_message_id`  | `Optional[str]` | Replying On?                              |

- Output

| Field        | Type   | Description |
|--------------|--------|-------------|
| `message_id` | `str`  | Message ID  |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_text_message/send_text_message.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_text_message/send_text_message.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_text_message/send_text_message_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/send_text_message/send_text_message_node.js!}
        ```
        </div>


## Send Poll
- Method: ``sendPoll``
- Input

| Field      | Type        | Description       |
|------------|-------------|-------------------|
| `token`    | `str`       | Token             |
| `chat_id`  | `str`       | Chat ID           |
| `question` | `str`       | Question Text     |
| `options`  | `list[str]` | Question Options  |

- Output

| Field         | Type   | Description |
|---------------|--------|-------------|
| `message_id`  | `str`  | Message ID  |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_poll/send_poll.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_poll/send_poll.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_poll/send_poll_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/send_poll/send_poll_node.js!}
        ```
        </div>


## Send Location
- Method: ``sendLocation``
- Input

| Field                  | Type                                    | Description                               |
|------------------------|-----------------------------------------|-------------------------------------------|
| `token`                | `str`                                   | Token                                     |
| `chat_id`              | `str`                                   | Chat ID                                   |
| `latitude`             | `str`                                   | Latitude                                  |
| `longitude`            | `str`                                   | Longitude                                 |
| `chat_keypad`          | `str`                                   | Keypad                                    |
| `disable_notification` | `str`                                   | Disable Notification?  (Default is false) |
| `inline_keypad`        | [`Optional[Keypad]`](../models/#keypad) | Keypad                                    |
| `reply_to_message_id`  | `str`                                   | Replying On?                              |
| `chat_keypad_type`     | `str`                                   | Keypad Type                               |

- Output

| Field         | Type   | Description |
|---------------|--------|-------------|
| `message_id`  | `str`  | Message ID  |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_location/send_location.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_location/send_location.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_location/send_location_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/send_location/send_location_node.js!}
        ```
        </div>


## Send Sticker 
- Method: ``sendSticker``
- Input

| Field                  | Type                                    | Description                               |
|------------------------|-----------------------------------------|-------------------------------------------|
| `token`                | `str`                                   | Token                                     |
| `chat_id`              | `str`                                   | Chat ID                                   |
| `sticker_id`           | `str`                                   | Sticker ID                                |
| `chat_keypad`          | `str`                                   | Keypad                                    |
| `disable_notification` | `str`                                   | Disable Notification?  (Default is false) |
| `inline_keypad`        | [`Optional[Keypad]`](../models/#keypad) | keypad                                    |
| `reply_to_message_id`  | `str`                                   | Replying On?                              |
| `chat_keypad_type`     | `str`                                   | Keypad Type                               |

- Output

| Field        | Type   | Description  |
|--------------|--------|--------------|
| `message_id` | `str`  | Message ID   |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_sticker/send_sticker.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_sticker/send_sticker.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_sticker/send_sticker_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/send_sticker/send_sticker_node.js!}
        ```
        </div>


## Send Contact 
- Method: ``sendContact``
- Input

| Field                  | Type                                    | Description                               |
|------------------------|-----------------------------------------|-------------------------------------------|
| `token`                | `str`                                   | Token                                     |
| `chat_id`              | `str`                                   | Chat ID                                   |
| `first_name`           | `str`                                   | Contact Name                              |
| `last_name`            | `str`                                   | Contact Last Name                         |
| `phone_number`         | `str`                                   | Contact Number                            |
| `chat_keypad`          | `str`                                   | Keypad                                    |
| `disable_notification` | `str`                                   | Disable Notification?  (Default is false) |
| `inline_keypad`        | [`Optional[Keypad]`](../models/#keypad) | Keypad                                    |
| `reply_to_message_id`  | `str`                                   | Replying On?                              |
| `chat_keypad_type`     | `str`                                   | Keypad Type                               |

- Output

| Field        | Type    | Description  |
|--------------|---------|--------------|
| `message_id` | `str`   | Message ID   |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_contact/send_contact.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_contact/send_contact.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/send_contact/send_contact_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/send_contact/send_contact_node.js!}
        ```
        </div>


## Get Chat  
- Method: ``getChat``
- Input

| Field      | Type    | Description |
|------------|---------|-------------|
| `token`    | `str`   | Token       |
| `chat_id`  | `str`   | Chat ID     |

- Output

| Field  | Type                      | Description |
|--------|---------------------------|-------------|
| `chat` | [`Chat`](../models/#chat) | Chat        |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_chat/get_chat.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_chat/get_chat.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_chat/get_chat_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/get_chat/get_chat_node.js!}
        ```
        </div>


## Get Updates 
- Method: ``getUpdates``
- Input

| Field       | Type   | Description |
|-------------|--------|-------------|
| `token`     | `str`  | Token       |
| `offset_id` | `str`  | ...         |
| `limit`     | `int`  | ...         |

- Output

| Field     | Type                                | Description      |
|-----------|-------------------------------------|------------------|
| `updates` | [`list[Update]`](../models/#update) | Array Of Updates |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_updates/get_updates.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_updates/get_updates.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_updates/get_updates_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/get_updates/get_updates_node.js!}
        ```
        </div>


## Forward Message 
- Method: ``forwardMessage``
- Input

| Field                  | Type   | Description                               |
|------------------------|--------|-------------------------------------------|
| `token`                | `str`  | Token                                     |
| `from_chat_id`         | `str`  | Forward From?                             |
| `message_id`           | `str`  | Message ID                                |
| `to_chat_id`           | `str`  | Forward To?                               |
| `disable_notification` | `bool` | Disable Notification?  (Default is false) |

- Output

| Field            | Type  | Description  |
|------------------|-------|--------------|
| `new_message_id` | `str` | Message ID   |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/forward_message/forward_message.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/forward_message/forward_message.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/forward_message/forward_message_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/forward_message/forward_message_node.js!}
        ```
        </div>


## Edit Message Text 
- Method: ``editMessageText``
- Input

| Field        | Type  | Description |
|--------------|-------|-------------|
| `token`      | `str` | Token       |
| `chat_id`    | `str` | Chat ID     |
| `message_id` | `str` | Message ID  |
| `text`       | `str` | Text        |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_message_text/edit_message_text.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_message_text/edit_message_text.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_message_text/edit_message_text_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/edit_message_text/edit_message_text_node.js!}
        ```
        </div>


## Edit Inline Keypad 
- Method: ``editMessageKeypad``
- Input

| Field        | Type  | Description  |
|--------------|-------|--------------|
| `token`      | `str` | Token        |
| `chat_id`    | `str` | Chat ID      |
| `message_id` | `str` | Message ID   |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_inline_keypad/edit_inline_keypad.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_inline_keypad/edit_inline_keypad.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_inline_keypad/edit_inline_keypad_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/edit_inline_keypad/edit_inline_keypad_node.js!}
        ```
        </div>

## Delete Message 

- Input

| Field        | Type   | Description  |
|--------------|--------|--------------|
| `token`      | `str`  | Token        |
| `chat_id`    | `str`  | Chat ID      |
| `message_id` | `str`  | Message ID   |

- Example

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/delete_message/delete_message.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/delete_message/delete_message.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/delete_message/delete_message_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/delete_message/delete_message_node.js!}
        ```
        </div>

