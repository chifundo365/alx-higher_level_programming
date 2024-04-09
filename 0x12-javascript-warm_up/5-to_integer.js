#!/usr/bin/node
let number = process.argv
number = +(number[2]);
if (isNaN(number)) {
  console.log('Not number');
} else {
  console.log('My number: ' + number);
}
