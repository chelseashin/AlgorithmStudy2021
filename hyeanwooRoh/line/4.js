// 00:52:10 ~ 01:46:30 54분
// 규칙찾는데 애먹음

const mazes = [
  [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]],
  [[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]],
  [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]],
  [[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]],
]

const dr = [0,1,0,-1];
const dc = [1,0,-1,0];

function solve(maze) {
  let moveCnt = 0;
  let curR = 0;
  let curC = 0;
  let curD = 0;
  while (curR !== maze.length - 1|| curC !== maze[0].length - 1) {
    let leftD = (curD + 3) % 4;
    let lr = curR + dr[leftD];
    let lc = curC + dc[leftD];
    
    if (lr < 0 || lr >= maze.length || lc < 0 || lc >= maze[0].length || maze[lr][lc] === 1) {
      // 지금 위치의 왼쪽에 벽이 있는 경우
      let tr = curR + dr[curD];
      let tc = curC + dc[curD];
      if (tr < 0 || tr >= maze.length || tc < 0 || tc >= maze[0].length || maze[tr][tc] === 1) {
        // 가고자 하는 방향에 벽이 있을 경우
        // 시계방향으로 90도 꺾으면서 뚫린 곳 찾기
        while (true) {
          // 시계방향 90도이기때문에 방향을 돌리면 왼쪽에 벽이 있는걸로 취급됨
          curD = (curD + 1) % 4;
          tr = curR + dr[curD];
          tc = curC + dc[curD];
          if (tr < 0 || tr >= maze.length || tc < 0 || tc >= maze[0].length || maze[tr][tc] === 1) {
            continue;
          } else {
            curR = tr;
            curC = tc;
            moveCnt++;
            break;
          }
        }        
      } else {
        // 가고자 하는 방향에 벽이 없을 경우
        // 움직이고 다음턴
        curR = tr;
        curC = tc;
        moveCnt++;
      }
    } else {
      // 왼쪽에 벽이 없으므로 반시계방향으로 90도 꺾고 움직이기
      curD = leftD;
      curR += dr[curD];
      curC += dc[curD];
      moveCnt++;
    }

  }

  return moveCnt;
}

for (const maze of mazes) {
  console.log(solve(maze));
}