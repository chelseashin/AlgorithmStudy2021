# 문제
from collections import deque
import heapq
import sys
input = sys.stdin.readline

def bfs(start_loc, maze, height, width, shark):
    visited = {start_loc}
    count, fish = 0, 0
    shark_size = shark
    queue = [(count, start_loc[0], start_loc[1], fish)]
    while queue:
        count, row, col, fish = heapq.heappop(queue)
        #print(count, row, col, fish, shark_size)
        if fish > 0:
            maze[row][col] = 0
            return fish, row, col, count
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr = row + dr
            nc = col + dc
            if 0 <= nr < height and 0 <= nc <width:
                if (nr, nc) in visited:
                    continue
                if shark_size >= maze[nr][nc]:
                    visited.add((nr, nc))
                    if maze[nr][nc] == 0 or shark_size == maze[nr][nc]:
                        heapq.heappush(queue, (count+1, nr, nc, fish))
                    else:
                        heapq.heappush(queue, (count+1, nr, nc, fish+1))
    return fish, start_loc[0], start_loc[1], count


def print_maze(maze):
    print("==start==")
    for i in range(len(maze)):
        print(*maze[i])


def count_shark_eat(maze, height, width, start_loc):
    time_eat = 0
    shark_size = 2
    current_eat = 0
    while True:
        eat_fish, row, col, time = bfs(start_loc, maze, height, width, shark_size)

        if eat_fish == 0:
            break
        else:        
            current_eat += 1

        if current_eat == shark_size:
            current_eat = 0
            shark_size += 1

        time_eat += time
        start_loc = (row, col)

    return time_eat

def main():
    start_loc = tuple()
    maze = list()
    N = int(input().rstrip())
    for i in range(N):
        rows = list(map(int, input().rstrip().split(" ")))
        maze.append(rows)
        for j, _ in enumerate(rows):
            if maze[i][j] == 9:
                start_loc = (i, j)
    maze[start_loc[0]][start_loc[1]] = 0
 
    print(count_shark_eat(maze, N, N, start_loc))


if __name__ == "__main__":
    main()