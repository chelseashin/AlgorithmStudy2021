import sys
from itertools import combinations
import copy
from collections import  deque
# https://www.acmicpc.net/problem/17142

# 14:36 시작
# 16:01 디버깅
# 16:37 끝

# 2:01 소요

"""
문제
1. 바이러스는 활성, 비활성 상태가 있음
2. 처음 바이러스는 모두 비활성
3. 활성상태의 바이러스는 상하좌우로 인접한 빈칸으로 동시에 복제 . 1초 소요
4. M개를 활성 상태로 변경하려고 함.
5. 모든 빈 칸에 바이러스 퍼트리는 시간의 최소값은?
6. 모든 빈칸 처리 못하면 -1 

풀이
1. 내장함수 combinations 사용해서 경우의 수를 구함
2. 활성화 바이러스에서 bfs를 통해 최소 거리 찾음.
3. bfs를 통해 구한 최대 시간을 반환한 뒤, 현재까지의 최솟값과 비교
4. 모든 경우의 수를 따졌는데 빈칸에 바이러스 못 퍼뜨리면 -1 반환

시행착오
1. 비활성화된 바이러스를 통과하지 못한다고 구현했음.
"""

# 0은 빈칸, 1은 벽, 2는 바이러스
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int,input().split())
virus = []

array = [list(map(int,input().split())) for _ in range(N)]
for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j] == 2:
            virus.append((i,j,0)) # 0은 이동거리값(bfs에서 활용)

def active_function(active_virus,array):
    new_array = copy.deepcopy(array)
    for i in range(N):
        for j in range(N):
            if new_array[i][j] == 0:
                new_array[i][j] = -1 # 갈수 있는 곳 -1

            elif new_array[i][j] == 1: # 벽인 경우
                new_array[i][j] = '-' # -로 표시

            elif new_array[i][j] == 2:
                new_array[i][j] = '*' # 바이러스 처리

    for x,y,num in active_virus:
        new_array[x][y] = 0 # 활성화 바이러스 처리

    return new_array

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(virus,array):

    max_num = 0
    check = [[False]*N for _ in range(N)]

    q=deque(list(virus))

    while q:
        vx,vy,time=q.popleft()

        check[vx][vy] = True

        for i in range(4):
            nx = vx+dx[i]
            ny = vy+dy[i]
            if 0<=nx<N and 0<=ny<N: # 범위 안에 들고
                if check[nx][ny] != True and (array[nx][ny] == -1 or array[nx][ny] == '*'): # 바이러스도 건너뛸 수 있음. 이거 처리 못했음.

                    if array[nx][ny] == -1:
                        array[nx][ny] = time+1

                    check[nx][ny] = True
                    q.append((nx,ny,time+1))

    for i in range(N):
        for j in range(N):
            if array[i][j] == '*' or array[i][j] == '-':
                continue
            if max_num<array[i][j]:
                max_num = array[i][j]

    return max_num


def print_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=' ')
        print()

def possible(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == -1:
                return False
    return True

def solve():
    answer = INF
    virus_combi=list(combinations(virus,M)) # 전체 비활성 바이러스 중 M개를 선택하는 경우의 수
    tag = False # 가능한게 없는지 체크

    for active_virus in virus_combi:

        time_array=active_function(active_virus,array) # 선택한 M개를 활성화
        min_time = bfs(active_virus, time_array)

        if possible(time_array): # 빈 칸없이 채워졌으면
            tag = True
            # 최대값 반환한 뒤 비교
            answer = min(min_time,answer)

    if tag ==False: # 가능한게 없으면
        return -1

    else:
        return answer

print(solve())
