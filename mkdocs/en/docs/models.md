### Chat

| Field        | Type   | Description                                      |
|--------------|--------|--------------------------------------------------|
| `chat_id`    | `str`  | Unique ID of Chat                                |
| `chat_type`  | `str`  | Type of Chat, can be (User, Bot, Group, Channel) |
| `user_id`    | `str`  | Unique ID of User                                |
| `first_name` | `str`  | First Name of User                               |
| `last_name`  | `str`  | Last Name of User                                |
| `title`      | `str`  | ...                                              |
| `username`   | `str`  | Username of User                                 |

### File

| Field       | Type   | Description       |
|-------------|--------|-------------------|
| `file_id`   | `str`  | Unique ID of File |
| `file_name` | `str`  | File Name         |
| `size`      | `str`  | in bytes          |

### ForwardedFrom

| Field            | Type   | Description                 |
|------------------|--------|-----------------------------|
| `type_from`      | `str`  | can be (User, Channel, Bot) |
| `message_id`     | `str`  | Unique ID of Message        |
| `from_chat_id`   | `str`  | ID of Origin Chat           |
| `from_sender_id` | `str`  | ID of Origin Sender (User)  |

### PaymentStatus

| Field        | Type   | Description            |
|--------------|--------|------------------------|
| `payment_id` | `str`  | Unique ID of Payment   |
| `status`     | `str`  | can be (Paid, NotPaid) |

### MessageTextUpdate

| Field        | Type   | Description          |
|--------------|--------|----------------------|
| `message_id` | `str`  | Unique ID of Message |
| `text`       | `str`  | Text                 |

### Bot

