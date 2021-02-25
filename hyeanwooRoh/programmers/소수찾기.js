// 1시간 3분
// 시작할때 소수배열을 만들었다가 시간이 오래 걸려 지웠다
// 풀다가 보니 소수확인을 하는게 더 오래 걸릴 것 같아 다시 복구했다
// 별개로 점심을 먹고난 후라 그런지 집중이 잘 안되었다

// 다음번에는 중복체크로 Set()을 써보자

let hasMaked = new Array(10000000);
let primes = new Array(5000000);
let answer = 0;

function solution(numbers) {
  setPrime();

  let isUsed = new Array(numbers.length).fill(false);
  let numArr = [];
  for(let i = 0; i < numbers.length; i++) {
    numArr.push(parseInt(numbers[i]))
  }

  for(let i = 1; i <= numArr.length; i++) {
    dfs(numArr, isUsed, '', i, 0);
  }

  return answer;
}

function dfs(numArr, isUsed, str, depth, curDepth) {
  if(depth === curDepth) {
    let num = parseInt(str);
    if(!hasMaked[num]) {
      hasMaked[num] = true;
      if(primes[num]) {
        // console.log(num);
        answer++;
      }
    }

    return ;
  }

  for(let i = 0; i < numArr.length; i++) {
    if(isUsed[i] === true) continue;
    
    str += numArr[i];
    isUsed[i] = true;
    dfs(numArr, isUsed, str, depth, curDepth+1);
    isUsed[i] = false;
    str = str.slice(0,str.length-1)
  }
}

function setPrime() {
  for (let i = 2; i < primes.length; i++) {
    if(primes[i] === false) {
      continue;
    } else {
      primes[i] = true;
    }
    for (let j = i*2; j < primes.length;j += i) {
      primes[j] = false;
    }
  }
}

console.log(solution('1234567'));