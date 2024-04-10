#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let y = 0; y < this.width; y++) {
        output += 'X';
      }
      console.log(output);
    }
  }
}

module.exports = Rectangle;
