import sys
import heapq


def is_in_boundary(x, y, N):
    if x < 0 or y < 0:
        return False
    if x >= N or y >= N:
        return False
    return True


def is_move(x, y, bamboo, dp):
    move_list = []
    dx_list = [0, 0, -1, 1]
    dy_list = [-1, 1, 0, 0]
    for dx, dy in zip(dx_list, dy_list):
        nx = x + dx
        ny = y + dy
        if is_in_boundary(nx, ny, len(bamboo)):
            if bamboo[x][y] < bamboo[nx][ny]:
                move_list.append(dp[nx][ny])
    return move_list


def find_max_lives(dp, bamboo, start):
    max_lives = 1
    while len(start) > 0:
        _, (x, y) = heapq.heappop(start)
        move_list = is_move(x, y, bamboo, dp)
        if len(move_list) > 0:
            dp[x][y] = max(move_list) + 1
        else:
            dp[x][y] = 1
        if dp[x][y] >= max_lives:
            max_lives = dp[x][y]
    return max_lives


def main():
    start = []
    dp = []
    bamboo = []
    N = int(sys.stdin.readline())
    for i in range(N):
        bamboo_row = list(map(int,
                              sys.stdin.readline().rstrip().split(" ")))
        bamboo.append(bamboo_row)
        dp.append([0]*(N))
        for j, value in enumerate(bamboo_row):
            heapq.heappush(start, (-value, (i, j)))
    print(find_max_lives(dp, bamboo, start))


if __name__ == "__main__":
    main()
