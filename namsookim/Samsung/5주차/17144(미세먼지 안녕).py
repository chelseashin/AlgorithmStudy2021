# https://www.acmicpc.net/problem/17144

# 1시간 27분 소요

R,C,T = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(R)]
machine = []

for r in range(R):
    if array[r][0] == -1:
        machine.append((r,0))
        machine.append((r+1,0))
        break

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def spread(array):
    global machine
    new_array = [[0]*C for _ in range(R)]

    for mx,my in machine:
        new_array[mx][my] = -1

    for x in range(R):
        for y in range(C):
            if array[x][y]>0: # 확산가능
                dir_cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<R and 0<=ny<C:
                        if array[nx][ny] != -1:
                            dir_cnt +=1
                            new_array[nx][ny] += array[x][y]//5
                new_array[x][y] += (array[x][y] - (array[x][y]//5 * dir_cnt))

    return new_array

def air_work(new_array):
    global machine
    # 위쪽 공기청정기는 반시계 방향 순환

    up_x, up_y = machine[0][0], machine[0][1]
    down_x,down_y = machine[1][0], machine[1][1]

    # 위쪽 공기청정기(반시계 회전)

    # 왼쪽
    for i in range(up_x-1,0,-1):
        new_array[i][0] = new_array[i-1][0]

    # 위쪽
    for i in range(C-1):
        new_array[0][i]= new_array[0][i+1]

    # 오른쪽
    for i in range(up_x):
        new_array[i][C-1] = new_array[i+1][C-1]

    # 중앙
    for i in range(C-1,1,-1):
        new_array[up_x][i] = new_array[up_x][i-1]
    new_array[up_x][1] = 0

    # 아래쪽 공기청정기(시계방향)
    # 왼쪽
    for i in range(down_x+1,R-1):
        new_array[i][0] = new_array[i+1][0]

    # 아래쪽
    for i in range(C-1):
        new_array[R-1][i]= new_array[R-1][i+1]

   # 오른쪽
    for i in range(R-1, down_x, -1):
        new_array[i][C-1] = new_array[i - 1][C-1]

   # 중앙
    for i in range(C-1, 1, -1):
        new_array[down_x][i] = new_array[down_x][i - 1]
    new_array[down_x][1] = 0

    return new_array

def check(array):
    answer = 0
    for x in array:
        answer += sum(x)
    return answer + 2 # -1 2개

def solve(array):

    for _ in range(T):
        new_array=spread(array) # 미세먼지 확산
        array=air_work(new_array) # 공기청정기 작동

    ans=check(array) # 방에 남은 미세먼지 전체 양 출력
    return ans

print(solve(array))