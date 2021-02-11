# 10:15 start
# 10:55 제출. 72%에서 틀림
# 11:08 정답
# 53분 소요
# 비활성 바이러스에도 바이러스가 퍼질 수 있음을 간과.
# 퍼질 수는 있으나 빈 공간을 모두 채운다는 개념과는 영향 X

import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 바이러스 퍼트렸을 때 최단시간 리턴
def bfs(virus):
    visited = [[-1] * N for _ in range(N)]
    for r, c in virus:
        visited[r][c] = 0
    Q = deque([(r, c) for r, c in virus])   # 깊은 복사 해줘야 경우마다 초기상태 유지 가능
    cnt = 0
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == 1:
                continue
            if visited[nr][nc] == -1:   # 실수 포인트 : 비활성 바이러스가 있는 공간에도 바이러스 퍼질 수 있음.
                if A[nr][nc] == 0:      # 완전 빈 공간일 때만 cnt + 1
                    cnt += 1
                visited[nr][nc] = visited[r][c] + 1     # 새 위치에 최단시간 남기며 이동
                Q.append((nr, nc))
                if cnt == space:        # 빈 공간 모두 채웠을 때 시간 리턴
                    return visited[nr][nc]
    return float('inf')

# 조합 코드
def comb(depth, k):
    global min_time
    if depth == M:
        min_time = min(min_time, bfs(pick))
        return
    for i in range(k, virus_cnt):
        if check[i]:
            continue
        check[i] = 1
        pick.append(virus_pos[i])
        comb(depth+1, i+1)
        pick.pop()
        check[i] = 0

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
virus_pos = []
virus_cnt = 0
space = 0
for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            space += 1
        if A[i][j] == 2:
            virus_pos.append((i, j))
            virus_cnt += 1

if space == 0:  # 빈 공간 X
    print(0)
else:
    min_time = float('inf')
    check = [0] * virus_cnt
    pick = []
    comb(0, 0)
    if min_time == float('inf'):
        print(-1)
    else:
        print(min_time)