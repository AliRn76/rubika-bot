
### Chat
| Field        | Type                            | Description |
|--------------|---------------------------------|-------------|
| `chat_id`    | `str`                           | Chat ID     |
| `chat_type`  | [`ChatTypeEnum`](#chattypeenum) | Chat Type   |
| `user_id`    | `str`                           | User ID     |
| `first_name` | `str`                           | First Name  |
| `last_name`  | `str`                           | Last Name   |
| `title`      | `str`                           | Title       |
| `username`   | `str`                           | Username    |

### File
| Field       | Type   | Description          |
|-------------|--------|----------------------|
| `file_id`   | `str`  | File ID              |
| `file_name` | `str`  | File Name            |
| `size`      | `str`  | File Size (In Bytes) |

### ForwardedFrom
| Field            | Type                                      | Description       |
|------------------|-------------------------------------------|-------------------|
| `type_from`      | [`ForwardedFromEnum`](#forwardedfromenum) | Forward From Type |
| `message_id`     | `str`                                     | Message ID        |
| `from_chat_id`   | `str`                                     | Froward From?     |
| `from_sender_id` | `str`                                     | From Sender?      |


### PaymentStatus
| Field        | Type                                      | Description    |
|--------------|-------------------------------------------|----------------|
| `payment_id` | `str`                                     | Payment ID     |
| `status`     | [`PaymentStatusEnum`](#paymentstatusenum) | Payment Status |


### MessageTextUpdate
| Field        | Type   | Description      |
|--------------|--------|------------------|
| `message_id` | `str`  | Message ID       |
| `text`       | `str`  | Message New Text |

### Bot
| Field            | Type            | Description       |
|------------------|-----------------|-------------------|
| `bot_id`         | `str`           | Bot ID            |
| `bot_title`      | `str`           | Bot Title         | 
| `avatar`         | [`File`](#file) | Bot Avatar        |
| `description`    | `str`           | Bot Description   |
| `username`       | `str`           | Bot Username      |
| `start_message`  | `str`           | Bot Start Message |
| `share_url`      | `str`           | Bot Shar URL      |

### BotCommand
| Field         | Type   | Description         |
|---------------|--------|---------------------|
| `command`     | `str`  | Command Text        |
| `description` | `str`  | Command Description | 

### Sticker
| Field             | Type            | Description             |
|-------------------|-----------------|-------------------------|
| `sticker_id`      | `str`           | Sticker ID              |
| `file`            | [`File`](#file) | Sticker File            | 
| `emoji_character` | `str`           | Sticker Emoji Character | 

### ContactMessage
| Field          | Type   | Description  |
|----------------|--------|--------------|
| `phone_number` | `str`  | Phone Number |
| `first_name`   | `str`  | First Name   | 
| `last_name`    | `str`  | Last Name    | 

### PollStatus
| Field                  | Type                                | Description           |
|------------------------|-------------------------------------|-----------------------|
| `state`                | [`PollStatusEnum`](#pollstatusenum) | Poll Status           |
| `selection_index`      | `int`                               | -1 Means Not Selected | 
| `percent_vote_options` | `list[int]`                         | ...                   |
| `total_vote`           | `int`                               | Total Vote            | 
| `show_total_votes`     | `bool`                              | Show Total Votes?     | 

### Poll
| Field         | Type                        | Description   |
|---------------|-----------------------------|---------------|
| `question`    | `str`                       | Poll Question |
| `options`     | `list[str]`                 | Poll Options  | 
| `poll_status` | [`PollStatus`](#pollstatus) | Poll Status   |

### Location
| Field       | Type  | Description |
|-------------|-------|-------------|
| `longitude` | `str` | Longitude   |
| `latitude`  | `str` | Latitude    | 

### LiveLocation
| Field              | Type                                                | Description          |
|--------------------|-----------------------------------------------------|----------------------|
| `start_time`       | `str`                                               | Start Time           |
| `live_period`      | `int`                                               | Live Period          | 
| `current_location` | [`Location`](#location)                             | Current Location     | 
| `user_id`          | `str`                                               | User ID              | 
| `status`           | [`LiveLocationStatusEnum`](#livelocationstatusenum) | Live Location Status | 
| `last_update_time` | `str`                                               | Last Update          | 

### ButtonSelectionItem
| Field       | Type                                                  | Description      |
|-------------|-------------------------------------------------------|------------------|
| `text`      | `str`                                                 | Button Text      |
| `image_url` | `str`                                                 | Button Image URL | 
| `type`      | [`ButtonSelectionTypeEnum`](#buttonselectiontypeenum) | Button Type      | 


### ButtonSelection
| Field                | Type                                                | Description                  |
|----------------------|-----------------------------------------------------|------------------------------|
| `selection_id`       | `str`                                               | Button Selection ID          |
| `search_type`        | `str`                                               | Search Type                  | 
| `get_type`           | `str`                                               | Get Items Type               | 
| `items`              | [`list[ButtonSelectionItem]`](#buttonselectionitem) | Array Of ButtonSelectionItem | 
| `is_multi_selection` | `bool`                                              | Is Multi Selection?          | 
| `columns_count`      | `str`                                               | Columns Count                | 
| `title`              | `str`                                               | Title                        |

### ButtonCalendar
| Field           | Type                                                | Description            |
|-----------------|-----------------------------------------------------|------------------------|
| `default_value` | `Optional[str]`                                     | Calendar Default Value |
| `type`          | [`ButtonCalendarTypeEnum`](#buttoncalendartypeenum) | Calendar Type          | 
| `min_year`      | `str`                                               | Calendar Min Year      | 
| `max_year`      | `str`                                               | Calendar Max Year      | 
| `title`         | `str`                                               | Calendar Title         | 


### ButtonNumberPicker
| Field           | Type            | Description   |
|-----------------|-----------------|---------------|
| `min_value`     | `str`           | Min Value     |
| `max_value`     | `str`           | Max Value     | 
| `default_value` | `Optional[str]` | Default Value | 
| `title`         | `str`           | Title         | 

### ButtonStringPicker
| Field           | Type            | Description   |
|-----------------|-----------------|---------------|
| `items`         | `list[str]`     | String Items  |
| `default_value` | `Optional[str]` | Default Value | 
| `title`         | `Optional[str]` | Button Title  | 

### ButtonTextbox
| Field           | Type                                                          | Description      |
|-----------------|---------------------------------------------------------------|------------------|
| `type_line`     | [`ButtonTextboxTypeLineEnum`](#buttontextboxtypelineenum)     | Button Text Type |
| `type_keypad`   | [`ButtonTextboxTypeKeypadEnum`](#buttontextboxtypekeypadenum) | Keypad Type      | 
| `place_holder`  | `Optional[str]`                                               | Placeholder      | 
| `title`         | `Optional[str]`                                               | Button Title     | 
| `default_value` | `Optional[str]`                                               | Default Value    | 

### ButtonLocation
| Field                      | Type                                                | Description          |
|----------------------------|-----------------------------------------------------|----------------------|
| `default_pointer_location` | [`Location`](#location)                             | ...                  |
| `default_map_location`     | [`Location`](#location)                             | Default Map Location | 
| `type`                     | [`ButtonLocationTypeEnum`](#buttonlocationtypeenum) | Button Location Type | 
| `title`                    | `Optional[str]`                                     | Button Title         | 
| `location_image_url`       | `str`                                               | ...                  | 

### AuxData
| Field       | Type  | Description |
|-------------|-------|-------------|
| `start_id`  | `str` | Start ID    |
| `button_id` | `str` | Button ID   |

### Button
| Field                  | Type                                        | Description  |
|------------------------|---------------------------------------------|--------------|
| `id`                   | `str`                                       | Button ID    |
| `type`                 | [`ButtonTypeEnum`](#buttontypeenum)         | Button Type  |
| `button_text`          | `str`                                       | Button Text  |
| `button_selection`     | [`ButtonSelection`](#buttonselection)       | ...          |
| `button_calendar`      | [`ButtonCalendar`](#buttoncalendar)         | ...          |
| `button_number_picker` | [`ButtonNumberPicker`](#buttonnumberpicker) | ...          |
| `button_string_picker` | [`ButtonStringPicker`](#buttonstringpicker) | ...          |
| `button_location`      | [`ButtonLocation`](#buttonlocation)         | ...          |
| `button_textbox`       | [`ButtonTextbox`](#buttontextbox)           | ...          |

### ButtonTypeEnum
| Field              | Type   | Description                        |
|--------------------|--------|------------------------------------|
| `Simple`           | `str`  | Show Simple Button                 |
| `Selection`        | `str`  | Show Selection (List) Button       |
| `Calendar`         | `str`  | Show Calendar Button               |
| `NumberPicker`     | `str`  | Show Number Picker Button          |
| `StringPicker`     | `str`  | Show Button As Array Of Strings    |
| `Location`         | `str`  | ...                                |
| `Payment`          | `str`  | Show Button For Payment            |
| `CameraImage`      | `str`  | Button For Capture Image           |
| `CameraVideo`      | `str`  | Button For Capture Video           |
| `GalleryImage`     | `str`  | Button For Take Image From Gallery |
| `GalleryVideo`     | `str`  | Button For Take Video From Gallery |
| `File`             | `str`  | Button For Send File               |
| `Audio`            | `str`  | Button For Send Audio              |
| `RecordAudio`      | `str`  | Button For Record Voice            |
| `MyPhoneNumber`    | `str`  | ...                                |
| `MyLocation`       | `str`  | ...                                |
| `Textbox`          | `str`  | Textbox Button                     |
| `Link`             | `str`  | Link Button                        |
| `AskMyPhoneNumber` | `str`  | ...                                |
| `AskLocation`      | `str`  | ...                                |
| `Barcode`          | `str`  | Button For Scan Button             |

### KeypadRow
| Field     | Type                      | Description      |
|-----------|---------------------------|------------------|
| `buttons` | [`list[Button]`](#button) | Array Of Buttons |

### Keypad
| Field              | Type                            | Description       |
|--------------------|---------------------------------|-------------------|
| `rows`             | [`list[KeypadRow]`](#keypadrow) | Array Of Keypads  |
| `resize_keyboard`  | `bool`                          | Resize Keyboard ? |
| `on_time_keyboard` | `bool`                          | ...               |

### MessageKeypadUpdate
| Field           | Type                | Description |
|-----------------|---------------------|-------------|
| `message_id`    | `str`               | Message ID  |
| `inline_keypad` | [`Keypad`](#keypad) | Keypad      |


### Message
| Field                 | Type                                      | Description      |
|-----------------------|-------------------------------------------|------------------|
| `message_id`          | `str`                                     | Message ID       |
| `text`                | `str`                                     | Text             |
| `time`                | `int`                                     | Time             |
| `is_edited`           | `bool`                                    | Is Edited ?      |
| `sender_type`         | [`MessageSenderEnum`](#messagesenderenum) | Sender Type      |
| `sender_id`           | `str`                                     | Sender ID        |
| `aux_data`            | [`AuxData`](#auxdata)                     | ...              |
| `file`                | [`File`](#file)                           | File             |
| `reply_to_message_id` | `str`                                     | Replying On?     |
| `forwarded_from`      | [`ForwardedFrom`](#forwardedfrom)         | Forwarded From ? |
| `forwarded_no_link`   | `str`                                     | ...              |
| `location`            | [`Location`](#location)                   | Location         |
| `sticker`             | [`Sticker`](#sticker)                     | Sticker          |
| `contact_message`     | [`ContactMessage`](#contactmessage)       | ...              |
| `poll`                | [`Poll`](#poll)                           | Poll             |
| `live_location`       | [`LiveLocation`](#livelocation)           | Current Location |


### Update
| Field                | Type                                        | Description        |
|----------------------|---------------------------------------------|--------------------|
| `type`               | [`UpdateTypeEnum`](#updatetypeenum)         | Update Type        |
| `chat_id`            | `str`                                       | Chat ID            |
| `removed_message_id` | `Optional[str]`                             | Removed Message ID |
| `new_message`        | [`Message`](#message)                       | New Message        |
| `updated_message`    | [`Optional[Message]`](#message)             | Updated Message    |
| `updated_payment`    | [`Optional[PaymentStatus]`](#paymentstatus) | Update Payment     |


### InlineMessage
| Field        | Type                              | Description |
|--------------|-----------------------------------|-------------|
| `sender_id`  | `str`                             | Sender ID   |
| `text`       | `str`                             | Text        |
| `file`       | `Optional[File]`                  | File        |
| `location`   | [`Optional[Location]`](#location) | Location    |
| `aux_data`   | [`Optional[AuxData]`](#auxdata)   | ...         |
| `message_id` | `str`                             | Message ID  |
| `chat_id`    | `str`                             | Chat ID     |



## Enums
<hr/>

### ChatTypeEnum
| Field     | Description     |
|-----------|-----------------|
| `User`    | Chat With User  |
| `Bot`     | Chat With Bot   |
| `Group`   | Chat In Group   |
| `Channel` | Chat In Channel |

### ForwardedFromEnum
| Field     | Description            |
|-----------|------------------------|
| `User`    | Forwarded From User    |
| `Channel` | Forwarded From Channel |
| `Bot`     | Forwarded From Bot     |

### PaymentStatusEnum
| Field     | Description |
|-----------|-------------|
| `Paid`    | Paid        |
| `NotPaid` | Not Paid    |

### PollStatusEnum
| Field    | Description    |
|----------|----------------|
| `Open`   | Poll Is Open   |
| `Closed` | Poll Is Closed | 

### LiveLocationStatusEnum
| Field     | Description           |
|-----------|-----------------------|
| `Stopped` | Live Location Stopped |
| `Live`    | Live Location Is Live | 

### ButtonSelectionTypeEnum
| Field        | Description            |
|--------------|------------------------|
| `TextOnly`   | Text                   |
| `TextImgThu` | Text And Small Picture | 
| `TextImgBig` | Text And Big Picture   |  

### ButtonSelectionSearchEnum
| Field   | Description                                           |
|---------|-------------------------------------------------------|
| `None`  | Default                                               |
| `Local` | Search In List Items With Fields That Sent In 'items' | 
| `Api`   | Search In List Items With API                         |

### ButtonSelectionGetEnum
| Field   | Description                                           |
|---------|-------------------------------------------------------|
| `Local` | Search In List Items With Fields That Sent In 'items' | 
| `Api`   | Search In List Items With API                         |

### ButtonCalendarTypeEnum
| Field           | Description    |
|-----------------|----------------|
| `DatePersian`   | Persian Date   |
| `DateGregorian` | Gregorian Data | 

### ButtonTextboxTypeKeypadEnum
| Field    | Type   | Description                 |
|----------|--------|-----------------------------|
| `String` | `str`  | Can Send All The Characters |
| `Number` | `str`  | Can Send Numeric Characters | 

### ButtonTextboxTypeLineEnum
| Field        | Type  | Description      |
|--------------|-------|------------------|
| `SingleLine` | `str` | Single Line Text |
| `MultiLine`  | `str` | Multi Line Text  | 

### ButtonLocationTypeEnum
| Field    | Description |
|----------|-------------|
| `Picker` | ...         |
| `View`   | ...         | 

### MessageSenderEnum
| Field  | Description |
|--------|-------------|
| `User` | User        |
| `Bot`  | Bot         |

### UpdateTypeEnum
| Field            | Description    |
|------------------|----------------|
| `UpdatedMessage` | Update Message |
| `NewMessage`     | New Message    |
| `RemovedMessage` | Remove Message |
| `StartedBot`     | Start Bot      |
| `StoppedBot`     | Stop Bot       |
| `UpdatedPayment` | Update Payment |

### ChatKeypadTypeEnum
| Field    | Description    |
|----------|----------------|
| `None`   | Default Value  |
| `New`    | New Keypad     |
| `Remove` | Remove Keypad  |