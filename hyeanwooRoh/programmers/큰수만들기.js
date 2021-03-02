// 1시간 8분 + 1시간 36분
// 계속 같은 방식으로 시도하다가 실패
// 스택을 써서 통과

function solution(number, k) {
  const answer = [];

  for (const num of number) {
    while (answer.length !== 0 && answer[answer.length - 1] < num && k > 0) {
      answer.pop();
      k--;
    }
    answer.push(num);
  }

  return answer.splice(0,number.length - k).join('');
}

console.log(solution('1924', 2));
console.log(solution('54321', 2));
console.log(solution('4177252841', 4));
