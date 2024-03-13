#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let indx = 0; indx < x; indx++) {
    theFunction();
  }
};
