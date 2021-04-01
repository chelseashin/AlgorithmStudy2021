# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl
# 8:36 시작
# 9:51 끝
# 1:15 소요

# 상:0, 하:1, 좌:2, 우:3

"""
풀이

- 미생물 정보 [개수, 방향]으로 맵으로 관리
- 빨간 위치에는 절대로 미생물 여러개 있을 수 없음.

1. 새로운 2차원 [] 배열을 만들었다. 모두 이동한 뒤 한꺼번에 처리해주기 위해
2. 개수가 2개 이상인 미생물들은 따로 처리 작업이 필요하다. 요구사항에 맞춰서 개수를 합한뒤 가장 큰 놈으로 방향 바꿔줌


시행착오
1. 첨에 -1을 기록한 배열을 만들었는데 여러마리 처리 때문에 바꿈
2. 딕셔너리를 쓰려다가 관리하기 귀찮아서 2차원 배열로 리스트를 넣음.
3. 일단 이동시킨 뒤 , 개수가 2인 애들은 조건에 맞게 처리해줬음.
4. 배열 리스트를 활용할 때 [[]] 와 [] 로 될 수 있다. 실수하지 않도록 주의!!

"""



def rev_dir(dir):
    reverse_dir = [1,0,3,2]

    return reverse_dir[dir]

def move(array):
    # 초기화

    new_array=[[[] for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if len(array[x][y]) == 1: # 무언가 있다

                temp=array[x][y]
                num, direction= temp[0][0],temp[0][1]
                nx = x + dx[direction]
                ny = y + dy[direction]
                if nx == 0 or ny == 0 or nx == N-1 or ny == N-1: # 방향 바뀜
                    # 미생물 수 반 감소
                    red_num = num // 2
                    if red_num == 0:
                        continue

                    new_array[nx][ny].append([red_num,rev_dir(direction)])

                else: # 안에 포함

                    new_array[nx][ny].append([num,direction])


    for i in range(N):
        for j in range(N):
            if len(new_array[i][j]) >=2:
                # print(new_array[i][j])
                sum_cell = 0
                n_dir = -1
                max_cell = 0
                for c_num, c_dir in new_array[i][j]:
                    # print(c_num,c_dir)
                    sum_cell += c_num
                    if c_num > max_cell:
                        max_cell = c_num
                        n_dir = c_dir
                # print(sum_cell,n_dir)
                # print(sum_cell,n_dir)
                new_array[i][j]=[[sum_cell, n_dir]]


    return new_array

def sum_result(array):
    result = 0
    for i in range(N):
        for j in range(N):
            if len(array[i][j]) != 0:
                temp = array[i][j]
                result+=temp[0][0]
    return result

import sys
sys.stdin = open("2382(미생물 격리).txt")

dx = [-1,1,0,0]
dy = [0,0,-1,1]
T = int(input())

for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    array = [[[] for _ in range(N)] for _ in range(N)]


    cell = []

    for _ in range(K):
        temp = list(map(int,input().split()))
        cell.append(temp)

    # 세로, 가로, 미생물 수, 이동방향
    # 미생물 배치
    for x,y,num,dir in cell:
        array[x][y].append([num,dir-1]) # 미생물 개수, 방향

    for _ in range(M):

        new_array = move(array)

        array = new_array

    print('#{0} {1}'.format(tc,sum_result(array)))


