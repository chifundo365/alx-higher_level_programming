#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let output = '';
        for (let y = 0; y < this.height; y++) {
          output += 'C';
        }
        console.log(output);
      }
    }
  }
}

module.exports = Square;
