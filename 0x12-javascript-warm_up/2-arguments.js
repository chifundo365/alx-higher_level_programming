#!/usr/bin/node
const argvLen = process.argv.length;
if (argvLen >= 4) {
  console.log('Arguments found');
} else if (argvLen === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
