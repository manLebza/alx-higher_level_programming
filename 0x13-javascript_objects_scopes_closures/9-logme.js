#!/usr/bin/node
let narg = 0;
exportd.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
