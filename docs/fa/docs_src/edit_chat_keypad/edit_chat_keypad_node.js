var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://messengerg2b1.iranlms.ir/v3/{{token}}/editChatKeypad',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
      "chat_id": chat_id,
      "chat_keypad_type": "New",
      "chat_keypad": {
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
        ],
        "resize_keyboard": true,
        "on_time_keyboard": false
      }
    })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});