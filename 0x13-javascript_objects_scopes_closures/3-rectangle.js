#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
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
