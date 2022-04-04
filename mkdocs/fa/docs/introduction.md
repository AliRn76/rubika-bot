
شما آپدیت رو در url های <b> receiveUpdate </b> و <b> receiveInlineMessage </b> دریافت خواهید کرد.

### <u>receiveUpdate</u>

هرگاه کاربر روی <b> keypad </b> بزند یا <b> پیامی ارسال </b>  کند، شما از این نوع ریکوئست دریافت میکنید. 

#### <i>نمونه‌ی body یک ریکوئست:</i>

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

  - <b>sender_id: </b> شناسه‌ای یکتا که به کاربر تعلق میگیرد. 
  - <b>text: </b>متن دکمه‌ای که ارسال شده. 
  - <b>button_id: </b>شناسه‌ای است که شما برای دکمه مورد نظر تنظیم کرده اید. 
  - <b>message_id: </b>شناسه‌ای یکتا که به پیام تعلق میگیرد. 
  - <b>chat_id: </b>شناسه‌ای یکتا که به مکالمه‌ی بین کاربر و ربات تعلق میگیرد <b> (شما در ادامه باید از این شناسه استفاده کنید.) </b> 

    
### <u>receiveInlineMessage</u>
You'll get a request whenever user tap an <b>inline keypad</b>

#### <i>نمونه‌ی body یک ریکوئست:</i>
  
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

  - <b>type: </b> میتواند <b> NewMessage </b>, <b> StartedBot </b>, <b>StoppedBot</b> و ... باشد. 
  - <b>text: </b>متن دکمه‌ای که ارسال شده. 
  - <b>button_id: </b>شناسه‌ای است که شما برای دکمه مورد نظر تنظیم کرده اید. 
  - <b>message_id: </b>شناسه‌ای یکتا که به پیام تعلق میگیرد. 
  - <b>chat_id: </b>شناسه‌ای یکتا که به مکالمه‌ی بین کاربر و ربات تعلق میگیرد <b> (شما در ادامه باید از این شناسه استفاده کنید.) </b> 

و زمانی که شما از طرف ربات به شکل بالا ریکوئست را دریافت کردید و آن را پردازش کردید، میتوانید با استفاده از [این متد](methods.md) ها میتوانید پاسخ کاربر را بدهید.
