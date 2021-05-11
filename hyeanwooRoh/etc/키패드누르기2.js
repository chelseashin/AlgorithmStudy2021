// 20분

const numberHand = ['T','L','T','R','L','T','R','L','T','R'];
const keypad = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]];

function solution(numbers, hand) {
  let answer = '';

  let idxL = keypad[10];
  let idxR = keypad[11];
  for (const num of numbers) {
    if (numberHand[num] === 'T') {
      let tmpHand = getHand(num, hand, idxL, idxR);
      answer += tmpHand;
      if (tmpHand === 'L') {
        idxL = keypad[num];
      } else {
        idxR = keypad[num];
      }
    } else {
      answer += numberHand[num];
      if (numberHand[num] === 'L') {
        idxL = keypad[num];
      } else {
        idxR = keypad[num];
      }
    }
  }

  return answer;
}

function getHand(num, hand, idxL, idxR) {
  let [kr, kc] = keypad[num];
  let lenL = Math.abs(kr - idxL[0]) + Math.abs(kc - idxL[1]);
  let lenR = Math.abs(kr - idxR[0]) + Math.abs(kc - idxR[1]);

  if (lenL < lenR) {
    return 'L';
  } else if (lenL > lenR) {
    return 'R'
  } else {
    return hand === 'right' ? 'R' : 'L';
  }
}