#!/usr/bin/node

exports.converter = function (base) {
  return function (k) {
    const l = k.toString(base);
    return l;
  };
};
