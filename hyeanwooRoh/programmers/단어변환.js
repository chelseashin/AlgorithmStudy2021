// 45분

// BFS로 시도했다가 DFS가 더 쉬울것같아서 바꿈

function solution(begin, target, words) {
  if (words.find(word => word === target) === undefined) {
    return 0;
  }
  
  function dfs(depth, prevWord, nextWord) {
    if (depth > words.length) return ;

    if (nextWord === target) {
      answer = Math.min(answer, depth);
      return;
    }

    for (const word of words) {
      console.log(depth, 'p:',prevWord,'n:',nextWord, 'w:',word);
      if (word !== prevWord && word !== nextWord && isConverse(nextWord, word)) {
        dfs(depth+1, nextWord, word);
      }
    }
  }
  
  let answer = 100000007;

  dfs(0, "", begin);

  return answer;
}

function isConverse(word, toWord) {
  let diffCnt = 0;
  for (let i = 0; i < word.length; i++) {
    if (word[i] !== toWord[i]) {
      diffCnt++;
    }

    if (diffCnt > 1) return false;
  }

  if (diffCnt === 1) {
    return true;
  } else {
    return false;
  }
}

console.log(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]));
console.log(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]));