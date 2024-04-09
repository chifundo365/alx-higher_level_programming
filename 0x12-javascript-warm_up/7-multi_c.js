#!/usr/bin/node
const msg = 'C is fun';
const number = +(process.argv[2]);

if (isNaN(number) || number === undefined) {
  console.log('Missing number of occurrences');
} else if (number >= 1) {
  for (let i = 0; i < number; i++) {
    console.log(msg);
  }
}
