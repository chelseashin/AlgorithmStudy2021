# 10:10 start
# 10:40 24% 런타임에러..
# 10:42 57%에서 틀렸습니다..
# 10:55 pass!

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 0
    Q = deque([(0, 0)])
    minTime = 0
    while Q:
        r, c = Q.popleft()
        if (r, c) == (N-1, M-1):    # 목적지까지 정상 도달
            if minTime:
                return min(visited[r][c], minTime)
            return visited[r][c]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):       # 격자 밖이면
                continue
            if A[nr][nc] == 1 or visited[nr][nc] > -1:  # 벽이거나 이미 방문했다면
                continue

            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))
            if A[nr][nc] == 2:      # 그람 구했다면 현 위치에서 목적지까지 직통시간 미리 구함
                minTime = visited[nr][nc] + (abs(N-1-nr) + abs(M-1-nc))

    # 목적지까지 정상적으로 도달하지 못한 경우
    if minTime:
        return minTime
    return T + 1

# main
N, M, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

temp = bfs()
if temp <= T:       # T시간 이내 도달
    print(temp)
else:
    print("Fail")

# 좋은 반례
# 3 3 100
# 0 1 2
# 0 1 1
# 0 0 0
# 답: 4