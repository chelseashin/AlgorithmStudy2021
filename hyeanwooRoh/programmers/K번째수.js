// 10분
// sort함수에 조건을 넣어주지않을 경우 틀리는 문제가 있었다
// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
// sort()에 compareFuntion이 제공되지않으면 요소를 문자열로 변환하여 유니코드를 기준으로 정렬한다

function solution(array, commands) {
  const answer = [];
  
  for(const c of commands) {
      const tmp = array.slice(c[0]-1, c[1]).sort((a,b)=> a-b)[c[2]-1];
      answer.push(tmp);
  }
  
  return answer;
}

const array = [1, 5, 2, 6, 3, 7, 4];
const commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]];

console.log(solution(array, commands));