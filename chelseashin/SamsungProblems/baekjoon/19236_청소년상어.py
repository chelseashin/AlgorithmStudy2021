# 백트래킹, 구현, 시뮬레이션

import sys
sys.stdin = open("19236_input.txt")
input = sys.stdin.readline

# 8방향
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)

def find_fish(idx, A):
    for i in range(4):
        for j in range(4):
            if A[i][j] and A[i][j][0] == idx:
                return [i, j, A[i][j][1]]       # 물고기의 [위치, 방향] 정보 리턴
    return 0

# 물고기 이동
def fish_move(A, sr, sc):
    for num in range(1, 17):
        pos = find_fish(num, A)
        if not pos:     # 해당 물고기 없으면
            continue
        fr, fc, fd = pos
        for _ in range(8):
            nr = fr + dr[fd]    # 여기서 물고기의 현재 방향(fd)을 넘겨야 함
            nc = fc + dc[fd]
            if not (0 <= nr < 4 and 0 <= nc < 4):   # 맵 벗어나거나
                fd = (fd + 1) % 8
                continue
            if (nr, nc) == (sr, sc):    # 상어가 있는 위치라면
                fd = (fd + 1) % 8         # 방향 전환
                continue
            # 물고기가 갈 수 있는 공간이라면
            A[fr][fc][0], A[nr][nc][0] = A[nr][nc][0], A[fr][fc][0]   # 번호 맞바꾸기
            A[fr][fc][1], A[nr][nc][1] = A[nr][nc][1], fd    # 방향 바꾸되, 이동할 방향은 d
            break   # 해당 물고기 이동은 끝

def shark_move(A, sr, sc):
    available = []
    sd = A[sr][sc][1]   # 상어의 이동방향
    for i in range(4):
        nr = sr + dr[sd] * i
        nc = sc + dc[sd] * i
        if not (0 <= nr < 4 and 0 <= nc < 4):  # 맵 벗어나거나
            continue
        if not (1 <= A[nr][nc][0] <= 16):      # 먹을 물고기 없으면
            continue
        available.append([nr, nc])
    return available

# 현재 배열, 상어의 위치, 먹은 물고기 번호의 합
def dfs(A, r, c, total):
    global result
    arr = [[A[i][j][:] for j in range(4)] for i in range(4)]    # 맵 저장
    # 해당 위치의 물고기 먹기
    eat = arr[r][c][0]
    result = max(result, total + eat)   # 먹을 때마다 최댓값 갱신
    arr[r][c][0] = -1   # 상어 표시 -1
    # 물고기 이동 - 맵과 상어 위치 넘기기
    fish_move(arr, r, c)
    # 상어 이동할 수 있는 좌표 후보 리스트 리턴 - 맵과 상어 위치 넘기기
    candidates = shark_move(arr, r, c)
    for cr, cc in candidates:
        dfs(arr, cr, cc, total + eat)
        A = [[arr[i][j][:] for j in range(4)] for i in range(4)]    # 맵 복원
        # A = [x[:] for x in arr]   # 위와 같음

# main
raw = [[] for _ in range(4)]
for i in range(4):
    L = list(map(int, input().split()))
    for j in range(0, 7, 2):
        raw[i].append([L[j], L[j+1]-1])
result = float('-inf')
dfs(raw, 0, 0, 0)
print(result)