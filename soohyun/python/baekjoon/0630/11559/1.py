# 걸린시간 1시간
import sys
from collections import deque
input = sys.stdin.readline
WIDTH = 6
HEIGHT = 12


def input_values():
    return [list(input().rstrip()) for _ in range(HEIGHT)]


def bomb_puyo(visited, pmaps, start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    start_puyo = pmaps[start[0]][start[1]]
    bomb_list = []
    while queue:
        row, col = queue.popleft()
        bomb_list.append((row, col))
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < HEIGHT and 0 <= nc < WIDTH:
                if not visited[nr][nc]:
                    if start_puyo == pmaps[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
    #print(bomb_list)
    if len(bomb_list) < 4:
        return []
    return bomb_list


def fall_puyo(pmaps, bomb_list):
    col_list = set()
    for row, col in bomb_list:
        pmaps[row][col] = '.'
        col_list.add(col)

    for col in list(col_list):
        for row in range(HEIGHT-1, -1, -1):
            if pmaps[row][col] != '.':
                value = pmaps[row][col]
                pmaps[row][col] = '.'
                nrow = row + 1
                while True:
                    #print(nrow, col)
                    if nrow >= HEIGHT:
                        pmaps[nrow-1][col] = value
                        break
                    if pmaps[nrow][col] != '.':
                        pmaps[nrow-1][col] = value
                        break
                    nrow = nrow + 1


def print_puyo(pmaps):
    print("")
    for row in pmaps:
        print(''.join(row))
    print("")


def start_game(pmaps):
    result = 0
    #print_puyo(pmaps)
    while True:
        visited = [[False]*WIDTH for _ in range(HEIGHT)]
        bomb_list = []
        for i in range(HEIGHT-1, -1, -1):
            for j in range(WIDTH):
                if not visited[i][j] and pmaps[i][j] !='.':
                    bomb_list.extend(bomb_puyo(visited, pmaps, (i, j)))

        if len(bomb_list) == 0:
            break
        else:
            fall_puyo(pmaps, bomb_list)
            result += 1
        #print_puyo(pmaps)
    return result


def main():
    pmaps = input_values()  
    print(start_game(pmaps))


if __name__ == "__main__":
    main()