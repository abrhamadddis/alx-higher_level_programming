#!/usr/bin/node
// a script that read and print the conteint of a file
const Put = process.argv[2];
const fs = require('fs');
fs.readFile(Put, 'utf8', function (err, data) {
  if (err) throw err;
  console.log(data.toString);
});
