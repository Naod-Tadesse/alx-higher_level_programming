#!/usr/bin/node

function addMeMaybe (num, fun) {
  fun(num + 1);
}

module.exports = { addMeMaybe };
