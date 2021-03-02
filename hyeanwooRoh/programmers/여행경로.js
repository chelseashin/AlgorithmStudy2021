function solution(tickets) {
  const path = ['ICN'];
  const route = {
    ICN: [],
  };

  for (const [source, destination] of tickets) {
    if (route[source] === undefined) {
      route[source] = [destination];
    } else {
      route[source].push(destination);
    }
  }

  for (const obj of Object.values(route)) {
    if (obj.length > 1) obj.sort().reverse();
  }

  let curSource = 'ICN';
  for (let i = 0; i < tickets.length ; i++) {
    console.log(curSource, route[curSource], path)
    const tmpDest = route[curSource].pop();
    path.push(tmpDest);
    curSource = tmpDest;
  }

  return path;
}

// console.log(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]));
// console.log(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]));
// console.log([['ICN', 'AAA'], ['ICN', 'AAA'], ['ICN', 'AAA'],['AAA', 'ICN'], ['AAA', 'ICN']]);
console.log(solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]));