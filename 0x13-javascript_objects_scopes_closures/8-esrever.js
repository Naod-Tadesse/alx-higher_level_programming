#!/usr/bin/node

exports.esrever = function (list) {
  const vr = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    vr[j] = list[i];
  }

  return vr;
};
