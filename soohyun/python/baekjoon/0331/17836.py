#시작 10:00
import sys
from collections import deque
MAZE = []
VISITED = []
DXY = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Knight():
    def __init__(self, x, y, sword, count):
        self.x = x
        self.y = y
        self.sword = sword
        self.count = count


def is_go(x, y, sword, count):
    global MAZE
    global VISITED
    if x < 0 or y < 0:
        return False
    elif x >= len(MAZE) or y >= len(MAZE[0]):
        return False
    return True

def is_over(cur_count, T):
    if cur_count > T:
        return True
    return False

def is_save(cur_x, cur_y, N, M):
    if cur_x == N-1 and cur_y == M-1:
        return True
    return False

def main():
    #input
    global MAZE
    global VISITED
    data = list()
    
    cur_x, cur_y, cur_count = 0, 0, 0
    N, M, T = map(int, sys.stdin.readline().strip().split(" "))
    MAZE = list()
    VISITED = list()
    queue = deque()
    for i in range(N):
        MAZE.append(list(map(int, 
                    sys.stdin.readline().rstrip().split(" "))))
        data.append([0]*M)
    VISITED.append(data)
    VISITED.append(data)

    queue.append(Knight(0, 0, False, 0))
    VISITED[0][0][0] = 1
    is_sord = False
    #bfs
    while len(queue) > 0:
        knight = queue.popleft()
        cur_x, cur_y, sword = knight.x, knight.y, knight.sword
        cur_count = knight.count
        if is_save(cur_x, cur_y, N, M):
            return cur_count
        if is_over(cur_count, T):
            continue
        for dxy in DXY:
            next_x = cur_x + dxy[0]
            next_y = cur_y + dxy[1]
            if is_go(next_x, next_y, sword, cur_count):
                #print(next_x, next_y, sword, cur_count)
                if MAZE[next_x][next_y] == 2 and not VISITED[1][next_x][next_y]:
                    queue.append(Knight(next_x, next_y, True, cur_count+1))
                elif MAZE[next_x][next_y] == 0 and not VISITED[sword][next_x][next_y]:
                    queue.append(Knight(next_x, next_y, sword, cur_count+1))
                    VISITED[sword][next_x][next_y] = cur_count + 1
                    if is_save(next_x, next_y, N, M):
                        return cur_count + 1
                elif MAZE[next_x][next_y] == 1 and not VISITED[sword][next_x][next_y]:
                    queue.append(Knight(next_x, next_y, sword, cur_count+1))
                    VISITED[sword][next_x][next_y] = cur_count + 1
                    if is_save(next_x, next_y, N, M):
                        return cur_count + 1
                    
                    
    return "Fail"
if __name__ == "__main__":
    print(main())