# 16:20 start
# 17:52 pass
# 1h 32m

import sys
sys.stdin = open("2105_input.txt")

# 시작점과 왼쪽, 오른쪽 길이 인자로 들어오면 돌면서 카페 종류 검사
def checkDesserts(sr, sc, left, right):
    global MAX
    cafe = [0] * 101
    cnt = 0             # 들린 카페 갯수
    lr = sr + left      # 왼쪽 꼭지점
    lc = sc - left
    rr = sr + right     # 오른쪽 꼭지점
    rc = sc + right
    br = sr + left + right      # 아래 꼭지점
    bc = sc + right - left

    # 왼쪽 길이만큼 두 변 검사
    for dis in range(1, left+1):
        if cafe[A[sr+dis][sc-dis]]:
            return
        cafe[A[sr+dis][sc-dis]] = 1
        if cafe[A[br-dis][bc+dis]]:
            return
        cafe[A[br-dis][bc+dis]] = 1
        cnt += 2

    # 오른쪽 길이만큼 두 변 검사
    for dis in range(1, right+1):
        if cafe[A[lr+dis][lc+dis]]:
            return
        cafe[A[lr+dis][lc+dis]] = 1
        if cafe[A[rr-dis][rc-dis]]:
            return
        cafe[A[rr-dis][rc-dis]] = 1
        cnt += 2

    # print(cafe)
    MAX = max(MAX, cnt)     # 최댓값 갱신


# 시작점 기준으로 좌, 우 가능한 거리 경우의 수 구하기
def makeDistance(sr, sc):
    for left in range(1, sc+1):
        for right in range(1, N-sc):
            if sr+left+right > N-1:     # 반대편 꼭지점이 맵 넘어가면 continue
                continue
            checkDesserts(sr, sc, left, right)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    MAX = -1
    for sr in range(N-2):
        for sc in range(1, N-1):
            makeDistance(sr, sc)

    print("#{} {}".format(tc+1, MAX))

    # 1 6
    # 2 -1
    # 3 4
    # 4 4
    # 5 8
    # 6 6
    # 7 14
    # 8 12
    # 9 18
    # 10 30