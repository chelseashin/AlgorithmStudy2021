# 10:30 start
# 11:31 finish
# 가로(행) 탐색, 세로(열)의 모든 케이스를 check_slope 함수에 넣어 가능하면 1, 불가능하면 0 리턴.
# check_slope 함수에서 같은 높이이면 cnt += 1
# 높이 1 높아질 때, 그동안의 쌓아온 거리가 경사로 길이보다 크거나 같다면 가능한 경우이므로 cnt = 1로 초기화
# 높이 1 낮아질 때, 현재 쌓아온 거리가 0보다는 크거나 같다면 현재 쌓아온 거리를 땡겨줘서 경사로 길이만큼 같은 높이를 유지할 때 경사로를 설치할 있도록 함. cnt = -X + 1
# 높이 2 이상 차이나면 경사로 건설할 수 없는 경우이므로 리턴 0

import sys
sys.stdin = open("4014_input.txt")

def check_slope(row):
    cnt = 1
    for i in range(1, N):
        if row[i] == row[i-1]:
            cnt += 1
        elif row[i] - row[i-1] == 1 and cnt >= X:   # 높이 1 높아지면
            cnt = 1
        elif row[i-1] - row[i] == 1 and cnt >= 0:   # 높이 1 낮아지면
            cnt = -X + 1
        else:   # 높이 2 이상 차이나면
            return 0
    if cnt >= 0:
        return 1
    return 0

# main
T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    A = []
    result = 0
    for i in range(N):
        A.append(list(map(int, input().split())))
        result += check_slope(A[i])

    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(A[j][i])
        result += check_slope(temp)

    print("#{} {}".format(tc+1, result))

    # 1 7
    # 2 4
    # 3 11
    # 4 11
    # 5 15
    # 6 4
    # 7 4
    # 8 1
    # 9 5
    # 10 8