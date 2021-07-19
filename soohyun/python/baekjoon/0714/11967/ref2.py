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

    for i, j in queue:
        for x, y in switch[i][j]:
            room[x][y] = True
            if visited[x][y] == 1:
                n_queue.append((x, y))
        switch[i][j] = []

        for ni, nj in (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1):
            if 0 < ni <= N and 0 < nj <= N and not visited[ni][nj]:
                if room[ni][nj]:
                    visited[ni][nj] = 2
                    n_queue.append((ni, nj))
                else:
                    visited[ni][nj] = 1

    queue = n_queue

print(sum(map(sum, room)))