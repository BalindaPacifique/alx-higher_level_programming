#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let indx = 0; indx < this.height; indx++) {
      let x = '';
      for (let indx1 = 0; indx1 < this.width; indx1++) {
        x += c;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
