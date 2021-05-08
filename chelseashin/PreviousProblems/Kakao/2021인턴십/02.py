# 14:48 pass
from collections import deque
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)   # 상하좌우

def bfs(sr, sc, A):
    visited = [[-1] * 5 for _ in range(5)]
    visited[sr][sc] = 0
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 격자 밖이거나 이미 방문했으면
            if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc] > -1:
                continue
            # 파티션이거나 다음 이동할 곳이 3이면
            if A[nr][nc] == "X" or visited[r][c] + 1 == 3: 
                continue
            if A[nr][nc] == "P":    # 거리두기 못 지킴
                return 0
            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))
    return 1

def solution(places):
    answer = []
    for place in places:    # 대기실 별로
        available = 1       # 거리두기 잘 지켰는지 
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P":
                    available = bfs(r, c, place)
                    if not available: break
            if not available: break
        answer.append(available)
    return answer