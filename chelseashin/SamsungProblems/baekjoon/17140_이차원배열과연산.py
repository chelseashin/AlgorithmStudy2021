# 20:00 start
# 21:27 4번 tc만 틀림
# 21:42 74%에서 틀림 - 행의 길이, 열의 길이를 맵 A에서 구하는 것으로 바꿈
# 이후 받은 run time error 에서 35번 줄 조건 추가하고 while time <= 101로 바꿔주니 정답
# 21:48 finish
# 1시간 48분 소요..
# R 연산과 C 연산을 하나의 함수로 관리하기 위해 행열 전환하는 함수 사용
# Counter 라이브러리 이용하여 각 숫자의 등장 횟수 세는 리스트를 만들어줌

import sys
input = sys.stdin.readline
from collections import Counter

def calc():
    global row, col
    max_col = 0
    for i in range(len(A)):
        # 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬
        r_temp = sorted(Counter(A[i]).most_common(), key=lambda x: (x[1], x[0]))
        A[i] = []
        cnt = 0
        for n, c in r_temp:
            if n == 0:      # 0이면 무시
                continue
            A[i].extend([n, c])
            cnt += 2
        max_col = max(max_col, cnt)
        col = max_col                   # 각 행의 최대 길이 갱신
    for r_temp in A:
        if len(r_temp) < max_col:
            r_temp.extend([0] * (max_col - len(r_temp)))    # 최대 길이에 맞춰 0 채우기

def solve():
    global row, col, A
    time = 0
    while time < 101:
        if len(A) > r-1 and len(A[0]) > c-1:    # runtime error의 주범. 조건 만족할 때만 
            if A[r-1][c-1] == k:                # 종료 가능
                return time
        if len(A) >= len(A[0]):    # 행 갯수 >= 열 갯수이면 R 연산 수행
            calc()
        else:
            A = list(map(list, zip(*A)))    # 행 열 전환
            calc()
            A = list(map(list, zip(*A)))
        time += 1
    return -1

# main
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

print(solve())