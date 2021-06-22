function solution(orders, course) {
  const answer = [];
  let cuisine;

  for (const c in course) {
    cuisine = {};
    for (const o in orders) {
      setCuisine(cuisine, orders[o], course[c]);
    }
    console.log(cuisine);
    answer.push(...getMaxValue(cuisine));
  }

  return answer.sort();
}

function setCuisine(cuisine, order, c) {
  if (order.length < c) return;

  comb(cuisine, order, [], 0, order.length, c, 0);
}

function comb(cuisine, order, arr, idx, n, r, target) {
  if (r == 0) {
    const str = arr.slice().sort().join("");
    cuisine[str] = cuisine[str] ? cuisine[str] + 1 : 1;
  } else if (target == n) {
    return;
  } else {
    arr[idx] = order[target];
    comb(cuisine, order, arr, idx + 1, n, r - 1, target + 1);
    comb(cuisine, order, arr, idx, n, r, target + 1);
  }
}

function getMaxValue(cuisine) {
  const max = Math.max(...Object.values(cuisine));
  if (max === 1) return [];

  const arr = [];
  for (const key of Object.keys(cuisine)) {
    if (cuisine[key] === max) arr.push(key);
  }
  return arr;
}

console.log(
  solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
);
// ["AC", "ACDE", "BCFG", "CDE"];
console.log(
  solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
);
//	["ACD", "AD", "ADE", "CD", "XYZ"]
console.log(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]));
//	["WX", "XY"]
