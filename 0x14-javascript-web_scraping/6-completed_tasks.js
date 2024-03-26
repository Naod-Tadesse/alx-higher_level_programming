#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todosdone = JSON.parse(body);
  const tasksByUser = {};

  todosdone.forEach(todo => {
    if (todo.completed) {
      if (!tasksByUser[todo.userId]) {
        tasksByUser[todo.userId] = 1;
      } else {
        tasksByUser[todo.userId]++;
      }
    }
  });

  console.log(tasksByUser);
});
