#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (const i of list) {
    if (i === searchElement) {
      occ = occ + 1;
    }
  }

  return occ;
};
