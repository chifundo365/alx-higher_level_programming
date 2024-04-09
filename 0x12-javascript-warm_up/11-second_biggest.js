#!/usr/bin/node
const numbers = process.argv;

if (numbers.length === 2 || numbers.length === 3) {
  console.log(0);
} else {
  let biggest = numbers[2];
  for (let i = 2; i < numbers.length; i++) {
    const number = +numbers[i];
    if (number > biggest) {
      biggest = number;
    }
  }
  let secondBiggest = +numbers[2];
  for (let x = 2; x < numbers.length; x++) {
    const number = +numbers[x];
    if (number !== biggest && ((biggest - number) < (biggest - secondBiggest)) && numbers.length > 4) {
      secondBiggest = number;
    } else if (numbers.length === 4) {
      secondBiggest = numbers[3] > numbers[4] ? numbers[4] : numbers[3];
    }
  }
  console.log(secondBiggest);
}
