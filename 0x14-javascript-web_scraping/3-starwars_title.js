#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2] + '/?format=json';

request(url, { json: true }, (error, res, body) => {
  if (error) throw error;
  console.log(body.title);
});
