#!/usr/bin/node
const argv = process.argv;
let input;
if (!isNaN(parseInt(argv[2])) === true) {
  input = argv[2];
  for (let i = 0; i <= input; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
