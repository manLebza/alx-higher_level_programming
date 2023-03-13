#!/usr/bin/node
const request = require('request');
let nFilms = 0;

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    for (let x = 0; x < results.length; x++) {
      const characters = results[x].characters;
      for (let y = 0; y < characters.length; y++) {
        if (characters[y].search('18') > 0) {
          nFilms++;
        }
      }
    }
  }
  console.log(nFilms);
});
