روبیکا  API هایی در اختیار کاربران قرار می‌دهد که با استفاده از آنها می‌توانید «بات» خودتان را بسازید. برای استفاده از این امکان تازه، مراحل زیر را طی کنید.


##مراحل استفاده 
- با استفاده از Bot Father یک بات بسازید.
- توکن دریافتی را کپی کنید و در باقی مراحل از آن استفاده کنید.
- با استفاده از توکن دریافتی در مرحله‌ قبل و مِتُد مورد نظر، URL ای با قالب زیر بسازید و با متد POST به آن Request بزنید.

```python
https://messengerg2b1.iranlms.ir/v3/{token}/{method}
```

* اگر از زبان ``python`` استفاده می‌کنید، می‌تونید برای ساخت بات از [rubika-bot](https://pypi.org/project/rubika-bot/)  نیز استفاده کنید. 

## توضیحات 

بعد از اینکه بات را در Bot Father ساختید و Endpoint خودتان را تعریف کردید، سیستم هر event یا پیامی را که به بات شما فرستاده شود، به یکی از دو روش زیر برای Endpoint شما با متد POST ارسال می‌کند

- Endpoint/``receiveUpdate``
- Endpoint/``receiveInlineMessage``

<br/>

### <u>receiveUpdate</u>

هر زمان کاربر <b> پیامی ارسال </b> کند یا <b> chat keypad </b> را لمس کند، شما `receiveUpdate` دریافت می‌کنید. 

<br/>
<i>نمونه body :</i>

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

  - <b>sender_id : </b> شناسه‌ای یکتا که به کاربر تعلق می‌گیرد. 
  - <b>text : </b>متن دکمه‌ای که ارسال شده. 
  - <b>button_id : </b>شناسه‌ای که شما برای دکمه مورد نظر تنظیم کرده‌اید. 
  - <b>message_id : </b>شناسه‌ای یکتا که به پیام تعلق می‌گیرد. 
  - <b>chat_id : </b>شناسه‌ای یکتا که به مکالمه‌ی بین کاربر و ربات تعلق می‌گیرد <b> (شما در ادامه باید از این شناسه استفاده کنید.) </b> 

    
<br/>

### <u>receiveInlineMessage</u>
هر گاه کاربر روی inline keypad بزند، شما `receiveInlineMessage` دریافت می‌کنید.

<br/>
<i>نمونه body :</i>

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

  - <b>type : </b> می‌تواند <b> NewMessage </b>, <b> StartedBot </b>, <b>StoppedBot</b> و... باشد. 
  - <b>text : </b>متن دکمه‌ای که ارسال شده. 
  - <b>button_id : </b>شناسه‌ای است که شما برای دکمه مورد نظر تنظیم کرده‌اید. 
  - <b>message_id : </b>شناسه‌ای یکتا که به پیام تعلق می‌گیرد. 
  - <b>chat_id : </b>شناسه‌ای یکتا که به مکالمه‌ی بین کاربر و ربات تعلق می‌گیرد <b> (شما در ادامه باید از این شناسه استفاده کنید.) </b> 

 زمانی که شما از طرف بات به شکل بالا Request را دریافت و پردازش کردید، می‌توانید با استفاده از [این متد‌ها](methods.md) به آن پاسخ دهید.
