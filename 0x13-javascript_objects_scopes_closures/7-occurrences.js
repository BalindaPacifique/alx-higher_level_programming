#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrence = 0;
  for (let indx = 0; indx < list.length; indx++) {
    if (searchElement === list[indx]) {
      nOccurrence++;
    }
  }
  return nOccurrence;
};
