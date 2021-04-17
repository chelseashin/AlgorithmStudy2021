# 09:46 start
# 10:28 finish
# 42m 소요

import sys
sys.stdin = open("1953_input.txt")
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
rev = (1, 0, 3, 2)

# 7가지 터널 상하좌우 뚫린 곳 표시 
tunnel = [[],
          [1, 1, 1, 1],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [1, 0, 0, 1],
          [0, 1, 0, 1],
          [0, 1, 1, 0],
          [1, 0, 1, 0]]

def bfs(sr, sc):
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])
    result = 1
    while Q:
        qlen = len(Q)
        for _ in range(qlen):
            r, c = Q.popleft()
            for d in range(4):
                if not tunnel[A[r][c]][d]:      # 나갈 수 있는 곳인지 먼저 확인
                    continue
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < M):     # 격자 밖이거나
                    continue
                if not A[nr][nc] or visited[nr][nc]:      # 터널이 없는 곳이거나 이미 방문했으면
                    continue
                if tunnel[A[nr][nc]][rev[d]]:             # 이동할 곳에 내가 들어갈 수 있는 곳인지
                    if visited[r][c] + 1 > L:             # L 시간 넘으면 답 리턴
                        return result
                    visited[nr][nc] = visited[r][c] + 1     # 이동 표시
                    Q.append((nr, nc))
                    result += 1
    return result

# main
T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    print("#{} {}".format(tc+1, bfs(R, C)))