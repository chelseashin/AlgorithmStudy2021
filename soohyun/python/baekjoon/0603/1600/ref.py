import sys, collections

# 입력부
k = int(sys.stdin.readline())
m , n = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

hx = [-1,-2,-1,-2,1,2,1,2]
hy = [-2,-1,2,1,-2,-1,2,1]

check = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

def go(a,b):
    q = collections.deque()
    q.append((a,b,0,0))
    check[a][b][0] = True
    while q:
        x,y,skill, cnt = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return cnt
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny][skill] == False:
                    if table[nx][ny] == 0:
                        check[nx][ny][skill] = True
                        q.append((nx, ny, skill, cnt + 1))

        if skill < k:
            for i in range(8):
                nx, ny = x + hx[i], y + hy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if check[nx][ny][skill + 1] == False:
                        if table[nx][ny] == 0:
                            check[nx][ny][skill + 1] = True
                            q.append((nx,ny,skill+1,cnt + 1))
    return -1

print(go(0,0))