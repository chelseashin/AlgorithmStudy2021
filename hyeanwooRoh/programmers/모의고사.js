// 16분

const student1 = [1, 2, 3, 4, 5];
const student2 = [2, 1, 2, 3, 2, 4, 2, 5];
const student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

function solution(answers) {
  const students = [0,0,0];

  answers.forEach((problem, idx) => {
    if(student1[idx%5] === problem) {
      students[0]++;
    }
    if(student2[idx%8] === problem) {
      students[1]++;
    }
    if(student3[idx%10] === problem) {
      students[2]++;
    }
  });

  const max = Math.max(...students);
  const answer = [];
  students.forEach((s,idx) => {
    if(s === max) {
      answer.push(idx+1);
    }
  })

  return answer;
}

// const answers = [1,2,3,4,5];
const answers = [1,3,2,4,2];

console.log(solution(answers));