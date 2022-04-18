var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://messengerg2b1.iranlms.ir/v3/{{token}}/setCommands',
  'headers': {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
      "bot_commands": [
          {
              "command": "command1",
              "description": "description1"
          },
          {
              "command": "command2",
              "description": "description2"
          },
      ]
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});