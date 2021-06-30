# 걸린시간 3시간 10분
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

DIRECTION = {0: (-1, 0), 1:(0, 1), 2: (1, 0), 3:(0, -1)}
class Robot:
    def __init__(self, loc, direction, count, robot_change):
        self.loc = loc
        self.direction = direction
        self.count = count
        self.robot_change = robot_change
    
    def __str__(self):
        return f'{self.loc} {self.direction} {self.count} {self.robot_change}'


def is_inrange(nr, nc, height, width):
    if nr >= 0 and nr < height and nc >= 0 and nc < width:
        return True
    return False


def print_arr(arr):
    for i, _ in enumerate(arr):
        print(*arr[i])


def cleaner(maze, robot):
    height, width = len(maze), len(maze[0])
    visited = deepcopy(maze)#[[0]*width for _ in range(height)]
    visited[robot.loc[0]][robot.loc[1]] = 2
    queue = deque()
    queue.append(robot)

    while len(queue) > 0:
        robot = queue.popleft()
        row, col = robot.loc
        nd = (4 + (robot.direction - 1)) % 4
        nr, nc = row + DIRECTION[nd][0], col + DIRECTION[nd][1]

        if is_inrange(nr, nc, height, width):
            #  다음으로 갈곳이청소가 이미 되어있거나 벽인 경우에는
            if visited[nr][nc] >= 1 or maze[nr][nc] == 1:
                # 네방향 모두 청소되어 있는경우
                if robot.robot_change >= 4:
                    # 바라보는 방향을 유지하면서 후진한다.
                    nr, nc = row - DIRECTION[robot.direction][0], col - DIRECTION[robot.direction][1]
                    if is_inrange(nr, nc, height, width):
                        # 뒤쪽이 벽이라 후진이 불가능한경우
                        if maze[nr][nc] == 1:
                            break
                        # 후진한다.
                        queue.append(Robot((nr, nc), robot.direction, 
                                            robot.count, 
                                            0))
                # 네방향 모두 청소되어있지 않으면
                else:
                    # 방향을 돌리고 2번으로 돌아간다.
                    queue.append(Robot((row, col), nd, 
                                        robot.count, 
                                        robot.robot_change+1))
            else:
                visited[nr][nc] = 2
                queue.append(Robot((nr, nc), nd, 
                                    robot.count + 1, 
                                    0)) 
    return robot.count


def input_values():
    height, _ = map(int, input().rstrip().split(" "))
    row, col, direction = map(int, input().rstrip().split(" "))
    maze = [ list(map(int, input().rstrip().split(" "))) for _ in range(height)]
    robot = Robot((row, col), direction, 1, 0)
    return maze, robot


def main():
    maze, robot = input_values()
    print(cleaner(maze, robot))


if __name__ == "__main__":
    main()
