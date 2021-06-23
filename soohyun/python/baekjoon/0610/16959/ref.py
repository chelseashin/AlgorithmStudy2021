from collections import deque
import sys
input = sys.stdin.readline
def dict2arr(route, N):
    arr = [0]*(N**2+1)
    for key, value in route.items():
        arr[key] = [value[0], value[1]]
    return arr
    

def bfs(route, N):
    route = dict2arr(route, N)
    maxn = 5*N**2
    # states = [1,1,1] # rook, bishop, knight
    steps = [0,0,0] # rook, bishop, knight
    for i in range(2,N**2+1):
        start = route[i-1]
        end = route[i]

        minn = [maxn,maxn,maxn]
        for ii in range(3): # 출발점
            # 룩
            r_step = rook(start, end, N)
            if ii != 0:
                r_step += 1

            if minn[0] > steps[ii]+r_step:
                minn[0] = steps[ii]+r_step
            
            # 비숍
            b_step = bishop(ii, start, end, N)

            if minn[1] > steps[ii]+b_step:
                minn[1] = steps[ii]+b_step
                
            # 나이트
            k_step = knight(ii, start, end, N)

            if minn[2] > steps[ii]+k_step:
                minn[2] = steps[ii]+k_step
        steps = minn
    
    return min(steps)

def rook(start, end, N): # rook으로 도착(기본)
    dr, dc = start[0]-end[0], start[1]-end[1]
    if not dr or not dc:
        return 1
    else:
        return 2


def bishop(ii, start, end, N): # bishop으로 도착
    dr, dc = abs(start[0]-end[0]), abs(start[1]-end[1])
    if ii == 1:
        if dr == dc:
            return 1
        elif dr%2 == dc%2:
            return 2
        else:
            return 4
    if ii == 0:
        if dr == dc:
            return 2
        else:
            return 3
    if ii == 2:
        if dr == dc:
            return 2
        elif dr%2 == dc%2:
            return 3
        else:
            d = [(2,-1), (2,1), (1,2), (-1,2), (-2,-1), (-2,1), (1,-2), (-1,-2)]
            for dr, dc in d:
                if 0<= start[0]+dr <N and 0<= start[1]+dc <N and abs(start[0]+dr-end[0])==abs(start[1]+dc-end[1]):                
                    return 3
            return 4


def knight(ii, start, end, N): # knight로 도착
    d = [(2,-1), (2,1), (1,2), (-1,2), (-2,-1), (-2,1), (1,-2), (-1,-2)]
    if ii == 2:
        queue = deque([start+[0]])
        visited = [[0]*N for _ in range(N)]
        visited[end[0]][end[1]] = 2
        step = 0
        while queue and step < 4:
            r,c, step = queue.popleft()
            if visited[r][c]:
                if visited[r][c] == 2:
                    return step
                continue
            visited[r][c] = 1

            for dr, dc in d:
                if 0<= r+dr <N and 0<= c+dc <N and visited[r+dr][c+dc] != 1:
                    queue.append([r+dr,c+dc,step+1])
        return 4
    if ii == 0:
        step = 4
        for dr, dc in d:
            if 0<= end[0]-dr <N and 0<= end[1]-dc <N:
                if (start[0], start[1]) == (end[0]-dr, end[1]-dc):
                    return 2
                if step > 3 and (not start[0]-end[0]+dr or not start[1]-end[1]+dc):                
                    step = 3
        return step
    if ii == 1:
        step = 4
        for dr, dc in d:
            if 0<= end[0]-dr <N and 0<= end[1]-dc <N:
                if (start[0], start[1]) == (end[0]-dr, end[1]-dc):
                    return 2
                if step > 3 and abs(start[0]-end[0]+dr)==abs(start[1]-end[1]+dc):                
                    step = 3
        return step

if __name__ == "__main__":
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    
    route = [0]*(N**2+1)
    for i in range(N):
        for j in range(N):
            route[board[i][j]] = [i,j]
    print(route)

    print(bfs(route, N))

