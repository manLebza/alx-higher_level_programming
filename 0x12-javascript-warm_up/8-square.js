#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0, s; x < size; x++) {
    s = '';
    for (let y = 0; y < size; y++) {
      s += 'I';
    }
    console.log(s);
  }
}
