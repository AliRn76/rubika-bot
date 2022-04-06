var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://messengerg2b1.iranlms.ir/v3/{{token}}/editMessageText',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
      "chat_id": chat_id,
      "message_id": message_id,
      "inline_keypad": {
        "rows": [
          {
            "buttons": [
              {
                "id": "100",
                "type": "Simple",
                "button_text": "Add Account"
              }
            ]
          },
          {
            "buttons": [
              {
                "id": "101",
                "type": "Simple",
                "button_text": "Edit Account"
              },
              {
                "id": "102",
                "type": "Simple",
                "button_text": "Remove Account"
              }
            ]
          }
        ]
      }
    })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});