from collections import deque


def out(pos):
    y, x = pos
    if 0 <= y < n and 0 <= x < n:
        return False
    return True


def bfs(start_list):
    wall_set = set()
    for start in start_list:
        y, x = start
        q = deque()
        q.append((y, x))
        visited[y][x] = True
        while q:
            i, j = q.popleft()
            for k in range(4):
                new_i = i + dy[k]
                new_j = j + dx[k]
                if new_i == n-1 and new_j == n-1:
                    return
                if not out((new_i, new_j)):
                    if not visited[new_i][new_j]:
                        visited[new_i][new_j] = True
                        if board[new_i][new_j] == 1:
                            q.append((new_i, new_j))
                        elif board[new_i][new_j] == 0:
                            wall_set.add((new_i, new_j))
    return list(wall_set)


def init():
    n = int(input(''))
    board = []
    visited = []
    for i in range(n):
        temp_list = list(map(int, input('')))
        board.append(temp_list)
        visited.append([False] * n)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    return n, board, 0, visited, dx, dy


n, board, count, visited, dx, dy = init()
pos_list = [(0, 0)]
while True:
    pos_list = bfs(pos_list)
    if not pos_list:
        break
    count += 1
print(count)