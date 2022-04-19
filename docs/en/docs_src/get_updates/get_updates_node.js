var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://messengerg2b1.iranlms.ir/v3/{{token}}/getUpdates',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "limit": limit,
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});