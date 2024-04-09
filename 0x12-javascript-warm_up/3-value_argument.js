#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2) console.log('no argument');
if (argv.length >= 3) console.log(argv[2]);
