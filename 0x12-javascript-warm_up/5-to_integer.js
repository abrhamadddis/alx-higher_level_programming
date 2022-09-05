#!/usr/bin/node

const argv = process.argv;
let argv1;

if (argv[2]) {
  if (!isNaN(parseInt(argv[2]))) {
    argv1 = parseInt(argv[2]);
    console.log('My number:', argv1);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
