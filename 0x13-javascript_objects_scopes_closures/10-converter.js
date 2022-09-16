#!/usr/bin/node
exports.converter = function (base) {
  return function baseC (a) {
    return a.toString(base);
  };
};
