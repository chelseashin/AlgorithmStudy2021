# 10:00 start
# 10:43 finish
# 실수 포인트 - 땅을 실제로 깎아주고 원상복귀시켜야 함.

import sys
sys.stdin = open("1949_input.txt")

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, chance):
    global MAX, visited
    MAX = max(MAX, visited[r][c])
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue
        if A[r][c] > A[nr][nc]:     # 이동할 곳이 현재 위치보다 낮은 경우 정상적으로 시행
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance)
            visited[nr][nc] = 0
        elif chance and A[nr][nc] - K < A[r][c]:
            temp = A[nr][nc]            # 깎기 전 봉우리의 위치 저장
            A[nr][nc] = A[r][c] - 1
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance-1)       # 산 깎을 기회 사용
            visited[nr][nc] = 0
            A[nr][nc] = temp            # 복원

# main
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = []
    top = 0
    for i in range(N):
        A.append(list(map(int, input().split())))
        for j in range(N):
            if A[i][j] > top:
                top = A[i][j]
    MAX = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i][j] == top:       # 가장 높은 봉우리에서 시작
                visited[i][j] = 1
                dfs(i, j, 1)
                visited[i][j] = 0

    print("#{} {}".format(tc+1, MAX))