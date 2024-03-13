#!/usr/bin/node
class Rectangle {
  constructor (a, b) {
    if ((a > 0) && (b > 0)) {
      this.width = a;
      this.height = b;
    }
  }

  print () {
    for (let indx = 0; indx < this.height; indx++) {
      let x = '';
      for (let indx1 = 0; indx1 < this.width; indx1++) {
        x += 'X';
      }
      console.log(x);
    }
  }
}

module.exports = Rectangle;
