#!/usr/bin/node
exports.esrever = function (list) {
  let leng = list.length - 1;
  let indx = 0;
  while ((leng - indx) > 0) {
    const auX = list[leng];
    list[leng] = list[indx];
    list[indx] = auX;
    indx++;
    leng--;
  }
  return list;
};
