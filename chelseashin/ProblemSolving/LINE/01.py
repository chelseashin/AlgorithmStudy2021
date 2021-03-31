# 19:32 start
# 19:55 finish

def solution(boxes):
    info = dict()
    for box in boxes:
        for x in box:
            if x not in info.keys():
                info[x] = 1
            else:
                info[x] += 1
    # print(info)
    temp = 0
    for value in info.values():
        if value % 2:
            temp += 1
    return temp // 2

print(solution([[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]))
print(solution([[1, 2], [3, 4], [5, 6]]))
print(solution([[1, 2], [2, 3], [3, 1]]))
print(solution([[1, 2], [5, 5], [5, 6]]))
