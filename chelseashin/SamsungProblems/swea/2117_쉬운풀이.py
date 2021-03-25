import sys
sys.stdin = open("2117_input.txt")
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
KLst = [k*k+(k-1)*(k-1) for k in range(26)]     # K의 값 리스트 미리 구해놓기

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = []
    homeLst = []
    for i in range(N):
        A.append(list(map(int, input().split())))
        for j in range(N):
            if A[i][j]:
                homeLst.append((i, j))
    # print(homeLst)
    maxCnt = 0
    for k in range(1, N+2):
        for i in range(N):
            for j in range(N):
                home = 0
                for r, c in homeLst:
                    if abs(i-r) + abs(j-c) < k:
                        home += 1
                if home * M - KLst[k] >= 0:
                    maxCnt = max(home, maxCnt)

    print("#{} {}".format(tc+1, maxCnt))
    # 1 5
    # 2 4
    # 3 24
    # 4 48
    # 5 3
    # 6 65
    # 7 22
    # 8 22
    # 9 78
    # 10 400