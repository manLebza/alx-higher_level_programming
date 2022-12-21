#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let k = 0; k < this.width; k++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}
module.exports = Rectangle;
