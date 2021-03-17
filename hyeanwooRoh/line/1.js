// 00:00:00 ~ 00:13:30 13분

const boxeses = [[[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]], [[1, 2], [3, 4], [5, 6]], [[1, 2], [2, 3], [3, 1]]];

function solve(boxes) {
  const products = [];
  // boxes 초기화
  for (const [n1, n2] of boxes) {
    products[n1] = products[n1] ? products[n1] + 1 : 1;
    products[n2] = products[n2] ? products[n2] + 1 : 1;
  }

  let duoProductCnt = 0;
  for (let i = 1; i < products.length; i++) {
    if (products[i] === 2) {
      duoProductCnt++;
    }
  }

  return boxes.length - duoProductCnt;
}

for (const boxes of boxeses) {
  console.log(solve(boxes));
}
