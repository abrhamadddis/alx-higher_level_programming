#!/usr/bin/node
const argv = process.argv;
let input;
if (argv[2] && !isNaN(parseInt(argv[2])) === true) {
  input = parseInt(argv[2]);
  for (let i = 1; i <= input; i++) {
    console.log('X'.repeat(input));
  }
} else {
  console.log('Missing size');
}
