// 10분
// 매번 정렬할 경우 시간초과가 날 수도 있다
// 다음번에는 정렬을 하지않고 Math.max, Math.min을 사용해보자

function solution(operations) {
  const pq = [];

  for(const op of operations) {
    const [command, num] = op.split(' ');

    if(command === 'I') {
      pq.push(Number(num));
      pq.sort((a,b) => a - b);
    } else {
      if(pq.length === 0) continue;

      if(num === '1') {
        pq.pop();
      } else {
        pq.shift();
      }
    }
  }

  if(pq.length > 0) {
    return [pq[pq.length-1], pq[0]];
  } else {
    return [0,0];
  }
}

// const operations = ['I 16','D 1'];
// const operations = ['I 7','I 5','I -5','D -1'];
const operations = ['I 10000', 'D -1', 'I 4', 'I 3', 'I 2', 'I 1'];

console.log(solution(operations));