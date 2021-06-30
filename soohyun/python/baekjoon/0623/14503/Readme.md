# 문제의 핵심
- 구현
- BFS
- 조건을 나눌 수 있는가?

# 사용 자료구조
- 로봇: 클래스
    - 현재위치
    - 바라보고 있는 방향
    - 움직인 영역개수
    - 로봇 변화 횟수
- visited: maze와 동일 2차원배열
- queue: 데크

# 알고리즘
-큐가 빌때까지 아래를 반복
    - 큐에서 하나 제외시킴
    - 다음 바라보는 방향과 다음위치를 계산함
    - 다음갈곳이 범위내에 있는경우
        - 다음으로 갈곳이청소가 이미 되어있거나 벽이고
            -  네방향 모두 청소되어 있는경우
                -  바라보는 방향으로 후진한다.
                    - 큐에 다음위치를 계산하여 넣는다.
                - 뒤쪽벽이라 후진이 불가능하면
                    - 멈춘다.
            - 네방향 모두 청소되어있지 않는경우
                - 방향만 돌린채 큐에 넣는다.
        - 청소되어있지 않으면
            - 방문표시를 하고
            - 청소후 큐에 넣는다.(영역을 +1함)

# Code Snippet
```python

    while len(queue) > 0:
        robot = queue.popleft()
        row, col = robot.loc
        nd = (4 + (robot.direction - 1)) % 4
        nr, nc = row + DIRECTION[nd][0], col + DIRECTION[nd][1]

        if is_inrange(nr, nc, height, width):
            #  다음으로 갈곳이청소가 이미 되어있거나 벽인 경우에는
            if visited[nr][nc] >= 1 or maze[nr][nc] == 1:
                # 네방향 모두 청소되어 있는경우
                if robot.robot_change >= 4:
                    # 바라보는 방향을 유지하면서 후진한다.
                    nr, nc = row - DIRECTION[robot.direction][0], col - DIRECTION[robot.direction][1]
                    if is_inrange(nr, nc, height, width):
                        # 뒤쪽이 벽이라 후진이 불가능한경우
                        if maze[nr][nc] == 1:
                            break
                        # 후진한다.
                        queue.append(Robot((nr, nc), robot.direction, 
                                            robot.count, 
                                            0))
                # 네방향 모두 청소되어있지 않으면
                else:
                    # 방향을 돌리고 2번으로 돌아간다.
                    queue.append(Robot((row, col), nd, 
                                        robot.count, 
                                        robot.robot_change+1))
            else:
                visited[nr][nc] = 2
                queue.append(Robot((nr, nc), nd, 
                                    robot.count + 1, 
                                    0)) 
```
# 빨리푼사람 풀이
```python
while m[a][b]!=1: # 벽을 만나면 멈춤
    if m[a][b]==0:
        cnt+=1
    m[a][b]=-1
    ck=1
    for i in range(1,5):
        x = a + d[c-i]
        y = b + d[3-c+i]
        if m[x][y]==0:
            a = x
            b = y
            c = (c-i)%4
            ck= 0
            break
    if ck:
        a+=d[c+2]
        b+=d[c+3]
```
# 시간 복잡도

# 복기할것
- 구현을 어떻게해야할까 한참 생각한 문제          