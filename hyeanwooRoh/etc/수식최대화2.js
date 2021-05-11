const expression = "100-200*300-500+20";
// const expression = "50*6-3*2";

function calc(arr, order) {
  let calcArr = [...arr];
  let expIdx = 0;

  while(expIdx !== order.length) {
    const tmpArr = [];
    for(let i=0; i < calcArr.length; i++) {
      if(calcArr[i] === order[expIdx]){
        tmpArr.push(eval(tmpArr.pop() + calcArr[i] + calcArr[i+1]));
        i++;
      } else {
        tmpArr.push(calcArr[i]);
      }
    }
    calcArr = [...tmpArr];
    expIdx++;
  }
  let result = Math.abs(calcArr[0]);
  max = Math.max(max, result);
}

let max = 0;

function solution(expression) {
  const arr = expression.split(/(\-|\*|\+)/g);

  calc(arr,['*','+','-']);
  calc(arr,['*','-','+']);
  calc(arr,['+','*','-']);
  calc(arr,['+','-','*']);
  calc(arr,['-','+','*']);
  calc(arr,['-','*','+']);

  return max;
}

console.log(solution(expression));
