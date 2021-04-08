# 21:00 start
# 21:28 이제야 input 받음..... 하
# 21:30 풀기 시작
# 22:15 finish 시간 2위 달성..ㅎ
# 일반적인 BFS에 윗층, 아랫층까지 포함해 총 6방향으로 가능한 다음 위치를 퍼트린다.
# 출력 시 문장 끝에 "." 안 찍어서 한번 틀림 ㅋㅋㅋ 문장 출력할 일 있으면 그냥 복붙하자.

from sys import stdin
input = stdin.readline
from collections import deque

dl = (-1, 1, 0, 0, 0, 0)
dr = (0, 0, -1, 1, 0, 0)
dc = (0, 0, 0, 0, -1, 1)

def bfs():
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited[sl][sr][sc] = 1
    Q = deque([(sl, sr, sc)])
    while Q:
        l, r, c = Q.popleft()
        for d in range(6):
            nl = l + dl[d]
            nr = r + dr[d]
            nc = c + dc[d]
            # 범위 밖이거나
            if not (0 <= nl < L and 0 <= nr < R and 0 <= nc < C):
                continue
            # 이미 방문했거나 벽이면
            if visited[nl][nr][nc] or B[nl][nr][nc] == "#":
                continue
            # 도착지면 출력 후 리턴
            if B[nl][nr][nc] == "E":
                print("Escaped in {} minute(s).".format(visited[l][r][c]))
                return
            # 가능한 다음 위치에 거리 표시하고 큐에 담기
            visited[nl][nr][nc] = visited[l][r][c] + 1
            Q.append((nl, nr, nc))
    
    print("Trapped!")   # 불가능한 경우

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    B = []      # 빌딩 3차원 배열로 표현
    sl, sr, sc = -1, -1, -1     # 시작 좌표
    for l in range(L):
        B.append([list(input().rstrip()) for _ in range(R)])
        for r in range(R):
            for c in range(C):
                if B[l][r][c] == "S":
                    sl, sr, sc = l, r, c
        input()
    bfs()