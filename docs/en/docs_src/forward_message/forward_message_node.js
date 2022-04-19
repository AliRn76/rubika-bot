var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://messengerg2b1.iranlms.ir/v3/{{token}}/frowardMessage',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "from_chat_id": from_chat_id,
    "message_id": message_id,
    "to_chat_id": to_chat_id
  })
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});