// 1시간 30분
// 그리디 분류인데 그리디로 풀리지않는다
// 참고: https://programmers.co.kr/questions/10979

const alphabetCnt = {
  A:0,
  B:1,
  C:2,
  D:3,
  E:4,
  F:5,
  G:6,
  H:7,
  I:8,
  J:9,
  K:10,
  L:11,
  M:12,
  N:13,
  O:12,
  P:11,
  Q:10,
  R:9,
  S:8,
  T:7,
  U:6,
  V:5,
  W:4,
  X:3,
  Y:2,
  Z:1,
}

const RIGHT = 'R';
const LEFT = 'L'

const replaceAt = (str, idx) => str.substr(0,idx) + 'A' + str.substr(idx+1);
const log = console.log;

function solution(name) {
  let answer = alphabetCnt[name[0]];
  let moveDir = RIGHT;
  let changeCnt = answer === 0 ? 0 : -1;
  for (const n of name) {
    if (n !== 'A') changeCnt++;
  }

  function checkBothSideA(idx, prevDir) {
    // check left
    let idxL = idx === 0 ? name.length : idx - 1;
    let leftACnt = 0;
    while (name[idxL] === 'A') {
      leftACnt++;
      idxL = idxL === 0 ? name.length - 1 : idxL - 1;
    }
    // check right
    let idxR = idx === name.length - 1? 0 : idx + 1;
    let rightACnt = 0;
    while (name[idxR] === 'A') {
      rightACnt++;
      idxR = idxR === name.length ? 0 : idxR + 1;
    }

    if (leftACnt < rightACnt) {
      return [leftACnt+1, LEFT];
    } else if (leftACnt > rightACnt) {
      return [rightACnt+1, RIGHT];
    } else {
      // 양쪽이 같은 경우 name길이의 반까지 탐색하여 A갯수로 결정
      let tmpCnt = prevDir === RIGHT ? rightACnt : leftACnt;
      return [tmpCnt+1, prevDir];
    }
  }

  let curAlphabetIdx = 0;
  while (changeCnt > 0) {
    log('main start')
    let [tmpIdx, tmpDir] = checkBothSideA(curAlphabetIdx, moveDir);
    log('tmps', tmpIdx, tmpDir);
    answer += tmpIdx;
    log('\nanswer:', answer)
    moveDir = tmpDir;
    curAlphabetIdx = moveDir === RIGHT ? 
      (curAlphabetIdx + tmpIdx) % name.length :
      (curAlphabetIdx - tmpIdx + name.length) % name.length;
    answer += alphabetCnt[name[curAlphabetIdx]];

    log('answer:', answer)
    log('current:',curAlphabetIdx,name[curAlphabetIdx])
    // 체크후에 A로 바꿔주기
    name = replaceAt(name, curAlphabetIdx);
    changeCnt--;
    log('\nmain end\n')
  }

  return answer;
}

// console.log(solution("JEROEN"));      // 56
// console.log(solution("JAN"));         // 23
// console.log(solution("AAAKAAAAAR"));  // 24
// console.log(solution("AABAQAAAAAN"))  // 30
console.log(solution("BBBBAAAAAB"))  // 10
// console.log(solution("BBBBAAAABA"))  // 12


// function solution(name) {
//   let moveCntR = alphabetCnt[name[0]];
//   let moveCntL = alphabetCnt[name[0]];

//   let moveDir = 'left' || 'right';
//   let leftACnt = 0;
//   let rightACnt = 0;

//   // move to right
//   for (let i = 1; i < name.length; i++) {
//     moveCntR++;

//     if (i === name.length -1 && alphabetCnt[name[i]] === 0) {
//       moveCntR--;
//       break;
//     }

//     moveCntR += alphabetCnt[name[i]]
//   }

//   // move to left
//   for (let i = name.length - 1; i > 0; i--) {
//     moveCntL++;

//     if (i === 1 && alphabetCnt[name[i]] === 0) {
//       moveCntL--;
//       break;
//     }

//     moveCntL += alphabetCnt[name[i]]
//   }

//   return Math.min(moveCntR, moveCntL);
// }