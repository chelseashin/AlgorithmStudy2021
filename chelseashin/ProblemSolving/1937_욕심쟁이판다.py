# 설명 링크 : https://yabmoons.tistory.com/154
# DP - Memoization을 해서 불필요한 연산을 없앤다!
# 이미 해본 곳을 또 탐색할 필요는 없으므로 표시된 것을 그대로 가져와서 활용한다.

from sys import stdin

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    if check[r][c]:
        return check[r][c]
    check[r][c] = 1     # 해당 위치는 무조건 먹을 수 있으므로 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        # 이동할 곳에 대나무가 더 많다면
        if A[r][c] < A[nr][nc]:
            # 판다가 오래 사는 일수 = 4방향 중 판다가 가장 많이 이동한 횟수(최장 경로) + 1
            check[r][c] = max(check[r][c], dfs(nr, nc)+1)
    return check[r][c]

# main
N = int(stdin.readline())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]     # memoization

for r in range(N):
    for c in range(N):
        if not check[r][c]:
            dfs(r, c)
            # print((r, c), "==============")
            # for ck in check:
            #     print(ck)
MAX = 0
for i in range(N):
    MAX = max(MAX, max(check[i]))
print(MAX)