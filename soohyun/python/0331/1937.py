#시작 10시 27분
#끝 12시 05분
import sys
import heapq

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]


def is_angry(cur_bamboo, nextbamboo):
    if nextbamboo <= cur_bamboo:
        return True
    return False


def is_go(nx, ny, N):
    if nx < 0 or ny < 0:
        return False
    if nx >= N or ny >= N:
        return False
    return True


def is_visited(next_visited, cur_visited):
    if next_visited > cur_visited:
        return True
    return False


def calc_max_live(start, bamboo, visited):
    max_live = -1
    queue = list()
    while len(start) > 0:
        num_of_bamboo, start_axis = heapq.heappop(start)
        x, y = start_axis[0], start_axis[1]
        if visited[x][y] >= 1:
            continue
        visited[x][y] = 1
        queue.append((num_of_bamboo, (x, y), 1))
        while len(queue) > 0:
            num_of_bamboo, axis, live = queue.pop(0)
            if max_live <= live:
                max_live = live
            for dx, dy in zip(DX, DY):
                nx = axis[0] + dx
                ny = axis[1] + dy
                if is_go(nx, ny, len(bamboo)):
                    next_bamboo = bamboo[nx][ny]
                    if is_angry(num_of_bamboo, next_bamboo):
                        continue
                    if is_visited(visited[nx][ny],
                                  visited[axis[0]][axis[1]]):
                        continue
                    visited[nx][ny] = live + 1
                    queue.append((next_bamboo, (nx, ny), live+1))
    return max_live


def main():
    # input
    bamboo = list()
    visited = list()
    start = []  # heapq 넣을곳
    N = int(sys.stdin.readline())
    for i in range(N):
        bamboo_row = list(map(int,
                          sys.stdin.readline().rstrip().split(" ")))
        bamboo.append(bamboo_row)
        visited.append([0]*N)
        for j, value in enumerate(bamboo_row):
            heapq.heappush(start, (value, (i, j)))

    # start
    print(calc_max_live(start, bamboo, visited))


if __name__ == "__main__":
    main()
