// 20+30분
// 문제를 제대로 이해하지못하다가 참고링크를 보고 이해했다
// 참고링크: https://www.ibric.org/myboard/read.php?Board=news&id=270333
// 틀린거 같은데 왜 맞죠

function solution(citations) {
  citations.sort((a,b) => b - a);
  let answer = 0;
  for(let i = 0; i < citations.length; i++) {
    if(citations[i] <= answer) {
      break;
    } else {
      answer++;
    }
  }

  return answer;
}

// const citations = [3, 0, 6, 1, 5];
// const citations = [47,42,32,28,24,22,17,15,10,10,8];
// const citations = [31, 66];
// const citations = [0, 0, 0];
// const citations = [0, 1, 1];
// const citations = [12, 11, 10, 9, 8, 1] // 5
// const citations = [6, 6, 6, 6, 6, 1] // 5
// const citations = [4, 4, 4] // 3
// const citations = [4, 4, 4, 5, 0, 1, 2, 3] // 4
// const citations = [10, 11, 12, 13] // 4
// const citations = [3, 0, 6, 1, 5] // 3
// const citations = [0, 0, 1, 1] // 1
// const citations = [0, 1] // 1
const citations = [10, 9, 4, 1, 1] // 3
console.log(solution(citations))