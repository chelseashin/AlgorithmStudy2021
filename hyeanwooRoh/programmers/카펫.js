// 11분

function solution(brown, yellow) {
  const size = brown + yellow;
  const len = parseInt(size/3);
  for(let x = 3; x <= len; x++) {
    if(size % x === 0) {
      const y = size / x;
      const calc = y * 2 + (x - 2) * 2;
      if(calc === brown) {
        return [y, x];
      }
    }
  }
}

// 수식으로만 푼 코드

// function solution(brown, yellow) {
//   const x = (brown - 12) * 0.5;
//   const y = yellow - brown + 8;
//   const i = ( 8 + x + Math.sqrt( Math.pow(x, 2) - (4 * y) ) ) * 0.5;
//   const j = ( 8 + x - Math.sqrt( Math.pow(x, 2) - (4 * y) ) ) * 0.5;
  
//   console.log(x,y,i,j);

//   var answer = [i, j];
//   return answer;
// }


const brown = 10;
const yellow = 2;
// const brown = 8;
// const yellow = 1;
// const brown = 24;
// const yellow = 24;

console.log(solution(brown, yellow));