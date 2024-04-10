#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let noc = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      noc += 1;
    }
  }

  return (noc);
};
