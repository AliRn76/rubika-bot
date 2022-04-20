
## گرفتن اطلاعات بات
- متد: ``getMe``
- ورودی

| فیلد     | نوع    | توضیحات |
|----------|--------|---------|
| `token`  | `str`  | توکن    |

- خروجی

| فیلد   | نوع                     | توضیحات |
|--------|-------------------------|---------|
| `bot`  | [`Bot`](../models/#bot) | بات     |

- مثال

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


## ارسال پیام (Text, Keypad, InlineKeypad)
- متد: ``sendMessage``
- ورودی

| فیلد                    | نوع                                                    | توضیحات                             |
|-------------------------|--------------------------------------------------------|-------------------------------------|
| `token`                 | `str`                                                  | توکن                                |
| `chat_id`               | `str`                                                  | شناسه‌ی چت                          |
| `text`                  | `str`                                                  | متن پیام                            |
| `chat_keypad`           | `Keypad`                                               | keypad                              |
| `disable_notification`  | `bool`                                                 | غیرفعال کردن اعلان؟  (پیشفرض false) |
| `inline_keypad`         | `Keypad`                                               | keypad                              |
| `reply_to_message_id`   | `Optional[str]`                                        | در جوابِ پیامِ؟                     |
| `chat_keypad_type`      | [`ChatKeypadTypeEnum`](../models/#chatkeypadtypeenum)  | نوع keypad                          |

- خروجی

| فیلد          | نوع    | توضیحات    |
|---------------|--------|------------|
| `message_id`  | `str`  | شناسه پیام |

- مثال

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


## ارسال keypad
- متد: ``sendMessage``
- ورودی

| فیلد                   | نوع                                                   | توضیحات                             |
|------------------------|-------------------------------------------------------|-------------------------------------|
| `token`                | `str`                                                 | توکن                                |
| `chat_id`              | `str`                                                 | شناسه‌ی چت                          |
| `text`                 | `str`                                                 | متن پیام                            |
| `chat_keypad_type`     | [`ChatKeypadTypeEnum`](../models/#chatkeypadtypeenum) | نوع keypad                          |
| `chat_keypad`          | `Keypad`                                              | keypad                              |
| `disable_notification` | `bool`                                                | غیرفعال کردن اعلان؟  (پیشفرض false) |
| `reply_to_message_id`  | `Optional[str]`                                       | در جوابِ پیامِ؟                     |

- خروجی

| فیلد           | نوع    | توضیحات    |
|----------------|--------|------------|
| `message_id`   | `str`  | شناسه پیام |

- مثال

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


## ارسال پیام متنی
- متد: ``sendMessage``
- ورودی

| فیلد                   | نوع              | توضیحات                             |
|------------------------|------------------|-------------------------------------|
| `token`                | `str`            | توکن                                |
| `chat_id`              | `str`            | شناسه‌ی چت                          |
| `text`                 | `str`            | متن پیام                            |
| `disable_notification` | `bool`           | غیرفعال کردن اعلان؟  (پیشفرض false) |
| `reply_to_message_id`  | `Optional[str]`  |  در جوابِ پیامِ؟                    |

- خروجی

| فیلد          | نوع    |  توضیحات     |
|---------------|--------|--------------|
| `message_id`  | `str`  | شناسه‌ی پیام |

- مثال

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


## ارسال نظرسنجی
- متد: ``sendPoll``
- ورودی

| فیلد       | نوع         | توضیحات        |
|------------|-------------|----------------|
| `token`    | `str`       | توکن           |
| `chat_id`  | `str`       | شناسه‌ی چت     |
| `question` | `str`       | متن سوال       |
| `options`  | `list[str]` | گزینه‌های سوال |

- خروجی

| فیلد         | نوع   | توضیحات      |
|--------------|-------|--------------|
| `message_id` | `str` | شناسه‌ی پیام |

- مثال

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


## ارسال موقعیت مکانی
- متد: ``sendLocation``
- ورودی

| فیلد                   | نوع                                     | توضیحات                             |
|------------------------|-----------------------------------------|-------------------------------------|
| `token`                | `str`                                   | توکن                                |
| `chat_id`              | `str`                                   | شناسه‌ی چت                          |
| `latitude`             | `str`                                   | عرض جغرافیایی                       |
| `longitude`            | `str`                                   | طول جغرافیایی                       |
| `chat_keypad`          | `str`                                   | keypad                              |
| `disable_notification` | `str`                                   | غیرفعال کردن اعلان؟  (پیشفرض false) |
| `inline_keypad`        | [`Optional[Keypad]`](../models/#keypad) | Keypad                              |
| `reply_to_message_id`  | `str`                                   | در جوابِ پیامِ؟                     |
| `chat_keypad_type`     | `str`                                   | نوع keypad                          |

- خروجی

| فیلد         | نوع   | توضیحات      |
|--------------|-------|--------------|
| `message_id` | `str` | شناسه‌ی پیام |

- مثال

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


## ارسال مخاطب 
- متد: ``sendContact``
- ورودی

| فیلد                   | نوع                                     | توضیحات                             |
|------------------------|-----------------------------------------|-------------------------------------|
| `token`                | `str`                                   | توکن                                |
| `chat_id`              | `str`                                   | شناسه‌ی چت                          |
| `first_name`           | `str`                                   | نام مخاطب                           |
| `last_name`            | `str`                                   | نام‌خانوادگی مخاطب                  |
| `phone_number`         | `str`                                   | شماره مخاطب                         |
| `chat_keypad`          | `str`                                   | keypad                              |
| `disable_notification` | `str`                                   | غیرفعال کردن اعلان؟  (پیشفرض false) |
| `inline_keypad`        | [`Optional[Keypad]`](../models/#keypad) | keypad                              |
| `reply_to_message_id`  | `str`                                   | در جوابِ پیامِ؟                     |
| `chat_keypad_type`     | `str`                                   | نوع keypad                          |

- خروجی

| فیلد          | نوع    |  توضیحات     |
|---------------|--------|--------------|
| `message_id`  | `str`  | شناسه‌ی پیام |

- مثال

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


## گرفتن اطلاعات چت 
- متد: ``getChat``
- ورودی

| فیلد                   | نوع                                     | توضیحات                             |
|------------------------|-----------------------------------------|-------------------------------------|
| `token`                | `str`                                   | توکن                                |
| `chat_id`              | `str`                                   | شناسه‌ی چت                          |

- خروجی

| فیلد   | نوع                       | توضیحات |
|--------|---------------------------|---------|
| `chat` | [`Chat`](../models/#chat) | چت      |

- مثال

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


## گرفتن آخرین آپدیت‌ها 
- متد: ``getUpdates``
- ورودی

| فیلد         | نوع    | توضیحات |
|--------------|--------|---------|
| `token`      | `str`  | توکن    |
| `offset_id`  | `str`  | ...     |
| `limit`      | `int`  | ...     |

- خروجی

| فیلد      | نوع                                 | توضیحات              |
|-----------|-------------------------------------|----------------------|
| `updates` | [`list[Update]`](../models/#update) | آرایه‌ای از آپدیت ها |

- مثال

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


## فوروارد کردن پیام 
- متد: ``forwardMessage``
- ورودی

| فیلد                   | نوع    | توضیحات                             |
|------------------------|--------|-------------------------------------|
| `token`                | `str`  | توکن                                |
| `from_chat_id`         | `str`  | از چتِ؟                             |
| `message_id`           | `str`  | شناسه‌ی پیام                        |
| `to_chat_id`           | `str`  | به چتِ؟                             |
| `disable_notification` | `bool` | غیرفعال کردن اعلان؟  (پیشفرض false) |

- خروجی

| فیلد              | نوع   | توضیحات           |
|-------------------|-------|-------------------|
| `new_message_id`  | `str` | شناسه‌ی پیام جدید |

- مثال

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


## ویرایش متن پیام 
- متد: ``editMessageText``
- ورودی

| فیلد                   | نوع    | توضیحات      |
|------------------------|--------|--------------|
| `token`                | `str`  | توکن         |
| `chat_id`              | `str`  | شناسه‌ی چت   |
| `message_id`           | `str`  | شناسه‌ی پیام |
| `text`                 | `str`  | پیام         |

- مثال

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


## ویرایش Inline Keypad 
- متد: ``editMessageKeypad``
- ورودی

| فیلد         | نوع    | توضیحات    |
|--------------|--------|------------|
| `token`      | `str`  | توکن       |
| `chat_id`    | `str`  | شناسه چت   |
| `message_id` | `str`  | شناسه پیام |

- مثال

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


## حذف پیام 
- متد: ``deleteMessage``
- ورودی

| فیلد         | نوع   | توضیحات      |
|--------------|-------|--------------|
| `token`      | `str` | توکن         |
| `chat_id`    | `str` | شناسه‌ی چت   |
| `message_id` | `str` | شناسه‌ی پیام |

- مثال

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


## تنظیم دستورات (commands) 
- متد: ``setCommands``
- ورودی

| فیلد           | نوع                                         | توضیحات             |
|----------------|---------------------------------------------|---------------------|
| `token`        | `str`                                       | توکن                |
| `bot_commands` | [`list[BotCommand]`](../models/#botcommand) | آرایه‌ای از دستورات |

- مثال

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/set_commands/set_commands.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/set_commands/set_commands.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/set_commands/set_commands_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/set_commands/set_commands_node.js!}
        ```
        </div>


## آپدیت آدرس بات (URL Endpoint) 
- متد: ``updateBotEndpoints``
- ورودی

| فیلد    | نوع                                                           | توضیحات   |
|---------|---------------------------------------------------------------|-----------|
| `token` | `str`                                                         | توکن      |
| `url`   | `str`                                                         | آدرس جدید |
| `type`  | [`UpdateEndpointTypeEnum`](../models/#updateendpointtypeenum) | نوع آدرس  |

- مثال

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/update_bot_endpoint/update_bot_endpoint.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/update_bot_endpoint/update_bot_endpoint.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/update_bot_endpoint/update_bot_endpoint_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/update_bot_endpoint/update_bot_endpoint_node.js!}
        ```
        </div>


## حذف keypad 
- متد: ``editChatKeypad``
- ورودی

| فیلد               | نوع    | توضیحات           |
|--------------------|--------|-------------------|
| `token`            | `str`  | توکن              |
| `chat_id`          | `str`  | شناسه‌ی چت        |
| `chat_keypad_type` | `str`  |  مقدارِ `Removed` |

- مثال

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/remove_chat_keypad/remove_chat_keypad.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/remove_chat_keypad/remove_chat_keypad.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/remove_chat_keypad/remove_chat_keypad_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/remove_chat_keypad/remove_chat_keypad_node.js!}
        ```
        </div>


## ویرایش keypad 
- متد: ``editChatKeypad``
- ورودی

| فیلد               | نوع                           | توضیحات      |
|--------------------|-------------------------------|--------------|
| `token`            | `str`                         | توکن         |
| `chat_id`          | `str`                         | شناسه‌ی چت   |
| `chat_keypad`      | [`Keypad`](../models/#keypad) | keypad       |
| `chat_keypad_type` | `str`                         | مقدارِ `New` |

- مثال

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_chat_keypad/edit_chat_keypad.sh!}
        ```
        </div>

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_chat_keypad/edit_chat_keypad.py!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/edit_chat_keypad/edit_chat_keypad_package.py!}
        ```
        </div>

    === "NodeJs"
        <div style="text-align: left">
        ```js
        {!> ../docs_src/edit_chat_keypad/edit_chat_keypad_node.js!}
        ```
        </div>
