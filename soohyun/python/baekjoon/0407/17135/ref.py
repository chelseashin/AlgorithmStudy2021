from itertools import combinations
from copy import deepcopy
import sys

MAP = []
DIED = []


def attack_len(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)


def can_shoot(map, row, col, attack_dist, mapcol):
    global DIED
    diclist = []
    for i in range(row-1, 0, -1):
        for j in range(mapcol):
            if map[i][j] == 1:
                length = attack_len(row, col, i, j)
                if length <= attack_dist:
                    diclist.append((length, j, i))
    if diclist:
        diclist.sort()
        DIED.append((diclist[0][2], diclist[0][1]))
        return True
    return False


def start_game(row, col, attack_dist):
    global MAP
    global DIED
    archers = [i for i in range(0, col)]
    archer_case = list(combinations(archers, 3))
    shoot_count = 0
    result = 0
    max_result = 0
    for item in archer_case:
        result = 0
        maps = deepcopy(MAP)
        for archer_row in range(row+1, 1, -1):
            for archer_col in item:
                if shoot_count < 3:
                    if can_shoot(maps, archer_row, archer_col, attack_dist, col):
                        shoot_count += 1

            shoot_count = 0
            for enemy in DIED:
                if maps[enemy[0]][enemy[1]] == 1:
                    result += 1
                    maps[enemy[0]][enemy[1]] = 0
            DIED = []
            if max_result < result:
                max_result = result
    return max_result


def print_map(maps):
    print("==start==")
    for i in range(len(maps)):
        print(*maps[i])
    print("==end")

def main():
    global MAP
    row, col, attack_distance = map(int, sys.stdin.readline().strip().split(" "))
    MAP = [[0]*(col+1) for _ in range(row+1)]
    for i in range(1, row+1):
        MAP[i] = list(map(int, sys.stdin.readline().strip().split()))
    return start_game(row, col, attack_distance)


if __name__ == "__main__":
    print(main())       
