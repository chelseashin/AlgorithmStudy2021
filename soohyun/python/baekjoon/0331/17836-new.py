import sys
from collections import deque

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


def bfs(sword, n, m, limit, MAZE, VISITED):
    queue = list()
    VISITED[0][0] = 1
    queue.append((0, 0))
    while(len(queue) > 0):
        x, y = queue.pop(0)
        if(MAZE[x][y] == 2):
            sword = n-1-x + m-1-y + VISITED[x][y] - 1  # 맨하탄 거리
        if(x == n-1 and y == m-1):
            return min(VISITED[x][y]-1, sword)
        for k in range(4):
            nx = x + DX[k]
            ny = y + DY[k]
            if(0<=nx<n and 0<=ny<m and MAZE[nx][ny] != 1):
                if(VISITED[nx][ny] == 0):
                    queue.append((nx, ny))
                    VISITED[nx][ny] = VISITED[x][y] + 1
    return sword


def main():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    n, m, limit = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    sword = 1000000
    res = bfs(sword, n, m, limit, arr, visited)
    if res > limit:
        return "FAIL"
    return res


if __name__ == "__main__":
   print(main())

