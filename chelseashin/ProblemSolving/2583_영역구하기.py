# 15:00 start
# 15:22 finish
# 간단한 BFS 문제

import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(sr, sc):
    Q = deque([(sr, sc)])
    A[sr][sc] = 0
    cnt = 1
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < M and 0 <= nc < N) or not A[nr][nc]:
                continue
            if A[nr][nc]:
                A[nr][nc] = 0
                Q.append((nr, nc))
                cnt += 1
    return cnt

# main
M, N, K = map(int, input().split())
A = [[1] * N for _ in range(M)]
for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            A[r][c] = 0
result = 0
parts = []
for i in range(M):
    for j in range(N):
        if A[i][j]:
            parts.append(bfs(i, j))
            result += 1
print(result)
print(*sorted(parts))