| Field           | Type            | Description          |
|-----------------|-----------------|----------------------|
| `bot_id`        | `str`           | Unique ID of Bot     |
| `bot_title`     | `str`           | Title of Bot         | 
| `avatar`        | [`File`](#file) | Avatar of Bot        |
| `description`   | `str`           | Description of Bot   |
| `username`      | `str`           | Username of Bot      |
| `start_message` | `str`           | Start Message of Bot |
| `share_url`     | `str`           | Share URL of Bot     |

### BotCommand

| Field          | Type   | Description             |
|----------------|--------|-------------------------|
| `command`      | `str`  | Command                 |
| `description`  | `str`  | Description of Command  | 

### Sticker

| Field             | Type             | Description          |
|-------------------|------------------|----------------------|
| `sticker_id`      | `str`            | Unique ID of Sticker |
| `file`            | [`File`](#file)  | Emoji File           | 
| `emoji_character` | `str`            | Character of Emoji   | 

### ContactMessage

| Field           | Type   | Description             |
|-----------------|--------|-------------------------|
| `phone_number`  | `str`  | Phone Number of Contact |
| `first_name`    | `str`  | First Name of Contact   | 
| `last_name`     | `str`  | Last Name of Contact    | 

### PollStatus

| Field                  | Type          | Description           |
|------------------------|---------------|-----------------------|
| `state`                | `str`         | can be (Open, Closed) |
| `selection_index`      | `int`         | -1 means not selected | 
| `percent_vote_options` | `list[int]`   | ...                   |
| `total_vote`           | `int`         | Total Vote Counts     | 
| `show_total_votes`     | `bool`        | ...                   | 

### Poll

| Field           | Type                        | Description         |
|-----------------|-----------------------------|---------------------|
| `question`      | `str`                       | Question Text       |
| `options`       | `list[str]`                 | Options of Question | 
| `poll_status`   | [`PollStatus`](#pollstatus) | ...                 |

### Location

| Field        | Type   | Description |
|--------------|--------|-------------|
| `longitude`  | `str`  | ...         |
| `latitude`   | `str`  | ...         | 

### LiveLocation

| Field              | Type                    | Description            |
|--------------------|-------------------------|------------------------|
| `start_time`       | `str`                   | ...                    |
| `live_period`      | `int`                   | in seconds             | 
| `current_location` | [`Location`](#location) | ...                    | 
| `user_id`          | `str`                   | Unique ID of User      | 
| `status`           | `str`                   | can be (Stopped, Live) | 
| `last_update_time` | `str`                   | ...                    | 

### ButtonSelectionItem

| Field       | Type     | Description                               |
|-------------|----------|-------------------------------------------|
| `text`      | `str`    | ...                                       |
| `image_url` | `str`    | ...                                       | 
| `type`      | `str`    | can be (TextOnly, TextImgThu, TextImgBig) | 

### ButtonSelection

| Field                | Type                                                | Description                   |
|----------------------|-----------------------------------------------------|-------------------------------|
| `selection_id`       | `str`                                               | Unique ID of Button Selection |
| `search_type`        | `Union[str, None]`                                  | can be (None, Local, Api)     | 
| `get_type`           | `str`                                               | can be (Local, Api)           | 
| `items`              | [`list[ButtonSelectionItem]`](#buttonselectionitem) | ...                           | 
| `is_multi_selection` | `bool`                                              |                               | 
| `columns_count`      | `str`                                               |                               | 
| `title`              | `str`                                               |                               | 

### ButtonCalendar

| Field           | Type                                                | Description                         |
|-----------------|-----------------------------------------------------|-------------------------------------|
| `default_value` | `str`                                               | ...                                 |
| `type`          | `Union[str, None]`                                  | can be (DatePersian, DateGregorian) | 
| `min_year`      | `str`                                               | ...                                 | 
| `max_year`      | [`list[ButtonSelectionItem]`](#buttonselectionitem) | ...                                 | 
| `title`         | `str`                                               | ...                                 | 

### ButtonNumberPicker

| Field           | Type               | Description                         |
|-----------------|--------------------|-------------------------------------|
| `min_value`     | `int`              | ...                                 |
| `max_value`     | `int`              | can be (DatePersian, DateGregorian) | 
| `default_value` | `Union[str, None]` | ...                                 | 
| `title`         | `Optional[str]`    | ...                                 | 

### ButtonStringPicker

| Field           | Type             | Description |
|-----------------|------------------|-------------|
| `items`         | `list[str]`      | ...         |
| `default_value` | `Optional[str]`  | ...         | 
| `title`         | `Optional[str]`  | ...         | 

### ButtonTextbox

| Field           | Type            | Description                    |
|-----------------|-----------------|--------------------------------|
| `type_line`     | `str`           | can be (SingleLine, MultiLine) |
| `type_keypad`   | `str`           | can be (String, Number)        | 
| `place_holder`  | `Optional[str]` | ...                            | 
| `title`         | `Optional[str]` | ...                            | 
| `default_value` | `Optional[str]` | ...                            | 

### ButtonLocation

| Field                       | Type                     | Description         |
|-----------------------------|--------------------------|---------------------|
| `default_pointer_location`  | [`Location`](#location)  | ...                 |
| `default_map_location`      | [`Location`](#location)  | ...                 | 
| `type`                      | `str`                    | can be Picker, View | 
| `title`                     | `str`                    | ...                 | 
| `location_image_url`        | `str`                    | ...                 | 

### AuxData

| Field       | Type   | Description         |
|-------------|--------|---------------------|
| `start_id`  | `str`  | ...                 |
| `button_id` | `str`  | ...                 |

### Button

| Field                  | Type                                        | Description                                                                                                                                                                                                                                           |
|------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                   | `str`                                       | Unique ID of Button                                                                                                                                                                                                                                   |
| `type`                 | `str`                                       | can be (Simple, Selection, Calendar, NumberPicker, StringPicker, Location, Payment, CameraImage, CameraVideo, GalleryImage, GalleryVideo, File, Audio, RecordAudio, MyPhoneNumber, MyLocation, Textbox, Link, AskMyPhoneNumber, AskLocation, Barcode) |
| `button_text`          | `str`                                       | ...                                                                                                                                                                                                                                                   |
| `button_selection`     | [`ButtonSelection`](#buttonselection)       | ...                                                                                                                                                                                                                                                   |
| `button_calendar`      | [`ButtonCalendar`](#buttoncalendar)         | ...                                                                                                                                                                                                                                                   |
| `button_number_picker` | [`ButtonNumberPicker`](#buttonnumberpicker) | ...                                                                                                                                                                                                                                                   |
| `button_string_picker` | [`ButtonStringPicker`](#buttonstringpicker) | ...                                                                                                                                                                                                                                                   |
| `button_location`      | [`ButtonLocation`](#buttonlocation)         | ...                                                                                                                                                                                                                                                   |
| `button_textbox`       | [`ButtonTextbox`](#buttontextbox)           | ...                                                                                                                                                                                                                                                   |

### KeypadRow

| Field      | Type                      | Description       |
|------------|---------------------------|-------------------|
| `buttons`  | [`list[Button]`](#button) | List of Buttons   |

### Keypad

| Field               | Type                            | Description  |
|---------------------|---------------------------------|--------------|
| `rows`              | [`list[KeypadRow]`](#keypadrow) | List of Rows |
| `resize_keyboard`   | `bool`                          | ...          |
| `on_time_keyboard`  | `bool`                          | ...          |

### MessageKeypadUpdate

| Field            | Type                | Description       |
|------------------|---------------------|-------------------|
| `message_id`     | `str`               | ID of Message     |
| `inline_keypad`  | [`Keypad`](#keypad) | New Inline Keypad |


### Message

| Field                 | Type                                | Description          |
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

| Field                | Type                                        | Description                                                                                 |
|----------------------|---------------------------------------------|---------------------------------------------------------------------------------------------|
| `type`               | `str`                                       | can be (UpdatedMessage, NewMessage, RemovedMessage, StartedBot, StoppedBot, UpdatedPayment) |
| `chat_id`            | `str`                                       | ID of Chat                                                                                  |
| `removed_message_id` | `Optional[str]`                             | ...                                                                                         |
| `new_message`        | [`Message`](#message)                       | ...                                                                                         |
| `updated_message`    | [`Optional[Message]`](#message)             | can be (User, Bot)                                                                          |
| `updated_payment`    | [`Optional[PaymentStatus]`](#paymentstatus) | ID of Sender (User)                                                                         |


### InlineMessage

| Field        | Type                              | Description                    |
|--------------|-----------------------------------|--------------------------------|
| `sender_id`  | `str`                             | ID of Sender (User)            |
| `text`       | `str`                             | Text of Message (can be empty) |
| `file`       | `File`                            | ...                            |
| `location`   | [`Optional[Location]`](#location) | ...                            |
| `aux_data`   | [`Optional[AuxData]`](#auxdata)   | ...                            |
| `message_id` | `str`                             | ID of Message                  |
| `chat_id`    | `str`                             | ID of Chat                     |



