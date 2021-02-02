# from 9:20 to 10:21
# 1h 1m
# 미리 어떻게 짤지 구상한 후 코드로 옮기니 오래 걸리지 않았다.
# 특별한 알고리즘 X, 있는 그대로 구현하는 simulation 문제
# 웜홀 정보 딕셔너리(wormhole_info)에 저장하여 웜홀 만났을 때 즉시 위치 바꿔줌
# 블록별로 상하좌우에서 왔을 때 어떻게 방향이 바뀌는지 change_dir에 정보 미리 저장해둠

import sys
sys.stdin = open("5650_input.txt")

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 블록별 방향 바꾸기
change_dir = ((),
              (1, 3, 0, 2),
              (3, 0, 1, 2),
              (2, 0, 3, 1),
              (1, 2, 3, 0),
              (1, 0, 3, 2))

# 게임 시작 위치와 방향 넘기면 게임 횟수 리턴
def play_game(r, c, d):
    global wormhole_info
    score = 0
    sr, sc = r, c       # 시작 위치 저장
    while True:
        r += dr[d]      # 이동하면서 시작해야 함
        c += dc[d]
        # 출발 위치로 돌아오거나 블랙홀 만나면 게임 끝. 점수 리턴
        if (r, c) == (sr, sc) or A[r][c] == -1:
            return score
        if 1 <= A[r][c] <= 5:           # 블록 만나면 방향 바꾸고 점수 + 1
            d = change_dir[A[r][c]][d]
            score += 1
        elif 6 <= A[r][c] <= 10:        # 웜홀 만나면 같은 번호의 웜홀로 이동. 방향은 유지
            r, c = wormhole_info[(r, c)]

# main
T = int(input())
for tc in range(T):
    N = int(input())
    wormhole_check = [0] * 11
    wormhole_info = dict()      # 웜홀 쌍 정보
    A = [[5] * (N+2)]   # 맵 벽(5)으로 둘러싸기
    for i in range(1, N+1):
        A.append([5] + list(map(int, input().split())) + [5])
        for j in range(1, N+1):
            if 6 <= A[i][j] <= 10:
                num = A[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else:   # 같은 번호 웜홀끼리 위치 정보 저장
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]
    A.append([5] * (N+2))

    # 게임 시작
    MAX = float('-inf')  # 게임에서 얻을 수 있는 최대 점수
    for sr in range(1, N+1):
        for sc in range(1, N+1):
            if A[sr][sc] == 0:      # 시작 위치와 방향 정한 후 게임 start
                for sd in range(4):
                    MAX = max(MAX, play_game(sr, sc, sd))
    print("#{} {}".format(tc+1, MAX))