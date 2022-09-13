#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let a = list.length - 1; a >= 0; a--) {
    newList.push(list[a]);
  }
  return newList;
};
