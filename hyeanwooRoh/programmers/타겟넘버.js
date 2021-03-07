// 8분

function solution(numbers, target) {
  let answer = 0;

  function dfs(index, depth, total) {
    if (depth === numbers.length) {
      if (total === target) {
        answer++;
      }
      return;
    }

    dfs(index+1, depth+1, total+numbers[index]); // +
    dfs(index+1, depth+1, total-numbers[index]); // -
  }

  dfs(0, 0, 0);

  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3));