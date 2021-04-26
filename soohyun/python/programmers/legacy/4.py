#시작 09시 10분
#끝 12시 13분
def change_direction(dx, dy, is_left):
    cx, cy = 0, 0
    if dx == 1 and dy == 0:
        if is_left:
            cx, cy = 0, 1
        else:
            cx, cy = 0, -1
    elif dx == 0 and dy == 1:
        if is_left:
            cx, cy = -1, 0
        else:
            cx, cy = 1, 0
    elif dx == -1 and dy == 0:
        if is_left:
            cx, cy = 0, -1
        else:
            cx, cy = 0, 1
    elif dx == 0 and dy == -1:
        if is_left:
            cx, cy = 1, 0
        else:
            cx, cy = -1, 0
    return cx, cy


def padding(maze):
    nmaze = []
    default_len = len(maze)
    nmaze.append([1] * (default_len + 2))
    for index, line in enumerate(maze):
        nmaze.append(list())
        nmaze[index + 1].append(1)
        nmaze[index + 1].extend(line)
        nmaze[index + 1].append(1)
    nmaze.append([1] * (default_len + 2))
    return nmaze

def solution(maze):
    x, y = 1, 1
    dx, dy = 1, 0
    time = 0
    nmaze = padding(maze)
    count = 20
    while True:
        if x == len(nmaze) - 2 and y == len(nmaze) - 2:
            time += 1
            break
        lx, ly = change_direction(dx, dy, True)
        if nmaze[x + lx][y + ly] == 0:
            dx, dy = change_direction(dx, dy, True)
        if nmaze[x + dx][y + dy] == 1:
            dx, dy = change_direction(dx, dy, False)
            continue
        x += dx 
        y += dy
        time += 1
    return time - 1

print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))