const maxLen = 1000;
const input_t = initT(maxLen);
const input_r = initR(maxLen);

function initT(maxLen) {
  const arr = [];
  for (let i = 0; i < maxLen; i++) {
    arr[i] = parseInt(Math.random() * 10001);
  }
  return arr;

}
function initR(maxLen) {
  const arr = [];
  for (let i = 0; i < maxLen; i++) {
    arr[i] = parseInt(Math.random() * 6);
  }
  return arr;
}

const st = + new Date();
console.log(solution(input_t, input_r))
const et = + new Date();
console.log(et - st +'ms');

function solution(t, r) {
  const answer = [];
  const guest = t.map((time, idx) => ({idx, time}));
  guest.sort((a,b) => b.time - a.time);

  for (let time = 0; time <= 10000; time++) {
    const tmpGuest = [];
    tmpGuest.push(guest.pop());

    let j = guest.length - 1;
    while (j >= 0 && guest[j].time <= time) {
      tmpGuest.push(guest.pop());
      j--;
    }
  
    if (tmpGuest[0] === undefined) break;

    tmpGuest.sort((a,b) => {
      if (r[a.idx] > r[b.idx]) {
        return 1;
      } else if (r[a.idx] === r[b.idx]) {
        return a.time - b.time;
      } else {
        return -1;
      }
    })

    answer.push(tmpGuest[0].idx);

    guest.push(...tmpGuest.splice(1))
  }
  return answer;
}

// console.log(solution([0,1,3,0], [0,1,2,3]));
// console.log(solution([7,6,8,1], [0,1,2,3]));