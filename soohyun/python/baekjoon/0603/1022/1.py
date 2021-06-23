import sys
input = sys.stdin.readline

direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def is_in_range(num_range, row, col):
    r1, c1, r2, c2 = tuple(num_range)
    if r1 <= row <= r2 and c1 <= col <= c2:
        return True
    return False


def make_snail(N, num_range):
    didx = 0
    count = 1
    row, col = N//2, N//2
    maze = [[0]*N for _ in range(N)]
    maze[row][col] = count
    max_in_range = 0
    

    for i in range(2, N+1):
        for _ in range(2):
            for k in range(i):
                if k == 0:
                    continue
                row += direct[didx][0]
                col += direct[didx][1]
                count += 1
                maze[row][col] = count
                if is_in_range(num_range, row, col):
                    max_in_range = max(max_in_range, count)
            didx = (didx + 1) % 4
    
    for k in range(i):
        if k == 0:
            continue
        row += direct[didx][0]
        col += direct[didx][1]
        count += 1
        maze[row][col] = count
        if is_in_range(num_range, row, col):
            print(1)
            max_in_range = max(max_in_range, count)

    return maze, max_in_range


def change_axis(N, i):
    return N + i


def print_maze(maze, max_in_range, num_range):
    r1, c1, r2, c2 = tuple(num_range)
    max_len = len(str(max_in_range))
    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            left_blank = max_len - len(str(maze[row][col]))
            blank = ''
            for _ in range(left_blank):
                blank += ' '
            print(blank + '{}'.format(maze[row][col]), end=" ")
        print("")
            


def main():
    rc_list = list(map(int, input().rstrip().split(" ")))
    abs_list = list(map(abs, rc_list))
    max_num = max(abs_list)
    N = max_num * 2 + 1

    if sum(rc_list) != sum(abs_list):
        num_range = [change_axis(max_num, i) for i in rc_list]
    else:
        num_range = rc_list

    maze, max_in_range = make_snail(N, num_range)
    print_maze(maze, max_in_range, num_range)


if __name__ == "__main__":
    main()
