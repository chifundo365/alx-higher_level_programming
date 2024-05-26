#!/usr/bin/node
const readFile = require('fs').readFile;
const argv = require('process').argv;

readFile(argv[2], 'utf8', function (error, data) {
  if (error) throw error;
  console.log(data);
});
