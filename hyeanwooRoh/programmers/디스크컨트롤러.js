
// 27분
// 문제내 제한사항에서 마지막 항목은 체크되지않고 있음

// 정렬을 할때 기준을 찾지못해서 방황하다가
// 단순하게 생각해보기로 하고 풀었더니 한번에 풀림
// 배열에서 요소를 삭제할때는 splice()를 쓰자

function solution(jobs) {
  jobs.sort((a,b) => a[1] - b[1]);

  let curTime = 0;
  let totalTime = 0;
  let cnt = jobs.length;
  while(jobs.length > 0) {
    const idx = jobs.findIndex(e => e[0] <= curTime);
    if(idx === -1) {
      curTime++;
    } else {
      const [stime, etime] = jobs[idx];
      curTime += etime;
      totalTime += curTime - stime;
      jobs.splice(idx, 1);
    }
  }

  return parseInt(totalTime / cnt);
}

const jobs = [[0, 3], [1, 9], [2, 6]];

console.log(solution(jobs));