# 시작 4시 35분
# 문제해석시간 4시 38분
# 휴식 5시 14분
# 코드생각시간 5시 20분
# 코드만드는시간 06시 03분
# 디버깅시간 06시 18분
# 오류잡는시간 7시 17분
import sys
import re
inputs = sys.stdin.readline
DL = (1, -1, 0, 0, 0, 0)
DR = (0, 0, -1, 1, 0, 0)
DC = (0, 0, 0, 0, -1, 1)


def print_map(building):
    for level in range(len(building)):
        for row in range(len(building[0])):
            print(*building[level][row])
        print()


def is_go(building, next_loc):
    level, r, c = next_loc
    if level < 0 or r < 0 or c < 0:
        return False
    if level >= len(building) or \
       r >= len(building[0]) or \
       c >= len(building[0][0]):
        return False
    if building[level][r][c] == '#':
        return False
    if building[level][r][c] == 'T':
        return False
    return True


def bfs(building, start_end_loc):
    l, r, c = start_end_loc['start']
    queue = [(start_end_loc['start'], 0)]  # 시작위치, 최단거리
    dist = -1
    building[l][r][c] = 1
    while len(queue) > 0:
        loc, dist = queue.pop(0)
        l, r, c = loc
        # 도착했는지 검사
        if loc == start_end_loc['end']:
            return dist        
        # 다음위치로 이동
        for dl, dr, dc in zip(DL, DR, DC):
            next_loc = l + dl, r + dr, c + dc
            if is_go(building, next_loc):
                queue.append((next_loc, dist+1))
                building[l+dl][r+dr][c+dc] = 'T'
    return -1


def find_start_end_loc(row, letter):
    result = re.search(letter, row)
    if result is not None:
        return result.start()
    return -1


def start_end(row, letter):
    result = find_start_end_loc(row, letter)
    if result != -1:
        return result
    return None


def print_result(result):
    if result > 0:
        print("Escaped in {0} minute(s).".format(result))
    else:
        print("Trapped!")


def main():
    while True:
        building = []
        start_end_loc = dict()
        levels, rows, columns = map(int, inputs().strip().split(" "))
        if levels == 0 and rows == 0 and columns == 0:
            break
        for level in range(levels):
            floor = []
            for r in range(rows):
                row = inputs().strip()
                floor.append(list(row))
                start = start_end(row, 'S')
                end = start_end(row, 'E')
                if start is not None:
                    start_end_loc['start'] = (level, r, start)
                if end is not None:
                    start_end_loc['end'] = (level, r, end)

            building.append(floor)
            inputs()
            #print(i, building)
        result = bfs(building, start_end_loc)
        print_result(result)


if __name__ == "__main__":
    main()
