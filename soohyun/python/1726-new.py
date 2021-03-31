import sys
class Robot():
    def __init__(self, x, y, direct, cnt):
        self.x = x
        self.y = y
        self.direct = direct
        self.cnt = cnt

DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]
VISITED = []
MAZE = []

def is_arrive(x, y, d, end_x, end_y, end_dir):
    if x == end_x and y == end_y and d == end_dir:
        return True
    return False

def is_move(x, y, M, N):
    if x < 0 or y < 0:
        return False
    if x >= M or y >= N:
        return False
    if MAZE[x][y] == 1:
        return False
    return True

def change_direction(cur_direction, rotation):
    direction = cur_direction
    if cur_direction == 1:
        if rotation == 1: direction = 4
        elif rotation == 4: directoin = 2
        elif rotation == 2: direction = 3
        elif rotation == 3: direction = 1
    elif cur_direction == 2:
        if rotation == 1: direction = 3
        elif rotation == 3: direction = 2
        elif rotation == 2: direction = 4
        elif rotation == 4: direction = 1
    return direction
    
def main():
    M, N = 0, 0
    start_x, start_y, start_dir = 0, 0, 0
    end_x, end_y, end_dir = 0, 0, 0
    queue = list()
    result = 0
    #input
    M, N = tuple(map(int, sys.stdin.readline().split(" ")))
    for i in range(M):
        row = list(map(int, sys.stdin.readline().split(" ")))
        MAZE.append(row)
    VISITED=[[[False]*5]*M]*N
    print(MAZE)
    start_x, start_y, start_dir = tuple(map(int, sys.stdin.readline().split(" ")))
    end_x, end_y, end_dir = tuple(map(int, sys.stdin.readline().split(" ")))  
    #bfs
    x, y = start_x, start_y
    loc = Robot(x-1, y-1, start_dir, 0)
    queue.append(loc)  
    while len(queue) > 0:
        cur_loc = queue.pop(0)
        x, y, direction = cur_loc.x, cur_loc.y, cur_loc.direct
        print("direction", x, y, direction)
        if is_arrive(x, y, direction, end_x, end_y, end_dir):
            result = cur_loc.cmd_count
            print("arrive!")
            break
        for i in range(1, 4):
            nx = x + DX[direction] * i
            ny = y + DY[direction] * i

            if not is_move(nx, ny, M, N):
                continue                

            if not VISITED[nx][ny][direction]:
                print("move", nx, ny, M, N, VISITED[nx][ny][direction])
                queue.append(Robot(nx, ny, 
                                  direction, 
                                  cur_loc.cnt+1))
                VISITED[x][y][direction] = True

        for i in range(1, 3):
            next_direction = change_direction(i, direction)
            if not VISITED[x][y][next_direction]:
                queue.append(Robot(x, y, 
                                  next_direction, 
                                  cur_loc.cnt+1))
                VISITED[x][y][next_direction] = True
    print(result)
if __name__ == "__main__":
    main()