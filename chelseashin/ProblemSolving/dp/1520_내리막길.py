# 11:00 start
# 11:56 end - 블로그 참고.. https://dirmathfl.tistory.com/204
# DFS + DP로 목적지까지 도착할 수 있는지 검사한다
# 재귀 호출을 통해서 방문 가능한 경로의 수를 반환하고,
# 한번 탐색한 경로는 더 이상 탐색하지 않도록 하는 방법을 사용하여야
# 시간 초과를 발생시키지 않고 문제를 해결할 수 있다.
# dfs를 통해 (m - 1, n - 1)까지 탐색한 후에,
# 값을 return 해주는 방식을 사용하면 오른쪽 아래 끝부터 값이 올라오게 될 것이다.

# 루프를 방지하기 위해 방문 확인 배열 visited를 -1로 초기화하고 이동할 때마다 0으로 설정해준다

# 1. 과정을 진행하면서 해당 위치가 목적지에 도착하면 1을 반환
# 2. 0 이상의 값이면 이전에 그만큼 방문 경로가 있으므로 해당 값을 반환해서 더해준다
# 3. -1이면 방문하지 않은 경로이므로 dfs + dp 수행


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c):
    if r == N-1 and c == M-1:   # 목적지 도착 시 1 반환
        return 1
    if visited[r][c] == -1:
        visited[r][c] = 0
        for v in visited:
            print(v)
        print()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if A[r][c] > A[nr][nc]:
                visited[r][c] += dfs(nr, nc)
    return visited[r][c]

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

print(dfs(0, 0))
# print(visited[0][0])      # 위와 같음