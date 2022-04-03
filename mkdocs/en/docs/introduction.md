
You will receive updates in <b>receiveUpdate</b> and <b>receiveInlineMessage</b> urls

### <u>receiveUpdate</u>
You'll get a request whenever user <b>send text</b> or tap a <b>keypad</b>

#### <i>sample request body:</i>

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

    
### <u>receiveInlineMessage</u>
You'll get a request whenever user tap an <b>inline keypad</b>

#### <i>sample request body:</i>
  
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

And when you get request, you can use these [methods](methods.md) for sending request to bot.
<hr/>