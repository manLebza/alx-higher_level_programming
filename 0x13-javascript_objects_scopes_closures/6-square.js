#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let k = 0; k < this.width; k++) {
        s += c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
