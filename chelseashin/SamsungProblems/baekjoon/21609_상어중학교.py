# 22:36 start
# 23:54 bfs, pq 구현
# 25:24 tc 1개 틀림..
# 39%에서 IndexError ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ 대체 뭘까요
# 디버깅만 2시간.... 오늘은 여기까지
# 다음 날 내 힘으로 pass!!!!!!!!!!! 우선순위 큐에 값이 없는 경우를 고려하니 정답.

from sys import stdin
input = stdin.readline
from collections import deque
from heapq import heappush, heappop

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 시작 위치, 시작번호, 그릴 번호
def bfs(sr, sc, num):
    temp = A[sr][sc]
    Q = deque([(sr, sc)])
    visited[sr][sc] = num
    blockCnt, rainbowCnt = 1, 0
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N): continue # 격자 밖
            # 이미 방문했거나 검은색 블록 / 빈 공간이면
            if visited[nr][nc] == num or A[nr][nc] <= -1:
                continue
            # 같은 숫자이거나 무지개 블록이면
            if A[nr][nc] == temp or A[nr][nc] == 0:
                visited[nr][nc] = num   # 방문 표시
                Q.append((nr, nc))      # 큐에 담기
                blockCnt += 1           # 블록 갯수 += 1
                if A[nr][nc] == 0:
                    rainbowCnt += 1     # 무지개 블록 갯수
    # (가장 큰 블록 그룹 > 무지개 블록 수 많은 것 > 행이 가장 큰 것 > 열이 가장 큰 것)
    heappush(pq, (-blockCnt, -rainbowCnt, -sr, -sc))
    return

def removeBlocks(sr, sc):
    start = A[sr][sc]
    A[sr][sc] = -2          # 첫 위치 맵에 -2로 표시(빈 공간)
    visited[sr][sc] = -1    # 첫 위치 -1로 방문 표시(visited 재사용)
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N): continue     # 격자 밖
            # 빈 공간/검은 블록이거나 이미 방문한 곳이면               
            if A[nr][nc] <= -1 or visited[nr][nc] == -1: continue
            # 같은 숫자 블록이거나 무지개 블록이면
            if A[nr][nc] == start or A[nr][nc] == 0:
                A[nr][nc] = -2          # 지운 곳 표시
                visited[nr][nc] = -1    # 방문 표시
                Q.append((nr, nc))      # 재탐색을 위해 큐에 담기

def findMaxBlockGroup():
    global score, blockGroup
    num = 1
    for r in range(N):
        for c in range(N):
            # 검은 블록/빈 공간이거나 무지개 블록이거나 이미 방문했으면
            if A[r][c] <= -1 or A[r][c] == 0 or visited[r][c]:
                continue
            if 1 <= A[r][c] <= M:
                bfs(r, c, num)
                num += 1

    if pq:      # 우선순위 큐에 값이 있는 경우에만
        blockCnt, rainbowCnt, row, col = heappop(pq)    # 최대 힙
        if -blockCnt >= 2:   # 그룹에 속한 블록의 개수는 2보다 크거나 같아야 함
            score += blockCnt ** 2  	# 점수 더하기
            removeBlocks(-row, -col)
        else:
            blockGroup = False      # 가장 블록 그룹이 2보다 작음 => 불가능
    else:
        blockGroup = False          # 블록 그룹 없음 => 불가능

def gravity():
    for c in range(N):
        blocks = deque()
        sr, sc = N-1, c
        for r in range(N-1, -1, -1):
            if A[r][c] >= 0:    # 블록 or 일반 블록이면
                blocks.append(A[r][c])      # 블록 큐에 추가
                A[r][c] = -2    # 빈 공간으로 만들기
            if A[r][c] == -1:
                while blocks:   # 큐에 값이 있는 동안 pop하며 해당 열에 값 채우기
                    A[sr][sc] = blocks.popleft()
                    sr -= 1
                blocks = deque()    # 큐 비우기
                sr = r-1
        if blocks:          # 마지막 부분 마저 값 채우기
            while blocks:
                A[sr][sc] = blocks.popleft()
                sr -= 1

def turnLeft90():
    newA = []
    for c in range(N-1, -1, -1):
        col = []
        for r in range(N):
            col.append(A[r][c])
        newA.append(col)
    return newA

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

score = 0
blockGroup = True    # 블록 그룹 존재 여부
while True:
    visited = [[0] * N for _ in range(N)]
    pq = []
    findMaxBlockGroup()    # 가장 큰 블록그룹 찾기 
    if not blockGroup:     # 종료 조건
        break
    gravity()           # 중력
    A = turnLeft90()    # 반시계방향으로 90도 회전
    gravity()           # 중력
print(score)