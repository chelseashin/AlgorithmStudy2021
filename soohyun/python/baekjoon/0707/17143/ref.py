import sys
input = sys.stdin.readline

def solve(sea):
    newSea = [[0]*(c+1) for i in range(r+1)] 
    for y in range(1,r+1):
        for x in range(1, c+1):
            if sea[y][x] != 0:
                s,d,z = sea[y][x]
                ny, nx = y+s*dir[d][0], x+s*dir[d][1]

                while ny < 1 or ny > r:
                    if ny < 1:
                        d = 2
                        ny = 2 - ny
                    if ny > r:
                        d = 1
                        ny = r+r-ny

                while nx < 1 or nx > c:
                    if nx < 1:
                        d = 3
                        nx = 2 - nx
                    if nx > c:
                        d = 4
                        nx = c+c-nx  

                if newSea[ny][nx] != 0:
                    if z > newSea[ny][nx][2]:
                        newSea[ny][nx] = [s,d,z]
                else:
                    newSea[ny][nx] = [s,d,z]    
    return newSea


r,c,m = map(int, input().split())
sea = [[0]*(c+1) for i in range(r+1)]
dir = [[0,0], [-1,0],[1,0],[0,1],[0,-1]]
 
for k in range(m):
    i,j,s,d,z = map(int, input().split())    
    s %= ((r if d <= 2 else c)-1)*2    
    sea[i][j] = [s,d,z]
 
cur = 0
result = 0
while cur < c:
    cur += 1
    for k in range(1,r+1):
        if sea[k][cur] != 0:
            result += sea[k][cur][2]
            sea[k][cur] = 0
            break
    sea = solve(sea) 
    
print(result)