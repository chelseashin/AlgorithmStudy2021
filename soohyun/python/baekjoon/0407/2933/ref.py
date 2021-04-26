import sys
import heapq
CAVE = []
DR = [-1, 1, 0, 0]
DL = [0, 0, -1, 1]


def get_mineral(start, step):
    y, x = start
    while 0 <= x < len(CAVE[0]):
        if CAVE[y][x] == 'x':
            return (y, x)
        x += step


def dfs(start, cluster, visited):
    global CAVE
    sr, sc = start
    floating = False
    visited[sr][sc] = True
    if sr not in cluster:
        cluster[sc] = [-sr]
    else:
        heapq.heappush(cluster[sc], -sr)
    if sr == len(CAVE):
        floating = False
    for dr, dl in zip(DR, DL):
        nr = sr + dr
        nc = sc + dl
        if 0 <= nr < len(CAVE) and 0 <= nc < len(CAVE[0]):
            if CAVE[nr][nc] == 'x' and not visited[nr][nc]:
                dfs((nr, nc), cluster, visited)
    return floating, cluster


def get_gap(row, col):
    for i in range(row, len(CAVE)):
        if i+1 == len(CAVE) or CAVE[i+1][col] == 'x':
            return i-row


def get_min_gap(cluster):
    min_gap = len(cluster)
    for x in cluster:
        y = -cluster[x][0]
        gap = get_gap(y, x)
        min_gap = min(min_gap, gap)
    return min_gap


def down(cluster):
    global CAVE
    min_gap, cluster = get_min_gap(cluster)
    for x in cluster:
        while cluster[x]:
            y = -heapq.heappop(cluster[x])
            CAVE[y][x] = '.'
            CAVE[y + min_gap][x] = 'x'


def start_fight(cav_size, stick_heights):
    row, col = cav_size
    for index, mineral in enumerate(stick_heights):
        nr = row - mineral
        nc = 0 if index % 2 == 0 else col - 1
        step = 1 if index % 2 == 0 else col - 1
        start_cluster = get_mineral((nr, nc), step)
        if not start_cluster: 
            continue
        mr, mc = start_cluster
        CAVE[mr][mc] = '.'
        for r, c in zip(DR, DL):
            nr = mr + r
            nc = mc + c
            if 0 <= nr < r and 0 <= nc < c:
                if CAVE[nr][nc] == 'x':
                    cluster = dict()
                    visited = [[False] * col for _ in range(row)]
                    floating, cluster = dfs((nr, nc), cluster, visited)
                    if floating:
                        down(cluster)
             

def print_cave():
    global CAVE
    for i in range(len(CAVE)):
        for j in range(len(CAVE[i])):
            print(CAVE[i][j], end='')
    print("====end===")


def main():
    global CAVE
    cave_size = tuple(map(int, sys.stdin.readline().strip().split(" ")))
    for _ in range(cave_size[0]):
        single_row = sys.stdin.readline()
        CAVE.append(list(single_row))
    _ = map(int, sys.stdin.readline().strip())
    height = list(map(int, sys.stdin.readline().strip().split(" ")))
    #print_cave()
    start_fight(cave_size, height)
    print_cave()



if __name__ == "__main__":
    main()