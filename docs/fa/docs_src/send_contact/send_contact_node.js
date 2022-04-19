var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://messengerg2b1.iranlms.ir/v3/{{token}}/sendContact',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "chat_id": chat_id,
    "first_name": first_name,
    "last_name": last_name,
    "phone_number": phone_number
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});