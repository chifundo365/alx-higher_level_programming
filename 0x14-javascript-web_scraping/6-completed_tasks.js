#!/usr/bin/node
const request = require('request');
const url = require('process').argv[2];

request(url, { json: true }, (error, response, body) => {
  const obj = {};
  if (error) throw error;
  body.forEach((task, index, tasks) => {
    if (task.completed) {
      if (task.userId in obj) {
        obj[task.userId] = obj[task.userId] + 1;
      } else {
        obj[task.userId] = 1;
      }
    }
  });
  console.log(obj);
});
