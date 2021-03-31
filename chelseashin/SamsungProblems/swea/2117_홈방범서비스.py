# 16:50
# 17:43 현재 계속 45개만 맞음..
# 18:00 pass
# 1시간 10분 소요

import sys
sys.stdin = open("2117_input.txt")
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
KLst = [k*k+(k-1)*(k-1) for k in range(26)]     # K의 값 리스트 미리 구해놓기

def bfs(sr, sc):
    global maxCnt
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    Q = deque([(sr, sc)])

    home = A[sr][sc]
    dis = 1
    # 1 크기일 때도 검사
    if home * M - KLst[dis] >= 0:
        maxCnt = max(home, maxCnt)

    while dis < N+2:
        qlen = len(Q)
        for _ in range(qlen):
            r, c = Q.popleft()
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc))
                    if A[nr][nc]:       # 집이 있는 경우
                        home += 1
        # 보안회사의 이익이 0 이상이면 최댓값 갱신
        if home*M - KLst[dis+1] >= 0:
            maxCnt = max(home, maxCnt)
        dis += 1

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    maxCnt = 0
    for i in range(N):
        for j in range(N):
            bfs(i, j)       # 모든 위치에서 검사
    print("#{} {}".format(tc+1, maxCnt))
    # 1 5
    # 2 4
    # 3 24
    # 4 48
    # 5 3
    # 6 65
    # 7 22
    # 8 22
    # 9 78
    # 10 400
