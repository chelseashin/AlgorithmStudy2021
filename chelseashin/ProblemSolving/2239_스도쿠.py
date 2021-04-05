from sys import stdin
input = stdin.readline

# 나의 풀이
# # 행 체크
# def rowCheck(r, num):
#     for c in range(9):
#         if board[r][c] == num:
#             return False
#     return True

# # 열 체크
# def colCheck(c, num):
#     for r in range(9):
#         if board[r][c] == num:
#             return False
#     return True

# def squareCheck(r, c, num):
#     nr = (r//3) * 3
#     nc = (c//3) * 3
#     for i in range(3):
#         for j in range(3):
#             if board[nr+i][nc+j] == num:
#                 return False
#     return True

# def dfs(depth):
#     if depth == len(zeros):
#         for row in range(9):
#             for col in range(9):
#                 print(board[row][col], end="")
#             print()
#         exit()
    
#     nr, nc = zeros[depth]
#     for num in range(1, 10):
#         if rowCheck(nr, num) and colCheck(nc, num) and squareCheck(nr, nc, num):
#             board[nr][nc] = num
#             dfs(depth + 1)
#             board[nr][nc] = 0

# # main
# board = []
# zeros = []
# for r in range(9):
#     board.append(list(map(int, input().rstrip())))
#     for c in range(9):
#         if board[r][c] == 0:
#             zeros.append((r, c))
# dfs(0)

# 다른 풀이
def solve(depth):
    if depth == N:
        for i in range(9):
            for j in range(9):
                print(A[i][j], end="")
            print()
        exit()
    r = B[depth] // 9
    c = B[depth] % 9
    for num in range(1, 10):
        temp = r//3*3 + c//3
        if not (row[r][num] or col[c][num] or squ[temp][num]):
            row[r][num], col[c][num], squ[temp][num] = 1, 1, 1
            A[r][c] = num
            solve(depth+1)
            A[r][c] = 0
            row[r][num], col[c][num], squ[temp][num] = 0, 0, 0

A = [list(map(int, input().rstrip())) for _ in range(9)]
B = [0] * 81
row = [[0] * 10 for _ in range(9)]      # 가로 정보
col = [[0] * 10 for _ in range(9)]      # 세로 정보
squ = [[0] * 10 for _ in range(9)]      # 3*3 정보

N = 0
for i in range(9):
    for j in range(9):
        n = A[i][j]
        if n:
            row[i][n] = 1
            col[j][n] = 1
            squ[i//3*3 + j//3][n] = 1
        else:
            B[N] = i * 9 + j  # 0일 때, 몇 번째 칸이 비어있는지
            N += 1
solve(0)