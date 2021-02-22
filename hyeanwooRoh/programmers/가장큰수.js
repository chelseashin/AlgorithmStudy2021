// 1시간
// 문제가 너무 어렵다고 생각해서 40분동안 어렵게 어렵게 compare()함수를 짰다
// 각 자릿수별로 비교하는 함수였고 숫자 중간에 0이 들어가면 잘못된 결과가 나오기때문에 틀렸다
// 반례를 살펴보고 포기할까 고민하다가 다른 방법이 떠올랐다
// 단순하게 두숫자를 합친 2가지 방법을 비교해서 정렬하는 방식이었는데 답이 맞았다
// 2번째 방법은 20분 걸렸다

function solution(numbers) {
  // let answer = numbers.sort(compare);
  numbers.sort(compare2);
  if(isOnlyZero(numbers)) return '0';
  return numbers.join('');
}

function compare(a, b) { 
  let strA = a+'';
  let strB = b+'';

  if(strA.length === strB.length) return a-b;

  let len = Math.max(strA.length, strB.length);
  let idxA = 0;
  let idxB = 0;
  for(let i = 0; i < len; i++) {
    if(parseInt(strA[idxA]) > parseInt(strB[idxB])) {
      return -1;
    } else if(parseInt(strA[idxA]) < parseInt(strB[idxB])){
      return 1;
    } else {
      idxA = Math.min(strA.length - 1, idxA+1);
      idxB = Math.min(strB.length - 1, idxB+1);
    }
  }
}

function isOnlyZero(numbers) {
  for(const num of numbers) {
    if(num !== 0) return false;
  }
  return true;
}

function compare2(a, b) { 
  let ab = parseInt(''+a+b);
  let ba = parseInt(''+b+a);

  return ba - ab;
}

// const input = [6, 10, 2];
// const input = [3, 30, 34, 5, 9];
// const input = [0, 5, 10, 15, 20]
// const input = [1000, 0, 5, 99, 100]
const input = [0, 0, 0, 0, 0]
// const input = [403, 40]

console.log(solution(input))