#!/usr/bin/node
// a program that return the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element in list) {
    if (list[element] === searchElement) {
      count++;
    }
  }
  return count;
};
