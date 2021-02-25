# 09:46 start
# 10:28 finish
# 42m 소요

import sys
sys.stdin = open("1953_input.txt")
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
rev = (1, 0, 3, 2)

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
                if not tunnel[A[r][c]][d]:
                    continue
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < M):
                    continue
                if not A[nr][nc] or visited[nr][nc]:
                    continue
                if tunnel[A[nr][nc]][rev[d]]:
                    if visited[r][c] + 1 > L:
                        return result
                    visited[nr][nc] = visited[r][c] + 1
                    Q.append((nr, nc))
                    result += 1
    return result

# main
T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    print("#{} {}".format(tc+1, bfs(R, C)))