#!/usr/bin/node
const argv = require('process').argv;
const writeFile = require('fs').writeFile;

writeFile(argv[2], argv[3], 'utf8', (error) => {
  if (error) throw error;
});
