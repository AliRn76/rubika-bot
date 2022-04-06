Rubika has created APIs for you that you can use to build your own "bot".

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

  Once you have received the above request from the bot and processed it, you can respond using [these methods](methods.md).