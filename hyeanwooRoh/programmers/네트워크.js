// 19분

function solution(n, computers) {
  let answer = 0;
  const visit = new Array(n).fill(false);

  function bfs(com) {
    const q = [com];
    visit[com] = true;

    while (q.length !== 0) {
      const tmp = q.shift();
      computers[tmp].forEach((c, idx) => {
        if (c === 1 && !visit[idx]) {
          q.push(idx);
          visit[idx] = true;
        }
      })
    }
  }

  for (let i = 0; i < n; i++) {
    if (!visit[i]) {
      bfs(i);
      answer++;
    }
  }
  
  return answer;
}

console.log(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]));
console.log(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]));