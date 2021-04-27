def return_result(map):
    result = list()
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] > 0:
                result.append(map[i][j])
    return result

                
def is_go(row, col, maps, n):
    if row < 0 or col < 0:
        return False
    if row >= n or col >= n:
        return False
    if maps[row][col] > 0:
        return False
    return True

def make_snail(maps, n):
    result = list()
    rounds = 0
    count = 1
    row, col = 0, 0
    maps[row][col] = count
    while count < (n*(n+1))/2:
        while True:
            nr = row + 1
            if is_go(nr, col, maps, n):
                row = nr
                count += 1
                maps[row][col] = count
            else:
                break
        while True:
            nc = col + 1
            if is_go(row, nc, maps, n):
                col = nc
                count += 1
                maps[row][col] = count
                result.append(count)
            else:
                break
        while True:
            nr = row - 1
            nc = col - 1
            if is_go(nr, nc, maps, n):
                row = nr
                col = nc
                count += 1
                maps[row][col] = count
                result.append(count)
            else:
                break
    return return_result(maps)
                
    
def solution(n):
    answer = []
    maps = []
    for i in range(n):
        maps.append([0]*n)
    answer = make_snail(maps, n)
    return answer