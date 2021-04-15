from sys import stdin
from itertools import combinations
import copy

died = []

def cal_len(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def print_map(maps):
    print("==start==")
    for i in range(len(maps)):
        print(*maps[i])
    print("==end")


def can_shoot(chess, row, col, D):
    diclist = []
    global died
    # 거리, col, row 순
    for i in range(row - 1, 0, -1):
        for j in range(M):
            if chess[i][j] == 1:
                length = cal_len(row, col, i, j)
                if length <= D:
                    diclist.append((length, j, i))

    if diclist:
        diclist.sort()
        died.append((diclist[0][2], diclist[0][1]))
        print("inshoot", died)
        return True

    return False


N, M, D = map(int, stdin.readline().split())

chess = [[0] * (M + 1) for _ in range(N + 1)]
print_map(chess)

for i in range(1, N + 1):
    chess[i] = list(map(int, stdin.readline().split()))
print_map(chess)
# archer 위치 조합
archers = [i for i in range(0, M)]
archers_case = list(combinations(archers, 3))

shoot_cnt = 0
result = 0
max_result = 0
# N번
for item in archers_case: # 모든 궁수 조합에 대해
    result = 0
    copy_chess = copy.deepcopy(chess) # 궁수 조합에 따라 다시해야하므로 deep copy 한다.
    for archs_row in range(N + 1, 1, -1): # 가장가까운 행부터
        for archs_col in item: # 각 조합의 궁수 위치에 대해
            if shoot_cnt < 3:  # 3발 보다 적게 쐈다면
                if can_shoot(copy_chess, archs_row, archs_col, D):
                    shoot_cnt += 1

        shoot_cnt = 0
        print("died", died)
        for enemy in died: # 쏜 적에 대해
            if copy_chess[enemy[0]][enemy[1]] == 1: # 이미 쏘지 않은 적이면
                result += 1 # 죽인 횟수에 더한다
                copy_chess[enemy[0]][enemy[1]] = 0
        died.clear() # 혹시모르니 비운다
        print("deid clear", died)
    if max_result < result: # 각 궁수 조합의 result 에 대해 최댓값을 찾는다
        max_result = result

print(max_result)