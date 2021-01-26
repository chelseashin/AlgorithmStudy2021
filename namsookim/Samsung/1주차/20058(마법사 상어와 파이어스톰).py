# https://www.acmicpc.net/problem/20058

# 18:06 시작
# 19:23 회전 완료


# 2시간 27 분 소요

"""
1.90도 시계방향 회전에서 오래 시간이 걸렸다.(1시간 20분) 나머지 얼음의 양을 줄이거나 가장 큰 덩어리를 구하는
 방법은 bfs를 통해 해결해야겠다고 생각했지만 진행하면서 얼음을 줄이는 실수와 회전할 때 새로운 배열에 적용시키지
 않는 실수 때문에 오래 걸렸다.

2. 구현할 때 꼼꼼하게 하는 습관을 기르자
"""
import copy
from collections import deque
N, Q = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(2**N)]

L_list = list(map(int,input().split()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def trun_right(x,y,length,array,new_array): # 시계방향 90도 회전

    for i in range(length):
        for j in range(length):
            new_array[x+i][y+j] = array[x+(length-1-j)][y+i]

def bfs(array):

    max_ice = 0
    visited = [[False]*(2**N) for _ in range(2**N)]

    for x in range(2**N):
        for y in range(2**N):
            if array[x][y] != 0 and visited[x][y] != True:

                q = deque([(x,y)])
                p_size = 1
                while q:
                    x,y=q.popleft()
                    visited[x][y] = True

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<2**N and 0<=ny<2**N and visited[nx][ny] != True and array[nx][ny] != 0:

                            q.append((nx,ny))
                            p_size +=1
                            visited[nx][ny] = True

                max_ice = max(max_ice,p_size)

    return max_ice

def ice_check(array):
    # 진행하면서 그 값을 내려서 틀렸었음. 진행하면서 0 이 되면 결과가 달라지게됨
    new_array = copy.deepcopy(array)
    for x in range(2**N):
        for y in range(2**N):
            if array[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<2**N and 0<=ny<2**N:
                        if array[nx][ny] !=0:
                            cnt +=1
                if cnt <3:
                    new_array[x][y] -= 1
    return new_array

def sum_ice(array):
    ans = 0
    for i in range(2**N):
        for j in range(2**N):
            ans += array[i][j]
    return ans


def solve(array):

    for L in L_list:
        L = 2**L
        new_array = [[0] * (2 ** N) for _ in range(2 ** N)]

        for i in range(0,2**N,L):
            for j in range(0,2**N,L):
                trun_right(i,j,L,array,new_array) # 90도 회전

        array = ice_check(new_array)

    answer1 = sum_ice(array)
    answer2 = bfs(array)
    print(answer1)
    print(answer2)

solve(array)