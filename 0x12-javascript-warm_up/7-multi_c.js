#!/usr/bin/node

console.log(isNaN(parseInt(process.argv[2])) ? 'Missing number of occurrences' : 'C is fun\n'.repeat(parseInt(process.argv[2]) - 1) + 'C is fun');
