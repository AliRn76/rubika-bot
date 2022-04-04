
### Chat
| فیلد         | نوع                             | توضیحات            |
|--------------|---------------------------------|--------------------|
| `chat_id`    | `str`                           | شناسه چت           |
| `chat_type`  | [`ChatTypeEnum`](#chattypeenum) | نوع چت             |
| `user_id`    | `str`                           | شناسه کاربر        |
| `first_name` | `str`                           | نام کاربر          |
| `last_name`  | `str`                           | نام خانوادگی کاربر |
| `title`      | `str`                           | ...                |
| `username`   | `str`                           | نام کاربری         |

### File
|  فیلد       | نوع     | توضیحات                  |
|-------------|---------|--------------------------|
| `file_id`   | `str`   | شناسه فایل               |
| `file_name` | `str`   | نام فایل                 |
| `size`      | `str`   | حجم فایل (به فرمت Bytes) |

### ForwardedFrom
| فیلد              | نوع                                       | توضیحات       |
|-------------------|-------------------------------------------|---------------|
| `type_from`       | [`ForwardedFromEnum`](#forwardedfromenum) | نوع فوروارد   |
| `message_id`      | `str`                                     | شناسه پیام    |
| `from_chat_id`    | `str`                                     | شناسه چت      |
| `from_sender_id`  | `str`                                     | شناسه کاربر   |


### PaymentStatus
| فیلد          |  نوع  | توضیحات                |
|---------------|-------|------------------------|
| `payment_id`  | `str` | شناسه پرداخت           |
| `status`      | `str` | can be (Paid, NotPaid) |


### MessageTextUpdate
| فیلد          | نوع     | توضیحات    |
|---------------|---------|------------|
| `message_id`  | `str`   | شناسه پیام |
| `text`        | `str`   | متن پیام   |

### Bot
|  فیلد           |  نوع            | توضیحات            |
|-----------------|-----------------|--------------------|
| `bot_id`        | `str`           | شناسه              |
| `bot_title`     | `str`           | عنوان              | 
| `avatar`        | [`File`](#file) | تصویر              |
| `description`   | `str`           | توضیحات            |
| `username`      | `str`           | نام‌کاربری ربات    |
| `start_message` | `str`           | پیام اولیه         |
| `share_url`     | `str`           | آدرسِ اشتراک‌گذاری |

### BotCommand
| فیلد            | نوع     | توضیحات       |
|-----------------|---------|---------------|
| `command`       | `str`   | متن دستور     |
| `description`   | `str`   | توضیحات دستور | 

### Sticker
|  فیلد             | نوع               | توضیحات          |
|-------------------|-------------------|------------------|
| `sticker_id`      | `str`             | شناسه استیکر     |
| `file`            | [`File`](#file)   | فایل             | 
| `emoji_character` | `str`             | کاراکترِ اموجی   | 

### ContactMessage
| فیلد             | نوع     | توضیحات       |
|------------------|---------|---------------|
| `phone_number`   | `str`   | شماره تلفن    |
| `first_name`     | `str`   | نام           | 
| `last_name`      | `str`   | نام خوانوادگی | 

### PollStatus
| فیلد                    | نوع                                 | توضیحات                     |
|-------------------------|-------------------------------------|-----------------------------|
| `state`                 | [`PollStatusEnum`](#pollstatusenum) | وضعیت نظرسنجی               |
| `selection_index`       | `int`                               | -1 به معنی انتخاب نشده است. | 
| `percent_vote_options`  | `list[int]`                         | ...                         |
| `total_vote`            | `int`                               | تعداد کل رای های نظرسنجی    | 
| `show_total_votes`      | `bool`                              | نمایش تمام رای ها؟          | 

### Poll
| فیلد             | نوع                          | توضیحات             |
|------------------|------------------------------|---------------------|
| `question`       | `str`                        | متن نظرسنجی         |
| `options`        | `list[str]`                  | گزینه‌های نظرسنجی   | 
| `poll_status`    | [`PollStatus`](#pollstatus)  | وضعیت نظرسنجی       |

### Location
| فیلد         | نوع     | توضیحات       |
|--------------|---------|---------------|
| `longitude`  | `str`   | طول جغرافیایی |
| `latitude`   | `str`   | عرض جغرافیایی | 

### LiveLocation
| فیلد                | نوع                                                 | توضیحات              |
|---------------------|-----------------------------------------------------|----------------------|
| `start_time`        | `str`                                               | زمان شروع            |
| `live_period`       | `int`                                               | مدت زمان (به ثانیه)  | 
| `current_location`  | [`Location`](#location)                             | موقعیت مکانی فعلی    | 
| `user_id`           | `str`                                               | شناسه کاربر          | 
| `status`            | [`LiveLocationStatusEnum`](#livelocationstatusenum) | وضعیت موقعیت مکانی   | 
| `last_update_time`  | `str`                                               | آخرین زمان بروزرسانی | 

### ButtonSelectionItem
| فیلد         | نوع                                                   | توضیحات        |
|--------------|-------------------------------------------------------|----------------|
| `text`       | `str`                                                 | متن دکمه       |
| `image_url`  | `str`                                                 | آدرس عکس دکمه  | 
| `type`       | [`ButtonSelectionTypeEnum`](#buttonselectiontypeenum) | نوع نمایش دکمه | 


### ButtonSelection
|  فیلد                | نوع                                                 | توضیحات                            |
|----------------------|-----------------------------------------------------|------------------------------------|
| `selection_id`       | `str`                                               | شناسه مربوط به لیست                |
| `search_type`        | `str`                                               | نوع جستجو                          | 
| `get_type`           | `str`                                               | نوع دریافت آیتم‌های لیست           | 
| `items`              | [`list[ButtonSelectionItem]`](#buttonselectionitem) | آرایه‌ای از ButtonSelectionItem ها | 
| `is_multi_selection` | `bool`                                              | امکان انتخاب چند آیتم              | 
| `columns_count`      | `str`                                               | تعداد ستون‌های لیست                | 
| `title`              | `str`                                               | عنوان                              |

### ButtonCalendar
| فیلد             | نوع                                                 | توضیحات            |
|------------------|-----------------------------------------------------|--------------------|
| `default_value`  | `Optional[str]`                                     | مقدار پیشفرض تقویم |
| `type`           | [`ButtonCalendarTypeEnum`](#buttoncalendartypeenum) | نوع تقویم          | 
| `min_year`       | `str`                                               | مقدار کمینه تقویم  | 
| `max_year`       | `str`                                               | مقدار بیشینه تقویم | 
| `title`          | `str`                                               | عنوان دکمه         | 


### ButtonNumberPicker
| فیلد             | نوع             | توضیحات      |
|------------------|-----------------|--------------|
| `min_value`      | `str`           | مقدار کمینه  |
| `max_value`      | `str`           | مقدار بیشینه | 
| `default_value`  | `Optional[str]` | مقدار پیشفرض | 
| `title`          | `str`           | عنوان دکمه   | 

### ButtonStringPicker
| فیلد             | نوع               | توضیحات            |
|------------------|-------------------|--------------------|
| `items`          | `list[str]`       | آرایه‌ای از متن‌ها |
| `default_value`  | `Optional[str]`   | مقدار پیشفرض       | 
| `title`          | `Optional[str]`   | عنوان دکمه         | 

### ButtonTextbox
| فیلد             | نوع                                                           | توضیحات            |
|------------------|---------------------------------------------------------------|--------------------|
| `type_line`      | [`ButtonTextboxTypeLineEnum`](#buttontextboxtypelineenum)     | نوع وارد کردن پیام |
| `type_keypad`    | [`ButtonTextboxTypeKeypadEnum`](#buttontextboxtypekeypadenum) | نوع صفحه کلید      | 
| `place_holder`   | `Optional[str]`                                               | ...                | 
| `title`          | `Optional[str]`                                               | عنوان دکمه         | 
| `default_value`  | `Optional[str]`                                               | مقدار پیشفرض       | 

### ButtonLocation
| فیلد                        | نوع                                                  | توضیحات            |
|-----------------------------|------------------------------------------------------|--------------------|
| `default_pointer_location`  | [`Location`](#location)                              | ...                |
| `default_map_location`      | [`Location`](#location)                              | موقعیت پیشفرض نقشه | 
| `type`                      | [`ButtonLocationTypeEnum`](#buttonlocationtypeenum)  | نوع نقشه           | 
| `title`                     | `Optional[str]`                                      | عنوان دکمه         | 
| `location_image_url`        | `str`                                                | ...                | 

### AuxData
|  فیلد       |  نوع  | توضیحات               |
|-------------|-------|-----------------------|
| `start_id`  | `str` | شناسه جهت دسترسی سریع |
| `button_id` | `str` | شناسه دکمه            |

### Button
|  فیلد                  | نوع                                         | توضیحات    |
|------------------------|---------------------------------------------|------------|
| `id`                   | `str`                                       | شناسه دکمه |
| `type`                 | [`ButtonTypeEnum`](#buttontypeenum)         | نوع دکمه   |
| `button_text`          | `str`                                       | متن دکمه   |
| `button_selection`     | [`ButtonSelection`](#buttonselection)       | ...        |
| `button_calendar`      | [`ButtonCalendar`](#buttoncalendar)         | ...        |
| `button_number_picker` | [`ButtonNumberPicker`](#buttonnumberpicker) | ...        |
| `button_string_picker` | [`ButtonStringPicker`](#buttonstringpicker) | ...        |
| `button_location`      | [`ButtonLocation`](#buttonlocation)         | ...        |
| `button_textbox`       | [`ButtonTextbox`](#buttontextbox)           | ...        |

### ButtonTypeEnum
| فیلد               |  نوع  | توضیحات                             |
|--------------------|-------|-------------------------------------|
| `Simple`           | `str` | نمایش دکمه به صورت معمولی           |
| `Selection`        | `str` | نمایش دکمه به صورت لیست             |
| `Calendar`         | `str` | نمایش دکمه به صورت تقویم            |
| `NumberPicker`     | `str` | نمایش دکمه به صورت لیستی از اعداد   |
| `StringPicker`     | `str` | نمایش دکمه به صورت لیستی از string  |
| `Location`         | `str` | ...                                 |
| `Payment`          | `str` | نمایش دکمه جهت پرداخت               |
| `CameraImage`      | `str` | نمایش دکمه جهت عکسبرداری از دوربین  |
| `CameraVideo`      | `str` | نمایش دکمه جهت فیلمبرداری از دوربین |
| `GalleryImage`     | `str` | نمایش دکمه جهت ارسال عکس از گالری   |
| `GalleryVideo`     | `str` | نمایش دکمه جهت ارسال فیلم از گالری  |
| `File`             | `str` | نمایش دکمه جهت ارسال فایل           |
| `Audio`            | `str` | نمایش دکمه جهت ارسال صوت            |
| `RecordAudio`      | `str` | نمایش دکمه جهت ضبط صوت              |
| `MyPhoneNumber`    | `str` | ...                                 |
| `MyLocation`       | `str` | ...                                 |
| `Textbox`          | `str` | نمایش دکمه جهت وارد کردن پیام متنی  |
| `Link`             | `str` | نمایش دکمه جهت ارسال آدرس اینترنتی  |
| `AskMyPhoneNumber` | `str` | ...                                 |
| `AskLocation`      | `str` | ...                                 |
| `Barcode`          | `str` | نمایش دکمه جهت اسکن بارکد           |

### KeypadRow

| فیلد      | نوع                      | توضیحات       |
|------------|---------------------------|-------------------|
| `buttons`  | [`list[Button]`](#button) | List of Buttons   |

### Keypad

| فیلد               | نوع                            | توضیحات  |
|---------------------|---------------------------------|--------------|
| `rows`              | [`list[KeypadRow]`](#keypadrow) | List of Rows |
| `resize_keyboard`   | `bool`                          | ...          |
| `on_time_keyboard`  | `bool`                          | ...          |

### MessageKeypadUpdate

| فیلد            | نوع                | توضیحات       |
|------------------|---------------------|-------------------|
| `message_id`     | `str`               | ID of Message     |
| `inline_keypad`  | [`Keypad`](#keypad) | New Inline Keypad |


### Message

| فیلد                 | نوع                                | توضیحات          |
|-----------------------|-------------------------------------|----------------------|
| `message_id`          | `str`                               | Unique ID of Message |
| `text`                | `str`                               | Text of Message      |
| `time`                | `int`                               | Unix Time            |
| `is_edited`           | `bool`                              | ...                  |
| `sender_type`         | `str`                               | can be (User, Bot)   |
| `sender_id`           | `str`                               | ID of Sender (User)  |
| `aux_data`            | [`AuxData`](#auxdata)               | ...                  |
| `file`                | [`File`](#file)                     | ...                  |
| `reply_to_message_id` | `str`                               | ...                  |
| `forwarded_from`      | [`ForwardedFrom`](#forwardedfrom)   | ...                  |
| `forwarded_no_link`   | `str`                               | ...                  |
| `location`            | [`Location`](#location)             | ...                  |
| `sticker`             | [`Sticker`](#sticker)               | ...                  |
| `contact_message`     | [`ContactMessage`](#contactmessage) | ...                  |
| `poll`                | [`Poll`](#poll)                     | ...                  |
| `live_location`       | [`LiveLocation`](#livelocation)     | ...                  |


### Update

| فیلد                | نوع                                        | توضیحات                                                                                 |
|----------------------|---------------------------------------------|---------------------------------------------------------------------------------------------|
| `type`               | `str`                                       | can be (UpdatedMessage, NewMessage, RemovedMessage, StartedBot, StoppedBot, UpdatedPayment) |
| `chat_id`            | `str`                                       | ID of Chat                                                                                  |
| `removed_message_id` | `Optional[str]`                             | ...                                                                                         |
| `new_message`        | [`Message`](#message)                       | ...                                                                                         |
| `updated_message`    | [`Optional[Message]`](#message)             | can be (User, Bot)                                                                          |
| `updated_payment`    | [`Optional[PaymentStatus]`](#paymentstatus) | ID of Sender (User)                                                                         |


### InlineMessage

| فیلد        | نوع                              | توضیحات                    |
|--------------|-----------------------------------|--------------------------------|
| `sender_id`  | `str`                             | ID of Sender (User)            |
| `text`       | `str`                             | Text of Message (can be empty) |
| `file`       | `File`                            | ...                            |
| `location`   | [`Optional[Location]`](#location) | ...                            |
| `aux_data`   | [`Optional[AuxData]`](#auxdata)   | ...                            |
| `message_id` | `str`                             | ID of Message                  |
| `chat_id`    | `str`                             | ID of Chat                     |



## Enums
<hr/>

### ChatTypeEnum
| فیلد      | توضیحات     |
|-----------|-------------|
| `User`    | چت با کاربر |
| `Bot`     | چت با ربات  |
| `Group`   | چت در گروه  |
| `Channel` | چت در کانال |

### ForwardedFromEnum
| فیلد       | توضیحات          |
|------------|------------------|
| `User`     | فوروارد از کاربر |
| `Channel`  | فوروارد از کانال |
| `Bot`      | فوروارد از ربات  |

### PaymentStatusEnum
| فیلد      | توضیحات     |
|-----------|-------------|
| `Paid`    | پرداخت شده  |
| `NotPaid` | پرداخت نشده |

### PollStatusEnum
| فیلد      | توضیحات               |
|-----------|-----------------------|
| `Open`    | نظرسنجی باز است.      |
| `Closed`  | نظرسنجی بسته شده است. | 

### LiveLocationStatusEnum
| فیلد      | توضیحات                |
|-----------|------------------------|
| `Stopped` | زمان شروع              |
| `Live`    | مدت زمان (به ثانیه)    | 

### ButtonSelectionTypeEnum
| فیلد          | توضیحات                           |
|---------------|-----------------------------------|
| `TextOnly`    | نمایش دکمه به صورت متن            |
| `TextImgThu`  | نمایش دکمه به صورت متن و عکس کوچک | 
| `TextImgBig`  | نمایش دکمه به صورت متن و عکس بزرگ |  

### ButtonSelectionSearchEnum
| فیلد    | توضیحات                                                          |
|---------|------------------------------------------------------------------|
| `None`  | حالت پیشفرض                                                      |
| `Local` | جستجو در آیتم‌های لیست با استفاده از مقادیر ارسالی در فیلد items | 
| `Api`   | جستجو در آیتم‌های لیست از طریق Api                               |

### ButtonSelectionGetEnum
| فیلد    | توضیحات                                                       |
|---------|---------------------------------------------------------------|
| `Local` | نمایش آیتم‌های لیست با استفاده از مقادیر ارسالی در فیلد items | 
| `Api`   | جستجو در آیتم‌های لیست از طریق Api                            |

### ButtonCalendarTypeEnum
| فیلد            | توضیحات                    |
|-----------------|----------------------------|
| `DatePersian`   | نمایش تقویم به فرمت شمسی   |
| `DateGregorian` | نمایش تقویم به فرمت میلادی | 

### ButtonTextboxTypeKeypadEnum
| فیلد     | نوع    | توضیحات                      |
|----------|--------|------------------------------|
| `String` | `str`  | امکان ارسال تمامی کاراکتر ها |
| `Number` | `str`  | امکان ارسال کاراکترهای عددی  | 

### ButtonTextboxTypeLineEnum
| فیلد         | نوع    | توضیحات                      |
|--------------|--------|------------------------------|
| `SingleLine` | `str`  | نوشتن پیام متنی در یک سطر    |
| `MultiLine`  | `str`  | نوشتن پیام متنی در چندین سطر | 

### ButtonLocationTypeEnum
| فیلد      | توضیحات |
|-----------|---------|
| `Picker`  | ...     |
| `View`    | ...     | 

