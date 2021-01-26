# 14:30 start
# 15:25 흰색, 빨간색 완성
# 16:55 디버깅... 5번 tc만 계속 안 맞음
# 18:00 end. 이전 답 참고하여 로직 고치고 pass
# 헐.. 근데 시간 1위 달성

import sys
input = sys.stdin.readline

dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)
rev = (1, 0, 3, 2)

def solve():
    turn = 0
    while True:
        turn += 1
        if turn >= 1000:    # 종료조건 1
            print(-1)
            return
        for num in range(1, K+1):
            r, c, d = horse_info[num]   # 현재 말의 위치, 방향
            nr = r + dr[d]
            nc = c + dc[d]
            # 이동하려는 칸이 파란색이거나 체스판을 벗어나는 경우
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == blue:
                d = rev[d]      # 방향 전환하고 그 방향으로 한 칸 이동
                nr = r + dr[d]
                nc = c + dc[d]
                # 다시 이동한 위치가 파란색 or 체스판 벗어나면
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == blue:
                    horse_info[num][2] = d      # 위치 그대로, 방향만 전환
                    continue
            # 이동하려는 위치가 흰색 또는 빨간색일 경우
            cur_idx = A[r][c].index(num)    # 현재 말이 몇 번째 있는지
            left = A[r][c][:cur_idx]
            right = A[r][c][cur_idx:]
            A[r][c] = left
            if board[nr][nc] == red:        # 빨간색이면 reverse
                right.reverse()
            A[nr][nc].extend(right)
            if len(A[nr][nc]) >= 4:     # 종료조건 2 - 말 4개 이상 쌓이면
                print(turn)
                return
            for n in right:             # 함께 움직인 말들도 위치 갱신
                horse_info[n][0] = nr
                horse_info[n][1] = nc
            horse_info[num][2] = d

# main
N, K = map(int, input().split())    # 맵 크기, 말 갯수
board = [list(map(int, input().split())) for _ in range(N)]     # 체스판 정보
A = [[[] for _ in range(N)] for _ in range(N)]
horse_info = dict()     # 말의 [위치, 방향] 정보 저장

for num in range(1, K+1):
    r, c, d = map(int, input().split())
    A[r-1][c-1] = [num]
    horse_info[num] = [r-1, c-1, d-1]
white, red, blue = 0, 1, 2
solve()