# from 15:05 to 17:49
# 2h 44m
# 15:30 문제 파악 완료
# 16:45 4번 TC만 오답.. 디버깅 지옥에 빠짐(맞왜틀)
# 17:30 지우고 그냥 새로 짬
# remove 함수에서 스택 안에 4방향 for문이 들어있어야 함.. 
# 격자의 좌우가 연결된 bfs라고 생각했으면 쉬웠을 텐데 늦게 깨달음
# 원판에 남은 숫자들의 합, 숫자 남은 칸의 수 계속 관리해주기
# control 함수에서 1 더하고 빼줄 때 remains_num에 반영해줘야 함,,
# 확실히 deque 내장함수 rotate 사용하는 것보다 리스트 슬라이싱하여 회전 구현하는 것이 빠름(220ms => 184ms)

import sys
sys.stdin = open("17822_input.txt")
input = sys.stdin.readline
# from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def rotate(x, d, k):
    for i in range(x-1, N, x):      # x의 배수번 원판
        if d == 0:      # 시계방향
            # board[i].rotate(k)
            board[i] = board[i][-k:] + board[i][:-k]
            print(board[i][-k:], "+", board[i][:-k])
        else:    # 반시계방향
            # board[i].rotate(-k)
            board[i] = board[i][k:] + board[i][:k]

def remove():
    global flag_remove, remains_cnt, remains_num
    for sr in range(N):
        for sc in range(M):
            if board[sr][sc]:             # 해당 위치에 값이 있으면
                temp = board[sr][sc]      # 시작점 값 저장
                flag = False
                S = [(sr, sc)]
                while S:
                    r, c = S.pop()
                    for dd in range(4):
                        nr = r + dr[dd]
                        nc = (c + dc[dd]) % M
                        if not (0 <= nr < N) or not board[nr][nc]:
                            continue
                        if (nr, nc) == (sr, sc):
                            continue
                        if board[nr][nc] == temp:
                            board[nr][nc] = 0
                            S.append((nr, nc))
                            flag = True         # 수 지움
                            remains_num -= temp
                            remains_cnt -= 1

                if flag:                 # 수 지운 적 있으면
                    flag_remove = True   # 전역 flag_remove 에도 반영
                    board[sr][sc] = 0    # 시작점 값 지우기
                    remains_num -= temp
                    remains_cnt -= 1

def control():
    global remains_cnt, remains_num
    if remains_cnt:
        avg = remains_num / remains_cnt
    else:
        avg = 0

    # 남은 값들 평균값 기준으로 처리
    for i in range(N):
        for j in range(M):
            if not board[i][j]:
                continue
            if board[i][j] > avg:       # 평균보다 크면
                board[i][j] -= 1
                remains_num -= 1
            elif board[i][j] < avg:     # 평균보다 작으면
                board[i][j] += 1
                remains_num += 1

# main
N, M, T = map(int, input().split())
board = []
remains_num = 0     # 원판에 있는 수들의 합
remains_cnt = 0     # 원판에 숫자 적힌 칸의 갯수
for i in range(N):
    board.append(list(map(int, input().split())))
    for j in range(M):
        remains_num += board[i][j]
        remains_cnt += 1

# 총 T번 회전
for t in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)         # 원판 회전
    flag_remove = False     # 지운 이력 여부
    remove()                # 인접한 수 지우기
    if not flag_remove:     # 지운 인접한 수 없다면
        control()           # 평균값으로 원판에 남은 큰 수, 작은 수 처리

# 원판에 남은 숫자의 합
print(remains_num)