// 56분
// 월간 코드챌린지때 풀어본적이 있는 문제였다
// 그때는 방법만 생각하다가 복잡할것같아 포기했었는데 이번에는 2차원배열로 하면 될것같아 바로 해주었다
// 다만 while문을 돌리는 과정에서 살짝 에러가 나서 시간을 조금 더 잡아먹었다 공부가 조금 더 필요하다
// --> java와 다르게 javascript에서 while문은, 안에 조건이 2개 이상이고 &&으로 묶은 경우라도 전부 탐색하는것 같다

function solution(n) {
  let answer = [];
  let snail = [];
  for(let r = 0; r < n; r++) {
    snail[r] = [];
    for(let c = 0; c < n; c++) {
      snail[r][c] = 0;
    }
  }

  let len = n;
  let num = 1;
  let [i, j, k] = [0, 0, 0];

  while(len > 0) {
    // down
    for(k = 0; k < len; k++) {
      snail[i++][j] = num++;
    }
    i--;
    len--;
    // right
    for(k = 0; k < len; k++) {
      snail[i][++j] = num++;
    }
    len--;
    // up
    for(k= 0; k < len; k++) {
      snail[--i][--j] = num++;
    }
    i++;
    len--;
  }

  for(let r = 0; r < n; r++) {
    for(let c = 0; c < n; c++) {
      if(snail[r][c] === 0) break;
      answer.push(snail[r][c]);
    }
  }

  return answer;
}

console.log(solution(4));