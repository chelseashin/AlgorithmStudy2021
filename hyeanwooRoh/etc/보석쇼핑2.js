// 보석구매 최적화
// 투포인터 알고리즘 사용
// 투포인터 알고리즘 자체는 DP랑 비슷한것 같다. DP를 단순화 시킨 느낌?
// 원래는 보석이 다 들어왔는지 체크하는 함수를 만들었지만 시간이 터져서 바꿈

// const gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"];
// const gems = ["DIA", "RUBY", "RUBY", "EMERALD", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"];
// const gems = ["DIA", "RUBY", "RUBY", "EMERALD", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "DIA", "SAPPHIRE", "EMERALD", "RUBY"];
// const gems = ["AA", "AB", "AC", "AA", "AC"];
// const gems = ["XYZ", "XYZ", "XYZ"];
// const gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"];

// 10만개 랜덤 입력변수 생성
const alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

const answerGems = [];
for(let i=0; i < 100; i++) {
  let str = [];
  for(let j=0; j < 10; j++) {
    let num = parseInt(Math.random()*26);
    str.push(alpabet[num]);
  }
  answerGems.push(str.join(''));
}

const gems = [];
for(let i=0; i < 100000; i++) {
  let idx = parseInt(Math.random()*answerGems.length);
  gems.push(answerGems[idx]);
}

console.log('calc start');

// 문제 풀이
function findMinSection(gems, answer) {
  let kindOfGems = [...new Set(gems)].length;
  let storeArr = [];
  let s = 0, e = 0, gemCnt = 0;

  while(true){
    if(storeArr.length > 0 && gems[e] === gems[s]) { // 맨 뒤 보석과 맨 앞이 중복될 경우
      storeArr.shift();
      s++;
      gemCnt--;
      while(storeArr.length > 1) {
        let tmp = storeArr.shift();
        if(storeArr.includes(tmp)){
          s++;
          continue;
        } else {
          storeArr.unshift(tmp);
          break;
        }
      }
    } else if(e === gems.length) { // 배열의 끝에 도착했을 경우
      break;
    } else { // 중복되지도 않고, 끝나지도 않을 경우
      if(!storeArr.includes(gems[e])){
        gemCnt++;
      }
      storeArr.push(gems[e]);
      e++;
    }

    // 모든 보석을 포함하는 지 확인
    if(gemCnt === kindOfGems) { 
      let currentRange = answer[1] - answer[0];
      let tmpRange = e - (s + 1);
      if(currentRange > tmpRange) {
        answer.pop();
        answer.pop();
        answer.push(s+1);
        answer.push(e);
      }
    }
  }
  
}

function solution(gems) {
  let answer = [0, 100001];

  findMinSection(gems,answer);

  return answer;
}

console.log(solution(gems));