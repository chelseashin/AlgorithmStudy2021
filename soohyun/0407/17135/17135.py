import sys
import math
import heapq
import copy
from collections import deque
input = sys.stdin.readline
MAP = deque()
MAPCOPY = deque()


def start_game(row, col, attack_dist):
    global MAP
    global MAPCOPY
    max_removed_enemy = 0
    archers = [0, 0, 0]
    
    while True:
        MAPCOPY = copy.deepcopy(MAP)
        archers = next_permuation(archers, col)
        #print(archers)
        removed_enemy = 0
        turn = 0
        if archers[0] == -1:
            return max_removed_enemy
        while turn < row:
            removed_enemy += attack(archers, turn, attack_dist)
            turn += 1
        if max_removed_enemy < removed_enemy:
            max_removed_enemy = removed_enemy
    return max_removed_enemy


def attack(archers, row, attack_dist):
    global MAPCOPY

    removed_enemy = 0
    removed_enemies = set()
    
    for archer in archers:
        archer = archer - 1
        archer_loc = (row, archer)
        enemy_row, enemy_col = find_attack_enemy(archer_loc, attack_dist)
        if enemy_row != math.inf and enemy_col != math.inf:
            removed_enemies.add((enemy_row, enemy_col))
            MAPCOPY[enemy_row][enemy_col] = 0
            removed_enemy += 1
    removed_enemy = len(removed_enemies)
    while len(removed_enemies) > 0:
        enemy_row, enemy_col = removed_enemies.pop()
        MAPCOPY[enemy_row][enemy_col] = 0
        print_MAP()
    return removed_enemy


def print_MAP():
    global MAPCOPY
    for row in MAPCOPY:
        print(*row)


def find_attack_enemy(archer, attack_dist):
    enemies = list()
    candidate_enemy = (archer[0]+1, archer[1])
    if is_enemy(candidate_enemy, archer):
        heapq.heappush(enemies, candidate_enemy)
    for i in range(1, attack_dist):
        next_enemy = (candidate_enemy[0] + i, candidate_enemy[1] + i)
        if is_enemy(next_enemy, archer):
            heapq.heappush(enemies, next_enemy)
        next_enemy = (candidate_enemy[0] + i, candidate_enemy[1] - i)
        if is_enemy(next_enemy, archer):
            heapq.heappush(enemies, next_enemy)
    if len(enemies) > 0:
        return heapq.heappop(enemies)
    return math.inf, math.inf


def is_enemy(candidate_ememy, archer):
    global MAPCOPY
    row, col = candidate_ememy
    if row >= 0 and col >= 0:
        if row < len(MAPCOPY) and col < len(MAPCOPY[0]):
            if row != archer[0]:  # 적은 항상 archer 아래에 있으므로
                if MAPCOPY[row][col] == 1:
                    return True
    return False


def next_permuation(archers, N):
    x, y, z = archers[0], archers[1], archers[2]
    if x == 0:
        return [1, 2, 3]
    if z < N:
        return [x, y, z + 1]
    else:
        if y < N - 1:
            y = y + 1
            z = y + 1
            return [x, y, z]
        else:
            if x < N - 2:
                x = x + 1
                y = x + 1
                z = y + 1
                return [x, y, z]
            else:
                return [-1, -1, -1]


def main():
    global MAP
    row, col, attack_distance = map(int, input().strip().split(" "))
    
    for r in range(row):
        column = list(map(int, input().strip().split(" ")))
        MAP.appendleft(column)
    MAP.appendleft([0]*col)
    return start_game(row, col, attack_distance)


if __name__ == "__main__":
    print(main())