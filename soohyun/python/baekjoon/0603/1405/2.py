import sys
import heapq
input = sys.stdin.readline

def bfs(maze,num):
    visited = dict()
    queue = [(0, 0, 0, 0)]
    visited[(0, 0)] = True
    while queue:
        break_wall, count, row, col = heapq.heappop(queue)
        if row == num-1 and col == num-1:
            return break_wall
        for i, j in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nrow = row + i
            ncol = col + j
            if 0 <= nrow < num and 0 <= ncol < num:
                if not visited.get((nrow, ncol), False):
                    visited[(nrow, ncol)] = True
                    if maze[nrow][ncol] == '1':
                        heapq.heappush(queue, (break_wall, count-1, nrow, ncol))
                    else:
                        heapq.heappush(queue, (break_wall+1, count-1, nrow, ncol))
    return 0



def main():
    num = int(input())
    maze = [input() for _ in range(num)]
    return bfs(maze, num)
    

if __name__ == "__main__":
    print(main())