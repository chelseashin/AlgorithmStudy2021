// 줄세우기
// 길라잡이 6-2. 다이나믹 프로그래밍 (2) D

// 30분
// LIS알고리즘 사용

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);

const input = ['7','3','7','5','2','6','1','4',''].map(Number);
input.pop();

const solve = (input) => {
  const N = input.shift();
  const dp = new Array(N).fill(1);

  for(let i = 0; i < N; i++) {
    for(let j = 0; j < i; j++) {
      if(input[j] < input[i]) {
        dp[i] = Math.max(dp[i], dp[j]+1);
      }
    }
  }

  const max = Math.max(...dp);
  console.log(N - max);
}

solve(input);