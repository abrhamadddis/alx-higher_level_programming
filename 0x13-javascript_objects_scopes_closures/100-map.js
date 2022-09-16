#!/usr/bin/node
const original = require('./100-data').list;
console.log(original);
const newList = original.map((x, index) => x * index);
console.log(newList);
