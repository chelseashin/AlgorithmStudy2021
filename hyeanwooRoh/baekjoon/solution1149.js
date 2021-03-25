// RGB 거리
// 58분

// 1년 반쯤전에 풀었다고 되있는데 아마 답을 보고 푼 것 같다
// 이번에는 dp라는 것만 알고 30분정도 고민하다가 푸는 방법을 찾았다

// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// const input = ['3','26 40 83','49 60 57','13 89 99'];
// const input = ['3','1 20 30','50 5 6','9 3 7'];
const input = ['2','100 1 100','999 1 999'];

const INF = 1001;

function solve() {
  const N = input.splice(0,1) * 1;
  const house = input.map(v => v.split(' ').map(s => s*1));
  
  const sum = house.map(() => [0,0,0]);

  for (let i = 0; i < 3; ++i) {
    sum[0][i] = house[0][i]; 
  }

  for (let i = 1; i < N; ++i) {
    sum[i][0] = house[i][0] + Math.min(sum[i-1][1],sum[i-1][2]);
    sum[i][1] = house[i][1] + Math.min(sum[i-1][0],sum[i-1][2]);
    sum[i][2] = house[i][2] + Math.min(sum[i-1][1],sum[i-1][0]);
  }

  console.log(Math.min(...sum[N-1]));
}

// solve();

function solve2() {
  const N = input.splice(0,1) * 1;
  const house = input.map(v => v.split(' ').map(s => s*1));

  for (let i = 1; i < N; ++i) {
    house[i][0] += Math.min(house[i-1][1],house[i-1][2]);
    house[i][1] += Math.min(house[i-1][0],house[i-1][2]);
    house[i][2] += Math.min(house[i-1][1],house[i-1][0]);
  }

  console.log(Math.min(...house[N-1]));
}

solve2();
