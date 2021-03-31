# 19:30 start
# 21:00 restart
# 21:28 pass

from sys import stdin
input = stdin.readline

# (시작 위치, 방향, 길이) 인자로 넘기면 재귀로 도미노 넘기기
def domino(sr, sc, sd, length):
    global temp
    if board[sr][sc]:
        board[sr][sc] = 0
        temp += 1
    for _ in range(length-1):
        sr += dirInfo[sd][0]
        sc += dirInfo[sd][1]
        if not (0 <= sr < N and 0 <= sc < M):
            continue
        domino(sr, sc, sd, board[sr][sc])

# main
N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
raw = [row[:] for row in board]
dirInfo = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
total = 0
for game in range(R):
    off_r, off_c, off_d = input().split()
    def_r, def_c = map(int, input().split())
    off_r = int(off_r) - 1
    off_c = int(off_c) - 1
    def_r -= 1
    def_c -= 1

    # 공격 : 도미노 넘기기
    temp = 0
    if board[off_r][off_c]:
        domino(off_r, off_c, off_d, board[off_r][off_c])
    total += temp

    # 수비 : 도미노 세우기
    board[def_r][def_c] = raw[def_r][def_c]

print(total)
for r in range(N):
    for c in range(M):
        if board[r][c]:
            board[r][c] = "S"
        else:
            board[r][c] = "F"
    print(*board[r])