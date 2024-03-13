#!/usr/bin/node
let nargs = 0;

exports.logMe = function (i) {
  console.log(nargs + ': ' + i);
  nargs++;
};
