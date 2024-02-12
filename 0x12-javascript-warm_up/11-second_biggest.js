#!/usr/bin/node

function findMax (num) {
  let index = 0;
  for (let i = 0; i < num.length; i++) {
    if (parseInt(num[i]) > parseInt(num[index])) {
      index = i;
    }
  }
  return index;
}

const first = process.argv.slice(2);
const index = findMax(process.argv.slice(2));
first.splice(index, 1);
console.log(first[findMax(first)]);
