import sys


N, M = map(int, input().split())
room = [[False] * (N + 1) for _ in range(N + 1)]
switch = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
visited = [[0] * (N + 1) for _ in range(N + 1)]
room[1][1], visited[1][1] = True, 2

for line in sys.stdin:
    x, y, a, b = map(int, line.split())
    switch[x][y].append((a, b))

queue = [(1, 1)]


while queue:
    n_queue = []

    for i, j in queue: #큐에서 모든 원소를 순회한다.
        for x, y in switch[i][j]: # 스위치를 순회하면서
            room[x][y] = True # 스위치를 켜고
            if visited[x][y] == 1: # 불이 꺼져있었다면 다시 방문할 수 있으므로
                n_queue.append((x, y)) # 다음 방문할곳에 넣어줌
        switch[i][j] = [] # 이미켰던건제거

        for ni, nj in (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1):
            # 상하좧우 돌면서
            if 0 < ni <= N and 0 < nj <= N and not visited[ni][nj]:
                if room[ni][nj]: # 불이 켜져 있다면
                    visited[ni][nj] = 2 # 방문표시후
                    n_queue.append((ni, nj)) # 큐에 넣는다.
                else: # 불이꺼져있다면
                    visited[ni][nj] = 1 #1로 표시한다.

    queue = n_queue

print(sum(map(sum, room)))