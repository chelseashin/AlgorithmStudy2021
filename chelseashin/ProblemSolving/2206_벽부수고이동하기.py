# 17:30 start
# 18:55 finish
# 1h 25m 소요
# bfs 함수 안에서 꽤 헤맸다.
# 폭탄 가지고 있을 때, 없을 때를 다른 visited에 표현
# 큐에 폭탄 정보와 위치 정보를 담으면서 BFS 퍼트리는 것이 핵심이다.
# 목적지 도달하면 거리 정보 리턴
# 목적지 도달하지 못하면 -1 리턴

import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    Q = deque([(0, 0, 1)])
    visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1
    visited[1][0][0] = 1
    while Q:
        r, c, bomb = Q.popleft()
        
        # 목적지에 도달했을 때의 visited에 있는 거리 정보 리턴
        if r == N-1 and c == M-1:
            # for vi in visited:
            #     for v in vi:
            #         print(v)
            #     print()
            return visited[bomb][r][c]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[bomb][nr][nc]:
                continue

            # 벽 만났고 폭탄 기회 남았다면
            if A[nr][nc] and bomb:
                visited[0][nr][nc] = visited[1][r][c] + 1   # 이 부분이 헷갈린 부분
                Q.append((nr, nc, 0))

            # 벽이 아닌 경우 일반적인 bfs
            if not A[nr][nc]:
                visited[bomb][nr][nc] = visited[bomb][r][c] + 1
                Q.append((nr, nc, bomb))
    return -1

N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
print(bfs())