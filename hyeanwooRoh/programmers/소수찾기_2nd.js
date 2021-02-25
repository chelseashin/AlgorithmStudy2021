// 45분
// 1번풀이와 다르게 Set사용
// * 1번째 풀이는 메모리도 148MB로 일정하고 
// * 시간도 120ms~150ms로 일정한 반면
// * 2번째 풀이는 특정 테스트케이스에서는 월등히 빨랐지만
// * 어떤 테스트케이스에서는 270MB에 700ms로 느린 경우가 보였다


const primes = [false, false];

function solution(numbers) {
  numbers = numbers.split('');
  setPrime(numbers.length);

  const numSet = new Set();
  const visit = new Array(numbers.length).fill(false);

  for (let i = 0; i < numbers.length; i++) {
    for (let j = 1; j <= numbers.length; j++) {
      visit[i] = true;
      permutation(numSet, numbers, visit, j, 1, numbers[i]);
      visit[i] = false;
    }
  }

  let cnt = 0;
  [...numSet].forEach(n => {
    if(primes[n]) cnt++;
  })

  return cnt;
}

function setPrime(len) {
  const arrLen = Math.pow(10, len) + 1;
  for (let i = 2; i < arrLen; i++) {
    primes.push(true);
  }

  for (let i = 2; i < primes.length; i++) {
    if(!primes[i]) continue;
    for (let j = i*2; j < primes.length;j += i) {
      primes[j] = false;
    }
  }
}

function permutation(numSet, numbers, visit, depth, currentDepth, num) {
  if (depth === currentDepth) {
    numSet.add(Number(num));
    return;
  }

  for (let i = 0; i < numbers.length; i++) {
    if (!visit[i]) {
      visit[i] = true;
      permutation(numSet, numbers, visit, depth, currentDepth+1, num+numbers[i]);
      visit[i] = false;
    }
  }
}

const input = '011';

console.log(solution(input));