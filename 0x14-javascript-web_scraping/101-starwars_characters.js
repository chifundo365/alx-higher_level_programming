#!/usr/bin/node
const request = require('request');
const movieId = require('process').argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, { json: true }, (error, res, body) => {
  if (error) throw error;
  printChars(body.characters, 0);
});

function printChars (array, index) {
  request(array[index], (error, res, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    if (index + 1 < array.length) printChars(array, index + 1);
  });
}
