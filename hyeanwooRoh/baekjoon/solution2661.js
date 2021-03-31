// 좋은수열

// 2시간 59분
// 백트래킹으로 하려다가 터질것 같아 백트래킹+그리디로 풀어봤지만 틀렸다
// 백트래킹으로 풀어보니 성공

// const input = require('fs').readFileSync('/dev/stdin').toString()*1;

const input = '7\n'*1;

let hasPrinted = false;

const checkString = (str) => {
  const len = str.length;
  let start = len - 1;

  for (let i = 1; i <= len/2; i++) {
    if (str.substring(start-i, len-i) === str.substring(start, len)) {
      return false;
    }
    start--;
  }
  return true;
}

const solve = (depth, answer) => {
  if (hasPrinted) return;

  if (depth === input) {
    hasPrinted = true;
    console.log(answer);
    return;
  }

  for (let i = 1; i <= 3; i++) {
    if (checkString(answer+i))
      solve(depth+1, answer+i);
  }
}

solve(1, '1');