#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', (error, content) => {
  if (error) {
    console.log(error);
    return;
  }
    console.log(content);
});
