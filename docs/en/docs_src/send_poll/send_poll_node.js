var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://messengerg2b1.iranlms.ir/v3/{{token}}/sendPoll',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "chat_id": chat_id,
    "question": "Do you have any question?",
    "options": ["yes", "no"],
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});