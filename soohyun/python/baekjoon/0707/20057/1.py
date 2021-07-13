import sys
input = sys.stdin.readline
BLOW = {(1, 0):0.01, (-1, 0):0.01,
        (1, -1):0.07, (-1, -1):0.07,
        (2, -1):0.02, (-2, -1):0.02,
        (1, -2):0.1, (-1, -2):0.1,
        (0, -3):0.05, (0, -2): 0.55}


def is_in_range(nr, nc, N):
    if 0 <= nr < N and 0 <= nc <N:
        return True
    return False


def blow_sand(count, sand, maze, start_loc, N):
    out_sand = 0
    left_sand = sand
    for direction, percentage in BLOW.items():
        if count == 1:
            dr, dc = -direction[1], -direction[0]
        elif count == 2:
            dr, dc = direction[0], -direction[1]
        elif count == 3:
            dr, dc = direction[1], direction[0]
        else:
            dr, dc = direction
        nr, nc = start_loc[0] + dr, start_loc[1] + dc
        blow_sand = int(sand * percentage)
        #print(nr, nc, blow_sand, percentage)
        if percentage == 0.55:
            if is_in_range(nr, nc, N):
                maze[nr][nc] += left_sand
            else:
                out_sand += left_sand
        else:
            left_sand = left_sand - blow_sand
            if is_in_range(nr, nc, N):
                maze[nr][nc] += blow_sand
            else:
                out_sand += blow_sand
    return out_sand


def print_maze(maze):
    print("====start====")
    for row in maze:
        print(*row)
    print("=====end=====")


def start_tornado(maze, N):
    start = ((N-1)//2, (N-1)//2)
    count = 0
    sand_count = 0
    # 좌 하 우 상
    #print_maze(maze)
    direction = [(0, 1, 0, -1), (-1, 0, 1, 0)]
    for i in range(1, N+1):
        repeat = 2 if i < N else 1
        for _ in range(repeat):
            for _ in range(i):
                #print(start, sand_count)
                nr = start[0] + direction[0][count]
                nc = start[1] + direction[1][count]
                sand = maze[nr][nc]
                maze[nr][nc] = 0
                # 모래 흩날려야함
                sand_count += blow_sand(count, sand, maze, start, N)
                #print_maze(maze)
                start = (nr, nc)
            count = (count + 1) % 4
    return sand_count

def main():
    N = int(input())
    maze = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    print(start_tornado(maze, N))


if __name__ == "__main__":
    main()