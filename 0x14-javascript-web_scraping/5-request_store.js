#!/usr/bin/node
const writeFile = require('fs').writeFile;
const request = require('request');
const url = require('process').argv[2];
const filename = require('process').argv[3];

request(url, (error, res, body) => {
  if (error) throw error;
  writeFile(filename, body, 'utf8', (error) => {
    if (error) throw error;
  });
});
