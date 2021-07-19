import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr1 = [[[] for _ in range(n)] for _ in range(n)]
arr2 = [[False] * n for _ in range(n)]
arr2[0][0] = True
for _ in range(m):
    a, b, c, d = map(int, read().split())
    arr1[a-1][b-1].append((c-1, d-1))
def dist(a, b):
    yield a+1,b;yield a-1,b;yield a,b+1;yield a,b-1
q = [(0, 0)]
ans = 1
arr3 = [[0] * n for _ in range(n)]
arr3[0][0] = 2
while q:
    tmp = []
    for x, y in q:
        for i, j in arr1[x][y]:
            if not arr2[i][j]:
                arr2[i][j] = True
                ans += 1
            if arr3[i][j] == 1:
                tmp.append((i, j))
                arr3[i][j] = 2
        for xx, yy in dist(x, y):
            if -1 < xx < n and -1 < yy < n and arr3[xx][yy] == 0:
                if arr2[xx][yy]:
                    arr3[xx][yy] = 2
                    tmp.append((xx, yy))
                else:
                    arr3[xx][yy] = 1
    q = tmp
print(ans)