// 26분
// 푸는 방향은 맞지만 자바스크립트 활용이 조금 아쉽다
// array.findIndex()와 array.some()을 사용해보자

const priorities = [2, 1, 3, 2];
const location = 2;

function solution(priorities, location) {
  let sortPri = [];
  priorities = priorities.map((item, idx) => {
    return {item, idx}
  })

  while(priorities.length > 0) {
    let tmpP = priorities.shift();
    let isImportant = true;
    
    for (const p of priorities) {
      if(tmpP.item < p.item) {
        priorities.push(tmpP);
        isImportant = false;
        break;
      }
    }
    
    if(isImportant) {
      sortPri.push(tmpP);
    }

    // let hasHighPriority = priorities.some(elem => elem.item > tmpP.item);
    // if(hasHighPriority) {
    //   priorities.push(tmpP);
    // } else {
    //   sortPri.push(tmpP);
    // }
  }

  for (let i = 0; i < sortPri.length; i++) {
    if(sortPri[i].idx === location) {
      return i + 1;
    }
  }
  // return sortPri.findIndex((item) => item.idx === location) + 1;
}

console.log(solution(priorities, location));