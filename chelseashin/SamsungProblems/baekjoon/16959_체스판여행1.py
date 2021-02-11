# Clone Coding
# 정말 정말 어려웠던 문제.. 거의 5~6시간 소요
# bfs + 상태 저장 + 의미 파악이 어려웠음
# 여전히 이해하기 어려운 문제

import sys
input = sys.stdin.readline
from collections import deque


# 나이트 : 8방향
knight_dr = (-1, -1, -2, -2, 2, 2, 1, 1)
knight_dc = (-2, 2, -1, 1, -1, 1, -2, 2)

# 룩 : 대각선 이동
rook_dr = (0, 0, 1, -1)
rook_dc = (1, -1, 0, 0)

# 비숍 : 직선 이동
bishop_dr = (1, -1, 1, -1)
bishop_dc = (1, -1, -1, 1)

N = int(input())
raw = []
visited = [[[[-1] * 3 for _ in range(N*N+1)] for _ in range(N)] for _ in range(N)]
Q = deque()
start, goal = 1, N*N
for i in range(N):
    raw.append(list(map(int, input().split())))
    for j in range(N):
        if raw[i][j] == 1:       # 1이 있는 칸에
            for k in range(3):   # 나이트, 룩, 비숍 중 하나를 놓으며 시작
                visited[i][j][1][k] = 0
                Q.append((i, j, 1, k))      # 첫 위치, 시작 숫자, 무슨 말인지

result = -1
while Q:
    r, c, num, piece = Q.popleft()
    if num == goal:
        # 첫 방문이거나 갱신된 값보다 작다면
        if result == -1 or result > visited[r][c][num][piece]:
            result = visited[r][c][num][piece]      # 갱신

    for p in range(3):        # 말 다른 말로 바꾸기
        if piece == p:
            continue
        if visited[r][c][num][p] == -1:
            visited[r][c][num][p] = visited[r][c][num][piece] + 1
            Q.append((r, c, num, p))

    # knight
    if piece == 0:
        for d in range(8):
            nr = r + knight_dr[d]
            nc = c + knight_dc[d]
            if (0 <= nr < N and 0 <= nc < N):
                next_num = num
                if raw[nr][nc] == num + 1:
                    next_num += 1
                if visited[nr][nc][next_num][piece] == -1:
                    visited[nr][nc][next_num][piece] = visited[r][c][num][piece] + 1
                    Q.append((nr, nc, next_num, piece))

    # rook
    elif piece == 1:
        for d in range(4):
            for dis in range(1, N+1):
                nr = r + rook_dr[d] * dis
                nc = c + rook_dc[d] * dis
                if (0 <= nr < N and 0 <= nc < N):
                    next_num = num
                    if raw[nr][nc] == num + 1:
                        next_num += 1
                    if visited[nr][nc][next_num][piece] == -1:
                        visited[nr][nc][next_num][piece] = visited[r][c][num][piece] + 1
                        Q.append((nr, nc, next_num, piece))
                else:
                    break

    # bishop
    elif piece == 2:
        for d in range(4):
            for dis in range(1, N+1):
                nr = r + bishop_dr[d] * dis
                nc = c + bishop_dc[d] * dis
                if (0 <= nr < N and 0 <= nc < N):
                    next_num = num
                    if raw[nr][nc] == num + 1:
                        next_num += 1
                    if visited[nr][nc][next_num][piece] == -1:
                        visited[nr][nc][next_num][piece] = visited[r][c][num][piece] + 1
                        Q.append((nr, nc, next_num, piece))
                else:
                    break
print(result)