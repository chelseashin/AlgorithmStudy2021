// 인구이동

// 1시간 14분
// bfs로 나라 탐색
// 구현 자체는 쉬운편이었고 중간에 인덱스 실수가 있었던 것 빼면 금방 풀었다

// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const log = console.log;
const input = ['2 20 50','50 30','20 40',''];
// const input = ['2 40 50','50 30','20 40',''];
// const input = ['2 20 50','50 30','20 40',''];
input.pop();

const di = [0,0,1,-1];
const dj = [1,-1,0,0];

const solve = (input) => {
  const [N, L, R] = input.shift().split(' ').map(Number);
  const map = input.map(n => n.split(' ').map(s => Number(s)));
  
  const isVisit = [];
  for(let i = 0; i < N; i++) {
    isVisit.push([]);
    for(let j = 0; j < N; j++) {
      isVisit[i].push(false);
    }
  }

  const initVisit = () => {
    for(let i = 0; i < N; i++) {
      for(let j = 0; j < N; j++) {
        isVisit[i][j] = false;
      }
    }
  }

  let isMoved = false;

  const bfs = (i, j) => {    
    const peoples = [];
    peoples.push([i,j]);
    let totalPopulation = map[i][j];

    const q = [];
    q.push([i,j,map[i][j]]);
    isVisit[i][j] = true;

    while(q.length > 0) {
      const tmp = q.shift();

      for(let d = 0; d < 4; d++) {
        const ti = tmp[0] + di[d];
        const tj = tmp[1] + dj[d];
        if (ti < N && ti >= 0 && tj < N && tj >= 0 && !isVisit[ti][tj]){
          const popDiff = Math.abs(map[ti][tj] - tmp[2]);
          if (popDiff >= L && popDiff <= R) {
            peoples.push([ti,tj])
            totalPopulation += map[ti][tj];
            q.push([ti,tj,map[ti][tj]]);
            isVisit[ti][tj] = true;
          }
        }
      }
    }

    if(peoples.length > 1) {
      const movedPopulation = parseInt(totalPopulation / peoples.length);
      for(const p of peoples) {
        map[p[0]][p[1]] = movedPopulation;
      }

      isMoved = true;
    }
  };

  const openBorderLine = () => {
    isMoved = false;
    for(let i = 0; i < N; i++) {
      for(let j = 0; j < N; j++) {
        if(!isVisit[i][j]) {
          bfs(i,j);
        }
      }
    }
  }
  
  for(let i = 0; i < 2000; i++) {
    openBorderLine();
    initVisit();
    if(!isMoved) {
      log(i);
      return;
    }
  }
};

solve(input);