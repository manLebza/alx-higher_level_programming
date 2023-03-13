#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/';
let id = parseInt(process.argv[2], 10);
let characters = [];

request(url, function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }
    for (let x = 0; x < results.length; x++) {
      if results[x].episode_id === id) {
        characters = results[x].characters;
	break;
      }
    }
    for (let y = 0; y < characters.length; y++) {
        request(characters[y], function (err, response, body) {
	if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
