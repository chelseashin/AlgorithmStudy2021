// 23분
// 여유분이 있는 학생을 기준으로 왼쪽부터 나눠주는 방식과
// 오른쪽부터 나눠주는 방식 두가지로 계산한 다음 더 큰값을 리턴해주는 식으로 함
// 확인해보니 왼쪽부터 나눠주기만 하면 답이 맞아서 시간을 줄일 수 있었음

function solution(n, lost, reserve) {
  const students = new Array(n).fill(1);

  lost.forEach(l => {
    students[l-1]--;
  })

  reserve.forEach(r => {
    students[r-1]++;
  })

  for (let i = 0; i < students.length; i++) {
    if (students[i] === 2) {
      if (i >= 1 && students[i-1] === 0) {
        students[i] = 1;
        students[i-1] = 1;
      } else if (i+1 < students.length && students[i+1] === 0) {
        students[i] = 1;
        students[i+1] = 1;
      }
    }
  }

  return students.filter(e => e !== 0).length;
}

console.log(solution(5,[2, 4],[1, 3, 5]));
console.log(solution(5,[2, 4],[3]));
console.log(solution(3,[3],[1]));
console.log(solution(7, [2, 3, 4], [1, 2, 3, 6]));

// function checkLeft(arr) {
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] === 2) {
//       if (i >= 1 && arr[i-1] === 0) {
//         arr[i] = 1;
//         arr[i-1] = 1;
//       } else if (i+1 < arr.length && arr[i+1] === 0) {
//         arr[i] = 1;
//         arr[i+1] = 1;
//       }
//     }
//   }

//   return arr.filter(e => e !== 0).length;
// }

// function checkRight(arr) {
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] === 2) {
//       if (i+1 < arr.length && arr[i+1] === 0) {
//         arr[i] = 1;
//         arr[i+1] = 1;
//       } else if (i >= 1 && arr[i-1] === 0) {
//         arr[i] = 1;
//         arr[i-1] = 1;
//       }
//     }
//   }

//   return arr.filter(e => e !== 0).length;
// }

// function solution(n, lost, reserve) {
//   const students = new Array(n).fill(1);

//   lost.forEach(l => {
//     students[l-1]--;
//   })

//   reserve.forEach(r => {
//     students[r-1]++;
//   })

//   return Math.max(checkLeft(students.slice()), checkRight(students.slice()));
// }