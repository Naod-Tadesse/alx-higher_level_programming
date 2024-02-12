#!/usr/bin/node

function callMeMoby (num, fun) {
  for (let i = 0; i < num; i++) {
    fun();
  }
}

module.exports = { callMeMoby };
