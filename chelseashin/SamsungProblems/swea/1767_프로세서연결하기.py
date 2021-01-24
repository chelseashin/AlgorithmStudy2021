# 약 2시간..? 소요
# 사용 알고리즘 : dfs
# 변수명 짓는 데 일관성 있게,, 자꾸 헷갈림

import sys
sys.stdin = open("1767_input.txt")

# 4방향
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def connect(r, c, d):
    cnt = 0
    while True:
        r += dr[d]
        c += dc[d]
        if not (0 <= r < N and 0 <= c < N):
            return cnt
        if A[r][c]:     # 코어에 해당하거나 다른 전선이 연결된 자리라면
            return 0
        A[r][c] = 2         # 연결하는 부분 2로 표시
        cnt += 1

# 현재 체크한 코어 수, 전선 연결한 코어 수, 연결한 전선 길이의 합
def dfs(depth, connectedCores, connectedlength):
    global A, minLength, maxCores
    if depth == coreCnt:
        if connectedCores < maxCores:   # 연결한 갯수가 최대 연결 갯수보다 이미 작으면
            return
        # 연결 갯수가 최대 연결 갯수보다 크다면
        if connectedCores > maxCores:
            maxCores = connectedCores
            minLength = connectedlength
        # 연결 갯수가 최대 연결 갯수와 같다면 최소 연결 길이 갱신
        elif connectedCores == maxCores:
            minLength = min(minLength, connectedlength)
        return minLength

    arr = [x[:] for x in A]         # 이전 상태 저장
    sr, sc = coreLst[depth]         # 연결 시도할 코어 위치
    for d in range(4):
        temp = connect(sr, sc, d)   # 코어 위치, 방향 넘겨주면 가장자리까지의 거리 리턴
        if temp:                    # 연결 가능하면
            dfs(depth+1, connectedCores+1, connectedlength+temp)
        A = [x[:] for x in arr]     # 연결한 상태니까 복원

    dfs(depth+1, connectedCores, connectedlength)   # 연결 실패하면

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    coreLst = []    # 코어 위치 좌표 담기
    coreCnt = 0     # 코어 갯수
    for i in range(1, N-1):
        for j in range(1, N-1):
            if A[i][j]:
                coreLst.append((i, j))
                coreCnt += 1
    maxCores = 0                # 연결한 코어의 수 - 최댓값 갱신용
    minLength = float('inf')    # 전선 길이의 합 - 최솟값 갱신용
    dfs(0, 0, 0)
    print("#{} {}".format(tc+1, minLength))