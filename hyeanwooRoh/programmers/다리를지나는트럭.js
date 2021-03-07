// 52분
// 초반에 문제를 잘못이해해서 어렵게 풀었다
// 알고보니 순서가 정해져 있어서 조건맞추어 구현했다.

const bridge_length = 2;
const weight = 10;
const truck_weights = [7,4,5,6]

function solution(bridge_length, weight, truck_weights) {
  let sec = 1;
  let bridge = new Array(bridge_length).fill(0);
  let onBridgeWeight = 0;
  let truck_cnt = truck_weights.length;
  
  while(truck_cnt != 0) {
    if(onBridgeWeight + truck_weights[0] <= weight) {
      let truck = truck_weights.shift();
      onBridgeWeight += truck;
      bridge[bridge.length-1] = truck;
    }
    if(bridge[0] !== 0) {
      onBridgeWeight -= bridge[0];
      bridge[0] = 0;
      truck_cnt--;
    }
    for(let i = 1; i < bridge.length; i++) {
      if(bridge[i] !== 0) {
        bridge[i-1] = bridge[i];
        bridge[i] = 0;
      }
    }
  
    sec++;
  }

  return sec;
}


console.log(solution(bridge_length, weight, truck_weights));