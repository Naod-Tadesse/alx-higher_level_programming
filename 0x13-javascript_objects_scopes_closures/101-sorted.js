#!/usr/bin/node
const dict = require('./101-data').dict;

const n = {};

for (const it in dict) {
  !n[dict[it]] ? (n[dict[it]] = [it]) : n[dict[it]].push(it);
}

console.log(n);
