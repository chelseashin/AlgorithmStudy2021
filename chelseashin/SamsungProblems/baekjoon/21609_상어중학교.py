# 22:36 start
# 23:54 bfs, pq 구현

from sys import stdin
input = stdin.readline
from collections import deque
from heapq import heappush, heappop

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 시작 위치, 시작번호, 그릴 번호
def bfs(sr, sc, temp, num):
    print("sr sc", (sr, sc), "시작번호 temp", temp, "그릴 번호 num", num)
    Q = deque([(sr, sc)])
    visited[sr][sc] = num
    blockCnt = 1
    rainbowCnt = 0
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 격자 밖이거나 검은색 블록이면
            if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc] == -1:
                continue
            # 이미 방문했거나 다른 숫자이면
            if visited[nr][nc] == num or (A[nr][nc] > 0 and A[nr][nc] != temp):
                continue
            print("들어올 수 있는 nr, nc", (nr, nc), A[nr][nc], visited[nr][nc])
            if A[nr][nc] == temp or A[nr][nc] == 0:
                visited[nr][nc] = num
                Q.append((nr, nc))
                blockCnt += 1
                if A[nr][nc] == 0:
                    rainbowCnt += 1
        print("QQQQQQQQQ", Q)
    print("(sr, sc) 결과 blockCnt", blockCnt, "rainbowCnt", rainbowCnt, (sr, sc))
    heappush(pq, (-blockCnt, -rainbowCnt, sr, sc))
    print()
    return 


def findMaxBlockGroup():
    print("findMaxBlockGroup 시작")
    num = 1
    for r in range(N):
        for c in range(N):
            # 검은/무지개 블록이거나 이미 방문했으면
            if A[r][c] == -1 or A[r][c] == 0 or visited[r][c]:
                continue
            print("start r c", (r, c))
            bfs(r, c, A[r][c], num)
            num += 1
            print("visited ===========================")
            for row in visited:
                print(row)
        
        print("우선순위q", pq)
        print()
        if r == 2:
            break        
            

# main
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for row in A:
    print(row)

score = 0
existBlockGroup = True
while existBlockGroup:
    visited = [[0] * N for _ in range(N)]
    pq = []
    findMaxBlockGroup()
    break