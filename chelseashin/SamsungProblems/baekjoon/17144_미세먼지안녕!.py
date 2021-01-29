# from 22:45 to 24:05
# 1h 20m
# 11:35 미세먼지 확산 완료
# 24:05 공기청정기 작동 완료 후 바로 통과
# 특별한 알고리즘 X. Simulation
# 1. 미세먼지 확산 시 새로운 맵에 표시하여 맵을 리턴
# 2. 공기청정기 작동은 윗 부분을 0, 아랫 부분을 1로 표현하여
#    각자의 범위 벗어날 때마다 방향 바꿔주며 새 위치와 현 위치를 swap하며 먼지 이동
#    이동 후 공기 청정기 그려주기

import sys
input = sys.stdin.readline

# 상 하 좌 우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 윗 부분 : 상 우 하 좌, 아랫 부분 : 하 우 상 좌
changeDir = ((0, 3, 1, 2), (1, 3, 0, 2))

# 미세먼지 확산
def spread():
    new = [[0] * C for _ in range(R)]   # 새로운 맵에 확산 상태 표현
    for r in range(R):
        for c in range(C):
            if A[r][c] > 0:
                fineDust = A[r][c]
                spreadDir = 0         # 퍼트릴 수 있는 방향
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if A[nr][nc] == -1:
                        continue
                    spreadDir += 1
                    new[nr][nc] += fineDust // 5
                new[r][c] += A[r][c] - (fineDust // 5) * spreadDir
    return new

# 공기청정기 작동
def clean():
    for part in range(2):   # 윗 부분: 0, 아랫 부분: 1
        sr, sc = airCleaner[part]
        r, c = sr, sc
        for d in range(4):
            while True:
                nr = r + dr[changeDir[part][d]]
                nc = c + dc[changeDir[part][d]]
                if part == 0:       # 윗 부분 범위
                    if not (0 <= nr < sr+1 and 0 <= nc < C):
                        break
                elif part == 1:     # 아랫 부분 범위
                    if not (sr <= nr < R and 0 <= nc < C):
                        break
                if (nr, nc) == (sr, sc):    # 시작 위치에 도착하면 종료
                    break
                A[r][c], A[nr][nc] = A[nr][nc], A[r][c]
                r, c = nr, nc
        A[sr][sc] = -1      # 작업 마친 후 공기청정기 표시

# main
R, C, T = map(int, input().split())
A = []
airCleaner = []
for i in range(R):
    A.append(list(map(int, input().split())))
    for j in range(C):
        if A[i][j] == -1:
            airCleaner.append((i, j))

for t in range(T):      # T초 동안
    A = spread()        # 1. 미세먼지 확산
    clean()             # 2. 공기청정기 작동

remains = 0             # 남은 미세먼지 양
for i in range(R):
    for j in range(C):
        if A[i][j] > 0:
            remains += A[i][j]
print(remains)