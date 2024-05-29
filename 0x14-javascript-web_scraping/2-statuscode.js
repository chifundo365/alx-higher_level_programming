#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

request(argv[2], (error, res, body) => {
  if (error) throw error;
  console.log('code:', res.statusCode);
});
