import sys
from collections import deque


# https://www.acmicpc.net/problem/1987
#
# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는
# 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

# Input Example
# 2 4
# CAAB
# ADCB


def dfs(x, y):
    global board, R, C

    max_depth = 0

    queue = set()
    queue.add((x, y, board[y][x]))

    while queue:
        current_x, current_y, current_visited = queue.pop()
        print(current_x, current_y, current_visited)
        max_depth = max(max_depth, len(current_visited))
        if max_depth == 26:
            return 26

        for movement in movement_array:
            next_x = current_x + movement[0]
            next_y = current_y + movement[1]
            if 0 <= next_x < C and 0 <= next_y < R and board[next_y][next_x] not in current_visited:
                queue.add((next_x, next_y, current_visited + board[next_y][next_x]))

    return max_depth


R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    row = list(sys.stdin.readline().strip())
    board.append(row)

movement_array = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]
start = (0, 0)
print(dfs(*start))
