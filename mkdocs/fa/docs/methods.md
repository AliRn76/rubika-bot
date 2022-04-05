
## گرفتن اطلاعات بات

- ورودی

| فیلد     | نوع    | توضیحات |
|----------|--------|---------|
| `token`  | `str`  | توکن    |

- خروجی

| فیلد   | نوع                     | توضیحات |
|--------|-------------------------|---------|
| `bot`  | [`Bot`](../models/#bot) | بات     |

- مثال

    === "Python"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_me/get_me.py!}
        ```
        </div>

    === "cURL"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_me/get_me.sh!}
        ```
        </div>
  
    === "Python Package"
        <div style="text-align: left">
        ```python
        {!> ../docs_src/get_me/get_me_package.py!}
        ```
        </div>


## ارسال پیام (Text, Keypad, InlineKeypad)

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


## ارسال keypad

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


## ارسال پیام متنی

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


## ارسال نظرسنجی

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


## ارسال موقعیت مکانی

- ورودی

| فیلد                   | نوع                                     | توضیحات                             |
|------------------------|-----------------------------------------|-------------------------------------|
| `token`                | `str`                                   | توکن                                |
| `chat_id`              | `str`                                   | شناسه‌ی چت                          |
| `latitude`             | `str`                                   | متن سوال                            |
| `longitude`            | `str`                                   | طول جغرافیایی                       |
| `chat_keypad`          | `str`                                   | عرض جغرافیایی                       |
| `disable_notification` | `str`                                   | غیرفعال کردن اعلان؟  (پیشفرض false) |
| `inline_keypad`        | [`Optional[Keypad]`](../models/#keypad) | ...                                 |
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


## ارسال استیکر 

- ورودی

| فیلد                   | نوع                                     | توضیحات                             |
|------------------------|-----------------------------------------|-------------------------------------|
| `token`                | `str`                                   | توکن                                |
| `chat_id`              | `str`                                   | شناسه‌ی چت                          |
| `sticker_id`           | `str`                                   | شناسه‌ی استیکر                      |
| `chat_keypad`          | `str`                                   | عرض جغرافیایی                       |
| `disable_notification` | `str`                                   | غیرفعال کردن اعلان؟  (پیشفرض false) |
| `inline_keypad`        | [`Optional[Keypad]`](../models/#keypad) | ...                                 |
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


## ارسال مخاطب 

- ورودی

| فیلد                   | نوع                                     | توضیحات                             |
|------------------------|-----------------------------------------|-------------------------------------|
| `token`                | `str`                                   | توکن                                |
| `chat_id`              | `str`                                   | شناسه‌ی چت                          |
| `first_name`           | `str`                                   | نام مخاطب                           |
| `last_name`            | `str`                                   | نام‌خانوادگی مخاطب                  |
| `phone_number`         | `str`                                   | شماره مخاطب                         |
| `chat_keypad`          | `str`                                   | عرض جغرافیایی                       |
| `disable_notification` | `str`                                   | غیرفعال کردن اعلان؟  (پیشفرض false) |
| `inline_keypad`        | [`Optional[Keypad]`](../models/#keypad) | ...                                 |
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

- مثال

    ```python
    
    ```


## گرفتن اطلاعات چت 

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


## گرفتن آخرین آپدیت‌ها 

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


## فوروارد کردن پیام 

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


## ویرایش متن پیام 

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


## ویرایش Inline Keypad 

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

### حذف پیام 

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

