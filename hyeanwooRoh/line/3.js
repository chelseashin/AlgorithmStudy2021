// 00:30:50 ~ 00:52:10 22분

// 1123456789
// 100000

const nums = [73425, 10007, 9, 1123456789];

function solve(n) {
  const toStringNum = '' + n;
  let minCnt = 123456789;
  let answer = 0;

  function dfs(depth, str) {
    if (depth > minCnt) return;

    if (str.length === 1) { // 숫자가 전부 합쳐지면 체크
      if (minCnt > depth) {
        minCnt = depth;
        answer = str * 1;
      }
      return;
    }
    
    for (let i = 0; i < str.length - 1; i++) {
      const leftNum = str.substring(0,i+1);
      const rightNum = str.substring(i+1);
      if (rightNum.charAt(0) === '0' && rightNum.length === 1) { // 오른쪽 숫자가 그냥 0만 있을때
        dfs(depth+1, leftNum);
      } else if (rightNum.charAt(0) !== '0') { // 오른쪽 숫자가 0으로 시작하지 않을때
        const tmpStr = leftNum*1 + rightNum*1;
        dfs(depth+1, ''+tmpStr);
      }
    }
  }

  dfs(0, toStringNum);

  return [minCnt, answer];
}

for (const n of nums) {
  console.log(solve(n));
}

// function dfs(depth, str) {
//   if (str.length === 1) {
//     if (minCnt > depth) {
//       minCnt = depth;
//       answer = str * 1;
//     }
//     return;
//   }
  
//   for (let i = 0; i < str.length - 1; i++) {
//     const leftNum = str.substring(0,i+1);
//     const rightNum = str.substring(i+1);
//     if (rightNum.charAt(0) !== '0') {
//       const tmpStr = leftNum*1 + rightNum*1;
//       dfs(depth+1, ''+tmpStr);
//     }
//   }
// }