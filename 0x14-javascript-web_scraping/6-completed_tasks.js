#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId] = 1;
      } else {
        completedTasksByUser[todo.userId]++;
      }
    }
  });

  console.log(completedTasksByUser);
});
