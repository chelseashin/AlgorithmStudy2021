// 1, 2, 3 더하기
// 길라잡이 2-1. 백트래킹 (1) C

// 19분
// DFS로 푸는 방법뿐만 아니라 DP로 푸는 방법도 있었다

// 1. 자바스크립트에서 문자열을 숫자로 변환하는 방법은 많이 존재한다
// --> Number(str), parseInt(str), parseFloat(str), str << 0, +str, str*1, str-0 등등
// --> 가장 빠른건 str*1 (*브라우저 환경에 따라 다를 수 있음)
// 참고: http://phrogz.net/js/string_to_number.html
// 2. 이과정에서 Array.push()와 Array[n] = value 가 속도차이가 난다는 걸 알았다
// 일반적으로 Array[n] = value가 조금 더 빠르며, 이는 자바스크립트 내부구조에 의한 것이라고 한다
// 참고: https://stackoverflow.com/questions/614126/why-is-array-push-sometimes-faster-than-arrayn-value

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = '10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'.trim().split('\n');
const addNum = [3,2,1];
let totalCnt = 0;

const dfs = (n, sum) => {
  if (n < sum) return;

  if (n === sum) {
    totalCnt++;
    return;
  }

  for(const a of addNum) {
    if (sum + a <= n) {
      dfs(n, sum + a);
    }
  }
}

const solve = (data) => {
  const numArr = data.splice(1).map(Number);
  const answer =  [];

  for(const n of numArr) {
    totalCnt = 0;
    dfs(n, 0);
    answer.push(totalCnt);
  }

  console.log(answer.join('\n'));
}

const input = '10\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'.trim().split('\n').map(v => v*1);

const solve2 = () => {
  const dp = [0,1,2,4];

  const max = input.reduce((acc, cur) => acc < cur ? cur : acc, 0);
  for (let i = 4; i <= max; i++) {
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
  }

  for (let i = 1; i < input.length; i++) {
    console.log(dp[input[i]]);
  }
}

solve2(input);
