# from 14:30 to 17:17
# 2h 47m
# 문제 파악은 금방
# d1, d2 길이 구하는 부분에서 계속 인덱스 틀려서 시간 소모
# 5로 안쪽을 채울 것이 아니라 테두리를 그려놓고 나머지 1, 2, 3, 4구역을 채운 후
# 전체 인구 수에서 그 만큼의 인구 합을 뺀 것을 중간 5구역의 전체 인구 합으로 생각

import sys
input = sys.stdin.readline

# 나눈 구획별 번호 그리기
def draw(sr, sc, d1, d2):
    global MIN
    check = [[0] * N for _ in range(N)]
    rr, rc = sr+d2, sc+d2   # 오른쪽 꼭지점
    lr, lc = sr+d1, sc-d1   # 왼쪽 꼭지점
    # 테두리 5로 채우기
    for i in range(d1+1):
        check[sr+i][sc-i] = 5
        check[rr+i][rc-i] = 5
    for j in range(1, d2):
        check[sr+j][sc+j] = 5
        check[lr+j][lc+j] = 5
    temp = [0] * 5   # 다섯 구역 각각의 인구 수의 합 담기
    # 1 채우기
    for i in range(lr):
        for j in range(sc+1):
            if check[i][j] == 5:
                break
            if check[i][j] == 0:
                check[i][j] = 1
                temp[0] += raw[i][j]
    # 2 채우기
    for i in range(rr+1):
        for j in range(N-1, sc, -1):
            if check[i][j] == 5:
                break
            if check[i][j] == 0:
                check[i][j] = 2
                temp[1] += raw[i][j]
    # 3 채우기
    for i in range(lr, N):
        for j in range(sc-d1+d2):
            if check[i][j] == 5:
                break
            if check[i][j] == 0:
                check[i][j] = 3
                temp[2] += raw[i][j]
    # 4 채우기
    for i in range(rr, N):
        for j in range(N-1, sc-d1+d2-1, -1):
            if check[i][j] == 5:
                break
            if check[i][j] == 0:
                check[i][j] = 4
                temp[3] += raw[i][j]
    # 5구역 인구 합 더하기
    temp[4] = (total - sum(temp))
    gap = max(temp) - min(temp)
    MIN = min(MIN, gap)     # 최솟값 갱신

# 시작점 기준으로 구획 나누기
def divide(sr, sc):
    for d1 in range(1, sc+1):
        for d2 in range(1, N-d1):
            if 0 <= sr <= (sr+d1+d2) < N and 0 <= sc-d1 < sc < sc+d2 < N:
                draw(sr, sc, d1, d2)

# main
N = int(input())
total = 0       # 전체 인구 수
raw = []        # 인구 정보 맵
for n in range(N):
    raw.append(list(map(int, input().split())))
    total += sum(raw[n])

# 선거구 나누는 기준점 찾기
MIN = float('inf')      # 갱신할 최소 인구 차이
for sr in range(N-2):
    for sc in range(1, N-1):
        divide(sr, sc)      # 시작점 기준으로 선거 구획 나눌 수 있는 경우 구하기
print(MIN)