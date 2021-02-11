# https://www.acmicpc.net/problem/19236


#01:06 시작
#01:24 코딩 시작
#01:42 입력 구현
#02:36 물고기 이동 구현
#03:56 디버깅 포기, 코드 변경
# 3시간 30분 소요 #

"""
문제

1. 물고기 이동
  - 1부터 16까지 순서대로
  - 공간 경계 넘거나 상어 만나면 45도 반시계 회전
  - 8방향 돌아도 없으면 그대로
  - 이동가능하면 위치 교환 방식으로 진행

2. 상어 이동
  - 한번에 여러칸 가능
  - 물고기 있는 곳으로만 이동가능
  - 물고기 먹으면 먹은 양 증가 + 물고기의 방향을 얻음

3. 출력
  - 상어가 먹을 수 있는 최대값

풀이

1. 문제에서 요구하는 대로 물고기 이동, 상어 이동 함수를 구함.
2. 상어가 이동한 뒤에 가능한 위치가 여러개 있을 수 있는데 백트래킹을 이용.
   - 모든 위치를 가보면서 현재 먹은 값이 최대값보다 크면 갱신

시행착오

1. 전체 배열을 탐색하여 1부터 16까지 물고기 찾는 방법이 아닌, 물고기 배열에 위치값을 통해 효율적으로 찾으려고 했음.
  - 디버깅하다가 안되서 도중에 바꿈

2. 물고기 이동 함수(fish_move()) 함수의 인자로 array배열을 안넘겨줬음. 엉뚱한 array로 물고기를 이동시켰음

3. 상어 이동 함수(shark_move()) 함수에서 shark_x, shark_y 값이 바뀌도록 실수함.

"""


import copy

shark_x, shark_y = 0,0
array = [[0] * 4 for _ in range(4)]
#print(array)
fish = [0 for _ in range(16)]

for i in range(4):
    temp = list(map(int,input().split()))
    y = 0
    start = 0
    for j in range(2,10,2):
        #print(j)
        t =temp[start:j]

        fish_num= t[0]
        fish_dir = t[1]

        array[i][y] = [fish_num, fish_dir-1]

        start = j
        y+=1

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

INF = int(1e9)

def find_fish(n,array): # 물고기 위치, 방향 반환 함수

    for x in range(4):
        for y in range(4):

            if array[x][y] == -1 or array[x][y] == 0:
                continue

            if array[x][y][0] == n:
                direction = array[x][y][1] # 방향
                return x,y, direction
    return None

def fish_move(array): # 물고기 이동함수

    for i in range(16):
        fish=find_fish(i+1,array) # array를 인자로 안줬음
        if fish ==None:
            continue
        x,y,dir =fish[0],fish[1],fish[2]
        for j in range(8):
            ndir = (dir+j)%8
            nx = x + dx[ndir]
            ny = y + dy[ndir]
            if nx<0 or nx >= 4 or ny<0 or ny>=4: # 이부분 0>nx로 잘못 설정 ㅠ
                continue
            if array[nx][ny] == -1:
                continue

            if array[x][y] != 0:
                array[x][y][1] = ndir # 새로운 방향 지정 안해줬음ㅠ

            array[nx][ny], array[x][y] = array[x][y], array[nx][ny] # 교환
            break

eat_fish = 0

def shark_move(shark_x,shark_y,shark_dir,array): # 상어 이동 함수
    possible = []
    x,y = shark_x, shark_y
    for i in range(4):
        nx = x + dx[shark_dir]  # 처음에 x 를 shark_x로 둬서 shark 위치가 바뀌도록 실수함.
        ny = y + dy[shark_dir]

        if nx>=4 or nx<0 or ny>=4 or ny<0:
            break
        if array[nx][ny] != 0:
            possible.append((nx,ny))
        x, y = nx, ny

    if len(possible) == 0:
        return None
    else:
        return possible

def solve(shark_x,shark_y,eat,array):

    fish_num, dir = array[shark_x][shark_y]
    array[shark_x][shark_y] = -1
    eat += fish_num # 먹은 양 증가

    shark_dir = dir # 상어 방향

    # 물고기 이동
    fish_move(array)

    # 상어 이동
    possible=shark_move(shark_x,shark_y,shark_dir,array)

    if possible == None:
        global eat_fish
        if eat_fish <eat:
            eat_fish = eat
        return

    else:
        for px,py in possible:
            array[shark_x][shark_y] = 0

            new_array = copy.deepcopy(array)
            solve(px,py,eat,new_array)

solve(0,0,0,array)
print(eat_fish)





