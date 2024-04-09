#!/usr/bin/node
function add(a, b) {
  return a + b;
}

const numbers = process.argv;
const n1 = +numbers[2];
const n2 = +numbers[3];

console.log(add(n1, n2));
