#!/usr/bin/node
const list = require('./100-data').list;

const ln = list.map((t, i) => t * i);

console.log(list);
console.log(ln);
