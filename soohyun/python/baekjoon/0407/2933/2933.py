# 시작 10시 26분
# 문제해석시간 11tl 16분
# 점심 2시 13분
# 코드생각시간 2시 46분
# 코드만드는시간 3시 31분
# 디버깅 시간  3시 57분 
# 휴식 4시 59분
# 디버깅 시간 5시 42분
# 상하좌우를 다 큐에 따로 담야아해
# 디버깅시간 06시 18분
# 오류잡는시간 7시 17분

import sys

CAVE = []
DR = [-1, 1, 0, 0]
DL = [0, 0, -1, 1]
DEBUG = False


def is_in_cave(col):
    if col < 0 or col >= len(CAVE[0]):
        return False
    return True


def is_go(row, col):
    if not is_in_cave(col):
        return False
    if row < 0 or row >= len(CAVE):
        return False
    if CAVE[row][col] == '.':
        return False
    return True


def remove_mineral(row, direct, row_size):
    global CAVE
    start, direction = direct
    while is_in_cave(start) and CAVE[row_size-row][start] == '.':
        start = start + direction
    if is_in_cave(start):
        CAVE[row_size-row][start] = '.'
        return row_size-row, start
    else:
        return None, None


def bfs(start, visited):
    global CAVE
    global DEBUG
    #print("start", start)
    cluster = dict()
    queue = [start]

    cluster[start[1]] = [start[0]]
    is_attach_floor = False
    while len(queue) > 0:
        row, col = queue.pop(0)       
        for dr, dc in zip(DR, DL):
            nr = row + dr
            nc = col + dc
            if is_go(nr, nc) and visited.get((nr, nc)) is None:
                if nr == len(CAVE) - 1:
                    is_attach_floor = True
                queue.append((nr, nc))
                visited[(nr, nc)] = True
                if cluster.get(nc) is None:
                    cluster[nc] = list()
                cluster[nc].append(nr)
    return is_attach_floor, cluster, visited


def dropped_cluster(removed_mineral, col_size):
    visited = dict()
    cluster = dict()
    print("removed_mineral", removed_mineral)
    for dr, dc in zip(DL, DR):
        nr = removed_mineral[0] + dr
        nc = removed_mineral[1] + dc
        if is_go(nr, nc) and visited.get((nr, nc)) is None:
            is_attach_floor, cluster, visited = bfs((nr, nc), visited)
            if not is_attach_floor:
                break
    return cluster


def meet_mineral_or_floor(row, col):
    #print("row", "col", row, col)
    if row+1 >= len(CAVE):
        #print("b1")
        return True
    if CAVE[row+1][col] == 'x':
        #print("b2")
        return True
    return False


def drop(cluster):
    print("CLUSTER", cluster)
    min_dropped = 1000000001
    for column in list(cluster.keys()):
        mineral_rows = cluster[column]
        dropped_row = max(mineral_rows)
        dist = 0
        while not meet_mineral_or_floor(dropped_row, column):
            dropped_row += 1
            dist += 1
        if min_dropped > dist:
            min_dropped = dist
    #print(min_dropped, column)
    for column in list(cluster.keys()):
        rows = sorted(cluster[column], reverse=True)
        #print(rows)
        for row in rows:
            #print("row", row)
            CAVE[row][column] = '.'
            CAVE[row+min_dropped][column] = 'x'
            

def start_fight(cave_size, stick_heights):
    global CAVE
    row_size, col_size = cave_size
    for index, mineral in enumerate(stick_heights):
        if index % 2 == 0:
            direction = (0, 1)
        else:
            direction = (col_size-1, -1)
        removed_mineral = remove_mineral(mineral, direction, row_size)
        print("==removed==")
        print(removed_mineral)
        print_cave()
        if removed_mineral[0] is not None and removed_mineral[1] is not None:
            print("===start===")
            cluster = dropped_cluster(removed_mineral, col_size)
            if len(cluster) > 0:
                drop(cluster)
        print_cave()


def print_cave():
    global CAVE
    for i in range(len(CAVE)):
        for j in range(len(CAVE[i])):
            print(CAVE[i][j], end='')
        print()
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
