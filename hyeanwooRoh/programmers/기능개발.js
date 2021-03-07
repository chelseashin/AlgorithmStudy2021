// 24분
// 쉬웠음
// 얼마나 걸리는지는 방정식으로 구하고 나머지는 그냥 단순비교

const progresses = [93, 30, 55];
const speeds = [1, 30, 5];

function solution(progresses, speeds) {
  let answer = [];
  let days = progresses.map((item, idx) => Math.ceil((100 - item)/speeds[idx]));
  
  for (let i = 0; i < days.length;) {
    let tmp = 1;
    for (let j = i+1; j < days.length; j++) {
      if(days[i] < days[j]) break;
      tmp++;
    }
    answer.push(tmp);
    if(tmp > 1) {
      i += tmp;
    } else {
      i++
    }
  }

  return answer;
}

console.log(solution(progresses, speeds))