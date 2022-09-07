#!/usr/bin/node

function factorial (a) {
  if (a > 0) {
    return (a * factorial(a - 1));
  }
  return (1);
}

console.log(factorial(parseInt(process.argv[2])));
