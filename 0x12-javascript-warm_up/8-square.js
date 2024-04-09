#!/usr/bin/node
const size = +(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else if (size) {
  for (let i = 0; i < size; i++) {
    let output = '';
    for (let x = 0; x < size; x++) {
      output += 'X';
    }
    console.log(output);
  }
}
