// 00:13:30 ~ 00:30:50 17분
// 투포인트 알고리즘 활용

const balls = [[1, 2, 3, 4, 5, 6], [11, 2, 9, 13, 24]];
const orders = [[6, 2, 5, 1, 4, 3], [9, 2, 13, 24, 11]];

function solve(ball, order) {
  const isCalled = [];
  ball.forEach(v => { // 호출 배열 생성
    isCalled[v] = false;
  })

  // 포인터 2개
  let start = 0;
  let end = ball.length - 1;
  const answer = [];
  
  for (const o of order) {
    if (ball[start] === o) { // 공이 왼쪽에 있을 경우
      start++;
      answer.push(o);
      while (isCalled[ball[start]]) { // while문 돌면서 호출되었던 공 제거
        answer.push(ball[start]);
        isCalled[ball[start]] = false;
        start++;
      }
    } else if (ball[end] === o) { // 공이 오른쪽에 있을 경우
      end--;
      answer.push(o);
      while (isCalled[ball[end]]) { // while문 돌면서 호출되었던 공 제거
        answer.push(ball[end]);
        isCalled[ball[end]] = false;
        end--;
      }
    } else { // 공이 양쪽 끝에 없을 경우 호출해놓음
      isCalled[o] = true;
    }
  }

  return answer;
}

for (const idx in balls) {
  console.log(solve(balls[idx], orders[idx]));
}