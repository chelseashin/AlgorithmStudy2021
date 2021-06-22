import sys
input = sys.stdin.readline

direct = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def is_in_range(num_range, row, col):
    r1, c1, r2, c2 = tuple(num_range)
    if r1 <= row <= r2 and c1 <= col <= c2:
        return True
    return False


def make_snail(N, num_range, r_len, c_len):
    didx = 0
    count = 1
    row, col = N//2, N//2
    cr, cc = num_range[0], num_range[1]
    maze = [[0]*c_len for _ in range(r_len)]
    if is_in_range(num_range, row, col):
        maze[row-cr][col-cc] = count 
    max_in_range = 0
    last_idx = 0


    for i in range(2, N+1):
        for _ in range(2):
            for k in range(i):
                if k == 0:
                    continue
                row += direct[didx][0]
                col += direct[didx][1]
                count += 1
                if is_in_range(num_range, row, col):
                    maze[row-cr][col-cc] = count
                    max_in_range = max(max_in_range, count)

            didx = (didx + 1) % 4
        last_idx = i
    for k in range(last_idx):
        if k == 0:
            continue
        row += direct[didx][0]
        col += direct[didx][1]
        count += 1
        
        if is_in_range(num_range, row, col):
            max_in_range = max(max_in_range, count)
            maze[row-cr][col-cc] = count

    return maze, max_in_range


def change_axis(N, i):
    return N + i


def print_maze(maze, max_in_range, r_len, c_len):
    max_len = len(str(max_in_range))
    for row in range(r_len):
        for col in range(c_len):
            left_blank = max_len - len(str(maze[row][col]))
            blank = ''
            #for _ in range(left_blank):
            #    blank += ' '
            print(str(maze[row][col]).rjust(max_len), end=' ')
            #print(blank + '{}'.format(maze[row][col]), end=" ")
        print("")
            


def main():
    rc_list = list(map(int, input().rstrip().split(" ")))
    abs_list = list(map(abs, rc_list))
    max_num = max(abs_list)
    N = max_num * 2 + 1
    r_len, c_len = rc_list[2] - rc_list[0] + 1, rc_list[3] - rc_list[1] + 1
    num_range = [change_axis(max_num, i) for i in rc_list]


    maze, max_in_range = make_snail(N, num_range, r_len, c_len)
    print_maze(maze, max_in_range, r_len, c_len)


if __name__ == "__main__":
    main()
