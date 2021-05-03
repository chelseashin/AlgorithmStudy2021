# 17:28 start
# 17:42 pass

def solution(triangle):
    for r in range(len(triangle)-2, -1, -1):
        for c in range(r+1):
            triangle[r][c] += max(triangle[r+1][c], triangle[r+1][c+1])
    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))