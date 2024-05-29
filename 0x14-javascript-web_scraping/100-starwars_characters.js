#!/usr/bin/node
const request = require('request');
const movieId = require('process').argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, { json: true }, (error, res, body) => {
  if (error) throw error;
  body.characters.forEach((charUrl, i, arr) => {
    request(charUrl, { json: true }, (error, res, body) => {
      if (error) throw error;
      console.log(body.name);
    });
  });
});
