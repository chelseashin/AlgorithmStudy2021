# from 14:40 to 15:13
# 33m

import sys
sys.stdin = open("20055_input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

robot = [0] * N * 2     # 로봇 위치 표시
zero = 0    # 내구도 0의 갯수
time = 0    # 몇 단계인지
while True:
    # 1. 벨트 회전
    A = [A[-1]] + A[:-1]
    robot = [robot[-1]] + robot[:-1]
    robot[N-1] = 0

    # 2. 로봇 이동
    for i in range(N-2, 0, -1):
        if robot[i]:    # 로봇이 있을 때
            # 다음 칸에 로봇 없고, 내구도 0 이상이면
            if not robot[i+1] and A[i+1] > 0:
                robot[i+1] = 1  # 로봇 이동
                robot[i] = 0
                A[i+1] -= 1         # 내구도 1 감소
                if A[i+1] == 0:     # 감소 후 0이면
                    zero += 1
    robot[N-1] = 0

    # 3. 로봇 올리기
    if not robot[0] and A[0] > 0:
        robot[0] = 1
        A[0] -= 1
        if A[0] == 0:
            zero += 1

    # 4. 0인 칸이 K개 이상이면 과정 종료
    time += 1
    if zero >= K:
        print(time)
        break