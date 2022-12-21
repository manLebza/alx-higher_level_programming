#!/usr/bin/node
let biggest = 0;
let x;
const arrayNums = [];
for (x = 2; x < process.argv.length; x++) {
  if (Number.isNaN(parseInt(process.argv[x])) === false) {
    arrayNums[x - 2] = parseInt(process.argv[x]);
  }
}
if (arrayNums.length > 1) {
  biggest = Math.max.apply(null, arrayNums);
  x = arrayNums.indexOf(biggest);
  arrayNums[x] = -Infinity;
  biggest = Math.max.apply(null, arrayNums);
}
console.log(biggest);
