#!/usr/bin/node
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
const c1 = parseInt(process.argv[2]);
const c2 = parseInt(process.argv[3]);
add(c1, c2);
