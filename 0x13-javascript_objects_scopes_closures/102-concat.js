#!/usr/bin/node

const filesystem = require('fs');
filesystem.writeFileSync(process.argv[4], filesystem.readFileSync(process.argv[2], 'utf8') + filesystem.readFileSync(process.argv[3], 'utf8'));
