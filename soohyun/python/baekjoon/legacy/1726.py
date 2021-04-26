#시작 15시 55분
# 끝 
import sys
import time
DIRMAP = {1:(0, -1),  2:(0, 1), 3:(1, 0), 4:(-1, 0)}
DIRECTION = ["CHANGE", "GO"]
MAZE = list()
VISITED = list()
class Location():
    def __init__(self, cur_x, cur_y, direction, cmd_count, go_count):
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.direction = direction
        self.all_count = all_count
        self.go_count = go_count


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

def turn_left(direction):
    return 4 - ((direction-1) % 4)

def turn_right(direction):
    return 4 - ((direction+1) % 4)

def main():
    M, N = 0, 0
    start_x, start_y, start_dir = 0, 0, 0
    end_x, end_y, end_dir = 0, 0, 0
    queue = list()
    result = 0
    visited = list()
    #input
    M, N = tuple(map(int, sys.stdin.readline().split(" ")))
    for i in range(M):
        row = list(map(int, sys.stdin.readline().split(" ")))
        MAZE.append(row)
        VISITED.append(row)
        
    start_x, start_y, start_dir = tuple(map(int, sys.stdin.readline().split(" ")))
    end_x, end_y, end_dir = tuple(map(int, sys.stdin.readline().split(" ")))
    # bfs
    x, y = start_x, start_y
    loc = Location(x, y, start_dir, 0)
    queue.append(loc)
    while len(queue) > 0:
        cur_loc = queue.pop(0)
        x, y, direction = cur_loc.cur_x, cur_loc.cur_y, cur_loc.direction
        VISITED[x][y] = cur_loc.cmd_count
        if is_arrive(x, y, direction, end_x, end_y, end_dir):
            result = cur_loc.cmd_count
            break
        for direct in DIRECTION:
            if direct == "GO":
                x += DIRMAP[cur_loc.direction][0]
                y += DIRMAP[cur_loc.direction][1]
                if is_move(x, y, M, N) and VISITED[x][y] =< cur_loc.cmd_count:
                    time.sleep(3)
                    queue.append(Location(x, y, direction, cur_loc.cmd_count+1))
            else:
                queue.append(Location(x, y, turn_left(direction), cur_loc.cmd_count+1))
                queue.append(Location(x, y, turn_right(direction), cur_loc.cmd_count+1))

    print(result)

if __name__ == "__main__":
    main()