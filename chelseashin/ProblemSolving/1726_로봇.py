# 21:10 start
# 22:32 16%에서 틀림..
# 22:46 75%에서 틀림..
# 22:56 pass..
# 참고.. https://rebas.kr/742


from sys import stdin
input = stdin.readline
from collections import deque

# 동 서 남 북
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

def bfs():
    visited = [[[0] * 4 for _ in range(N)] for _ in range(M)]
    Q = deque([(sr-1, sc-1, sd-1)])
    while Q:
        r, c, d = Q.popleft()
        if (r, c, d) == (gr-1, gc-1, gd-1):
            print(visited[r][c][d])
            # for vi in visited:
            #     print(vi)
            return
        # 직진
        for i in range(1, 4):
            nr = r + dr[d] * i
            nc = c + dc[d] * i
            if not (0 <= nr < M and 0 <= nc < N):
                break
            if A[nr][nc]:
                break
            if not visited[nr][nc][d]:
                Q.append((nr, nc, d))
                visited[nr][nc][d] = visited[r][c][d] + 1
        
        # 방향전환
        for i in range(4):
            if i == d:      # 같은 방향이면
                continue
            # 다른 방향일 때
            if (d+i) % 4 == 1:   # 180도 회전이면(남<=>북, 동<=>서)
                k = 2            # 동작 2번
            else:
                k = 1            # 동작 1번
            # k = 2 if (i+d) % 4 == 1 else 1
            if not visited[r][c][i]:
                Q.append((r, c, i))
                visited[r][c][i] = visited[r][c][d] + k

# main
M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
sr, sc, sd = map(int, input().split())
gr, gc, gd = map(int, input().split())

bfs()
# print(0%4, 1%4, 2%4, 3%4, 4%4)
# print(2%4, 3%4, 5%4)
# print(3%4, 4%4, 5%4)