# 17:50 start
# 19:31 pass
# 1시간 41분 소요,, 쉬운 문젠데 너무 오래 걸렸다.
# 시뮬레이션은 몇일만 쉬어도 금방 감 떨어진다.. 쉼없이 계속 코딩하자
# 특별한 알고리즘은 없다. 주어진 대로 그대로 구현하면 됨!

from sys import stdin
input = stdin.readline

# 8방향
dr = (0, 0, -1, -1, -1, 0, 1, 1, 1)
dc = (0, -1, -1, 0, 1, 1, 1, 0, -1)

# 1. 모든 구름이 d방향으로 s칸 이동한다.
# 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
def moveClouds(d, s):
    newClouds = set()
    for r, c in clouds:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        A[nr][nc] += 1
        newClouds.add((nr, nc))
    return newClouds

# 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
def rainFall():
    for r, c in newClouds:
        waterCnt = 0
        for d in range(2, 9, 2):    # 대각선 방향(2, 4, 6, 8)
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if A[nr][nc]:   # 바구니에 물 있는 곳이면
                waterCnt += 1
        A[r][c] += waterCnt     # 4방향 중 물이 있는 곳의 갯수만큼 더함

# 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
def makeNewClouds():
    clouds = set()      # 3. 구름이 모두 사라진다. 초기화 후 재활용
    for r in range(N):
        for c in range(N):
            if (r, c) in newClouds: # 구름이 있던 곳이면 넘어감
                continue
            if A[r][c] >= 2:        # 물의 양 2 이상인 모든 칸에 물이 생기고
                clouds.add((r, c))  # 구름의 새 위치 추가
                A[r][c] -= 2        # 물의 양 2 줄어듦
    return clouds

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
clouds = {(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)}

# 비바라기 M번 시전
for m in range(M):
    d, s = map(int, input().split())
    newClouds = moveClouds(d, s)    # 구름 이동 후 새 위치 리턴
    rainFall()
    clouds = makeNewClouds()        # 구름의 새 위치 리턴

# 출력
result = 0
for row in range(N):
    for col in range(N):
        result += A[row][col]
print(result)