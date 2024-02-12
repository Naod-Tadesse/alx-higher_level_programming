#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let p = '';
    for (let k = 0; k < num; k++) {
      p += 'X';
    }
    console.log(p);
  }
}
