# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo



import sys
import copy
from collections import deque

def print_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=' ')
        print()

N, M,K = map(int,input().split())
max_array = [[0]*(M+(2*K)) for _ in range(N+(2*K))]
#print(max_array)
array = [list(map(int,input().split())) for _ in range(N)]

# 배열 늘리기

# 언제 부터 넣냐?

for i in range(K,K+N):
    for j in range(K,K+M):
        max_array[i][j] = array[K-i][K-j]
#print_array(max_array)

def active_check(non_active_cell,active_cell):
    #print(non_active_cell)
    temp = []
    for i in range(len(non_active_cell)):
        x,y,index,time=non_active_cell[i]
        if time == 0:
            active_cell.append((x,y,index,index))
        else:
            time -= 1
            temp.append((x,y,index,time))
    return temp


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(array,active_cell,non_active_cell):

    # 죽은 부분은 냅둠
    new_array=copy.deepcopy(array)
    remain_active_cell = []
    while active_cell:
        x,y,index,time=active_cell.pop(0)


        if x == -1 and y == -1: # 이미 처리된적 있는 세포면
            continue

        # 활성화 한 뒤 세포는 죽음
        new_array[x][y] = -1 # 어차피 번식 못하니 죽었다고 처리

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 범위 나갈일 없음
            if array[nx][ny] !=0: # 누가 있거나 죽은거니
                continue
            else: # 0이면 비어있음
                if new_array[nx][ny] == 0: # 그냥 넣음
                    new_array[nx][ny] = index
                    non_active_cell.append((nx,ny,index,index))

                elif new_array[nx][ny]>0: # 누가 있으면 크기비교
                    print('겹치네?')
                    # 생명력 높은 세포만 그 자리 차지
                    if new_array[nx][ny] < index:
                        print(non_active_cell,' 여기에서')
                        print(nx,ny,array[nx][ny],index,' 이거 제거')
                        non_active_cell.remove((nx, ny, array[nx][ny],index)) # 현재 있는 놈 바뀌니 비활성 세포에서 제거

                        new_array[nx][ny] = index
                        non_active_cell.append((nx,ny,index,index))
    #print(q)

    return new_array,remain_active_cell

def solve(array):

    active_cell = []
    non_active_cell = []

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] !=0:
                non_active_cell.append((i,j,array[i][j],array[i][j]))


    for t in range(K+1): # K시간 후
        # 현재 array -> 시간 반영
        

        new_array,remain_cell = bfs(array, active_cell, non_active_cell) # 시간이 0인 놈 활성화 되고 번식
        array = new_array

        for x,y,index,time in remain_cell:
            active_cell.append((x,y,index,time)) # 활성화 되었다는 처리로 -1,-1 삽입

        # 활성화 된놈들 번식하고 비활성 상태 놈들 저장
        non_active_cell=active_check(non_active_cell,active_cell)



    # 남아있는 총 개수출력
    print(len(active_cell)+len(non_active_cell))


solve(max_array)