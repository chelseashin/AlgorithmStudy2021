# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRF8s6ezEDFAUo

# 3시간 20분 소요
"""
문제
1. 1~5까지 블록, 6~10 까지 웜홀, -1 블랙홀
2. 블록을 부딪힐 때 부딪힌 방향에 따라 방향이 변함
3. 웜홀에 도착하면 같은 쌍의 웜홀에서 나옴, 방향 그대로
4. 블랙홀 만나거나 시작방향에 도착하면 종료

풀이
1. 요구사항대로 구현

시행착오
1. 벽 만나기 전에 시작위치 도달할 수 있음
2. 같은 번호중 다른 웜홀 좌표 구하는 조건 잘못 설정


"""

import sys
sys.stdin = open('5650(핀볼게임).txt')


dx = [-1, 0, 1, 0]  # 위, 오른, 아래, 왼
dy = [0, 1, 0, -1]

def calc_direction(block_num,dir): # 방향 반환 함수

    # 1번 블록은 오른쪽->위쪽 or 아래->오른쪽
    if block_num == 1:
        if dir ==3 or dir ==2 : # 오른쪽 또는 아래쪽일 경우
            if dir == 3: #오른쪽에서 오면
                return 0 # 위쪽

            elif dir == 2: #아래쪽으로 오면
                return 1 #오른쪽

        else: # 나머지는 반대로
            return (dir+2)%4

    # 2번 블록은 왼쪽->아래쪽, 위쪽-> 오른쪽
    if block_num == 2:
        if dir == 3 or dir == 0 : # 오른쪽, 아래쪽
            if dir == 3: # 오른쪽이면
                return 2 # 아래쪽

            elif dir == 0:
                return 1 #오른쪽

        else: # 나머지는 반대로
            return (dir+2)%4

    # 3번 블록 / 위쪽방향->왼쪽, 오른쪽방향->아래방향
    if block_num == 3:
        if dir == 0 or dir == 1:
            if dir == 0:
                return 3  # 왼쪽

            elif dir == 1:
                return 2  # 아래쪽

        else:  # 나머지는 반대로
            return (dir + 2) % 4

    # 4번 블록 / 오른쪽->위쪽, 아래쪽->왼쪽
    if block_num == 4:
        if dir == 1 or dir == 2:  # 오른쪽, 아래쪽
            if dir == 1: #오른쪽
                return 0  # 위쪽

            elif dir == 2: # 아래족
                return 3  # 왼쪽

        else:  # 나머지는 반대로
            return (dir + 2) % 4

    # 5번 블록 / 모두 반대
    if block_num == 5:
        return (dir+2)%4


def move(x,y,dir,start_x,start_y):
    # 블랙홀 -1, 빈공간 0 , 블록 1~5, 웜홀 6~10

    # 만약에 바로 벽을 만난거면 x,y 좌표에 방향만 반대처리
    nx = x
    ny = y

    while True:

        # 출발위치랑 같으면 종료
        if nx == start_x and ny == start_y:
            return nx, ny, -1, dir # -1 반환 시 종료조건

        if nx<0 or ny<0 or nx>=N or ny>=N: # 벽을 만났으면

            # 들어오기 전 좌표 반환

            bx = x-dx[dir] # 처음 들어올 때 한칸 이동시켜주고 함수로 들어옴. 1칸 뒤로 이동시켜줌
            by = y-dy[dir]

            return bx,by,0,(dir+2)%4 # 좌표,종류,방향 반환 (벽을 만났을 때 0 반환)

        else: # 범위 안에 들면

            block_num = array[nx][ny]

            # 블랙홀을 만났으면 종료(-1) 리턴
            if block_num == -1:

                return nx,ny,-1,dir

            if block_num == 0: # 빈 블록이면 그대로 진행
                nx +=dx[dir]
                ny +=dy[dir]

                continue

            if 1<=block_num<=5: # 만약에 블록을 만난거면 좌표, 방향값 반환

                ndir=calc_direction(block_num,dir)
                nnx = nx + dx[ndir]
                nny = ny + dy[ndir]

                return nnx,nny,block_num,ndir


            # 웜홀은 만났으면 해당 번호와 같고, 좌표가 다른 웜홀로 좌표설정 후 방향은 그대로
            if 6<=block_num<=10:

                for worm in worm_holl[block_num]:

                    if nx == worm[0] and ny == worm[1]: # 웜홀 같은 놈은 넘어감.
                        continue

                    #if nx != worm[0] and ny != worm[1]: # 라고 조건 설정 실수

                    wx,wy = worm[0]+dx[dir], worm[1] + dy[dir]
                    return wx, wy, block_num,dir

def solve(array):
    answer = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            # 해당 좌표가 빈칸일 때 4가지 방향 탐색
            if array[i][j] == 0:
                start_x, start_y = i, j # 처음 위치 기록, 이동 중 같으면 종료시켜주기 위해서
                for dir in range(4):
                    cnt = 0
                    # 블록, 웜홀 , 블랙홀, 벽 만날때까지 이동
                    x = i+dx[dir]
                    y = j+dy[dir]

                    while True:

                        nx,ny, kind, ndir = move(x,y,dir,start_x,start_y) # 새로운 위치 좌표와, 만난것의 종류, 새로운 방향 반환

                        # 벽 또는 블록이면 +1 증가// 벽은 0 반환
                        if 0<=kind<=5:
                            cnt +=1

                        elif kind == -1: # 블랙홀 일 경우
                            answer = max(answer,cnt)
                            break

                        # 벽 맞고 처음위치 도달 할 수 있음
                        if nx == start_x and ny == start_y :

                            answer = max(answer,cnt)
                            break

                        x,y, dir = nx, ny, ndir

    return answer

T= int(input())
for tc in range(1,T+1):
    N = int(input())

    array = []
    worm_holl = [[] for _ in range(11)] # n번째 웜홀 위치좌표 기록
    for i in range(N):
        temp = list(map(int, input().split()))
        array.append(temp)
        for j in range(len(temp)):
            if 6 <= temp[j] <= 10:
                worm_holl[temp[j]].append((i, j))
    
    print('#{0} {1}'.format(tc,solve(array)))