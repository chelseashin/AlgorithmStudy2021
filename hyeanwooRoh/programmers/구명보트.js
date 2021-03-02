// 27분 + 12분
// 첫번째 시도에서 효율성에서 터졌다
// 두번째 시도에서는 반대로 무거운 사람부터 처리했더니 코드가 단순해지고 통과

function solution(people, limit) {
  people.sort((a,b) => b - a);
  let boat = 0;

  for (let i = 0; i < people.length; i++) {
    if (people[i] + people[people.length-1] <= limit) {
      people.pop();
    }
    boat++;
  }

  return boat;
}

console.log(solution([70, 50, 80, 50],100));
console.log(solution([70, 80, 50],100));
console.log(solution([40, 40, 60, 70, 100, 95],110));


// function solution(people, limit) {
//   people.sort((a,b) => a - b);

//   let answer = 0;
//   while (people.length > 0) {
//     const tmpPeople = people.shift();
    
//     let idx = -1;
//     for (let i = 0; i < people.length; i++) {
//       if(tmpPeople + people[i] <= limit){
//         idx = i;
//       } else {
//         break;
//       }
//     }

//     if (idx !== -1) {
//       people.splice(idx, 1);
//     }

//     answer++;
//   }

//   return answer;
// }