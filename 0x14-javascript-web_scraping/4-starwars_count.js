#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;
const url = argv[2] + '/?format=json';

let numMovies = 0;
request(url, { json: true }, (error, res, body) => {
  if (error) throw error;
  const results = body.results;
  results.forEach((result, index, resultsArr) => {
    result.characters.forEach((charUrl, index, charUrls) => {
      if (charUrl.search('/18/') !== -1) {
        numMovies += 1;
      }
    });
  });
  console.log(numMovies);
});
