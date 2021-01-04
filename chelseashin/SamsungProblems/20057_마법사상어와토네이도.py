# from 9:20 to 11:30
# 2h 10m

import sys
sys.stdin = open("20057_input.txt")
input = sys.stdin.readline

# 좌 하 우 상
dr = (0, 1, 0, -1)
dc = (-1, 0, 1, 0)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

r, c = N//2, N//2
info = [(r, c, 0)]  # 토네이도 정보(현재 좌표, 방향) 담는 리스트
dd = 0      # 방향
dis = 1     # 거리
before = A[r][c]    # 최초 모래의 양
while True:
    for i in range(2):          # 같은 길이만큼이 2번씩 반복됨
        for j in range(dis):    # 길이만큼 이동
            nr = r + dr[dd]
            nc = c + dc[dd]
            before += A[nr][nc]
            if j == dis-1:      # 이동의 끝은 다음 방향을 가짐
                info.append((nr, nc, (dd+1) % 4))
            else:
                info.append((nr, nc, dd))
            r, c = nr, nc
        dd = (dd+1) % 4
    dis += 1
    if dis == N:    # 마지막 0번 행은 따로 처리
        for k in range(N-2, -1, -1):
            info.append((0, k, dd))
            before += A[0][k]
        break

# 비율 리스트
ratio = [0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05]
# 모래 날리는 방향 : 좌 하 우 상 - y 위치(nr, nc) 기준으로
move = [((-1, 1), (1, 1), (-1, 0), (1, 0), (-2, 0), (2, 0), (-1, -1), (1, -1), (0, -2)),
        ((-1, -1), (-1, 1), (0, -1), (0, 1), (0, -2), (0, 2), (1, -1), (1, 1), (2, 0)),
        ((-1, -1), (1, -1), (-1, 0), (1, 0), (-2, 0), (2, 0), (-1, 1), (1, 1), (0, 2)),
        ((1, -1), (1, 1), (0, -1), (0, 1), (0, -2), (0, 2), (-1, -1), (-1, 1), (-2, 0))]

# 토네이도 시전
result = 0
for r, c, d in info:
    nr = r + dr[d]
    nc = c + dc[d]
    current = A[nr][nc]     # y 위치의 현재 모래 양 저장
    for t in range(9):      # 9 방향으로 모래 날리기
        tr = nr + move[d][t][0]
        tc = nc + move[d][t][1]
        amount = int(current * ratio[t])    # 비율만큼 날린 모래 양
        if (0 <= tr < N and 0 <= tc < N):   # 범위 안에 있으면
            A[tr][tc] += amount             # 기존의 모래에 더해짐
            A[nr][nc] -= amount             # y 위치의 모래에서 빼줌
        else:
            result += amount                # 밖으로 나간 모래 처리
            A[nr][nc] -= amount
    # 알파 처리
    ar = nr+dr[d]
    ac = nc+dc[d]
    if (0 <= ar < N and 0 <= ac < N):       # 범위 안에 있으면
        A[ar][ac] += A[nr][nc]              # 기존의 모래에 더해짐
        A[nr][nc] = 0
    else:
        result += A[nr][nc]
        A[nr][nc] = 0
print(result)