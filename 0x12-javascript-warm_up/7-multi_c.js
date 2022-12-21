#!/usr/bin/node
let x = parseInt(process.argv[2]);
if (Number.isNaN(x)) {
  console.log('Missing number of occurrances');
} else {
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}
