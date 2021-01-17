<<<<<<< HEAD
# https://www.acmicpc.net/problem/17822
# 10:16
# 11:57 끝

# 1시간 41분 소요

"""
문제
1. x의 배수의 원판을 d 방향으로 k번 회전한다
2. 인접한 곳에 같은 수가 있으면 모두 찾음
   2-1. 그런 수가 있다면 모두 지운다(-1)
   2-2. 없으면 원판에 적힌 수의 평균을 구한다.
      2-2-1. 평균보다 큰수에서는 값 = 값 -1
      2-2-2. 평균보다 작은수에서는 값 = 값 +1

풀이
1. 각 원판을 deque로 관리해주었다. deque의 rotate를 활용해서 회전시켜주기 위해.
2. 회전 후, 2차원 배열의 가로축, 세로축을 비교하면서 인접한 값을 처리해주었다.
   (주의사항, 열은 끝과 처음이 연결되어 있지만, 행의 끝과 처음은 연결되어있지 않음)

시행착오
1. 열의 끝과 처음을 연결시켜 주지 않았음.
2. 나누기 연산을 할 때 0으로 나누는 경우를 고려하지 않았음.
"""


import copy
from collections import deque
N, M , T = map(int,input().split())
array = [deque(list(map(int,input().split()))) for _ in range(N)]
info = [list(map(int,input().split())) for _ in range(T)]

def trun_direction(array,x,d,k):
    if d == 1: # 반시계 회전이면 rotate(-1)
        dir = -1
    else: # 시계 회전이면 rotate(1)
        dir = 1
    for i in range(x-1,N,x): # x가 2 이면 1,3 이 회전해야됨
        for _ in range(k): # k번 회전
            array[i].rotate(dir)
    return array

def find_near(array):
    tag = True # 인접하면서 수가 같은것이 있으면 , 찾으면 tag = False처리
    new_array = copy.deepcopy(array)
    for i in range(N): # 열처리
        for j in range(M):
            if array[i][j] == -1:
                continue

            if array[i][j] == array[i][(j+1)%M]: # 열은 첫번째와 끝에가 연결되어 있음
                new_array[i][j] = -1
                new_array[i][(j+1)%M] = -1
                tag = False

    for i in range(M):
        for j in range(N-1): # 행 돌리기
            if array[j][i] == -1:
                continue
            if array[j][i] == array[j+1][i]:
                new_array[j][i] = -1
                new_array[j+1][i] = -1
                tag= False

    # 못찾으면 tag = True
    if tag: # 인접하면서 수가 같은 것이 없으면
        total_value = 0 # 전체 값 더하기
        cnt = 0 # 개수 세기
        for i in range(N):
            for j in range(M):
                if array[i][j] == -1:
                    continue
                total_value += array[i][j]
                cnt += 1

        # 평균처리
        if total_value == 0:
            mean_value = 0
        else:
            mean_value = total_value / cnt

        for i in range(N):
            for j in range(M):
                if new_array[i][j] == -1:
                    continue
                if mean_value < new_array[i][j]: # 평균보다 크면 -1
                    new_array[i][j] -= 1
                elif mean_value > new_array[i][j]: # 평균보다 작으면 +1
                    new_array[i][j] += 1

    return new_array

def solve(array,info):

    for x,d,k in info:
        new_array=trun_direction(array,x,d,k) # x의 배수 원판을 찾아 회전
        array=find_near(new_array) # 근처에 인접한 수 처리

    answer = 0

    for i in range(N):
        for j in range(M):
            if array[i][j] == -1:
                continue
            answer += array[i][j]

    return answer

=======
# https://www.acmicpc.net/problem/17822
# 10:16
# 11:57 끝

# 1시간 41분 소요

"""
문제
1. x의 배수의 원판을 d 방향으로 k번 회전한다
2. 인접한 곳에 같은 수가 있으면 모두 찾음
   2-1. 그런 수가 있다면 모두 지운다(-1)
   2-2. 없으면 원판에 적힌 수의 평균을 구한다.
      2-2-1. 평균보다 큰수에서는 값 = 값 -1
      2-2-2. 평균보다 작은수에서는 값 = 값 +1

풀이
1. 각 원판을 deque로 관리해주었다. deque의 rotate를 활용해서 회전시켜주기 위해.
2. 회전 후, 2차원 배열의 가로축, 세로축을 비교하면서 인접한 값을 처리해주었다.
   (주의사항, 열은 끝과 처음이 연결되어 있지만, 행의 끝과 처음은 연결되어있지 않음)

시행착오
1. 열의 끝과 처음을 연결시켜 주지 않았음.
2. 나누기 연산을 할 때 0으로 나누는 경우를 고려하지 않았음.
"""


import copy
from collections import deque
N, M , T = map(int,input().split())
array = [deque(list(map(int,input().split()))) for _ in range(N)]
info = [list(map(int,input().split())) for _ in range(T)]

def trun_direction(array,x,d,k):
    if d == 1: # 반시계 회전이면 rotate(-1)
        dir = -1
    else: # 시계 회전이면 rotate(1)
        dir = 1
    for i in range(x-1,N,x): # x가 2 이면 1,3 이 회전해야됨
        for _ in range(k): # k번 회전
            array[i].rotate(dir)
    return array

def find_near(array):
    tag = True # 인접하면서 수가 같은것이 있으면 , 찾으면 tag = False처리
    new_array = copy.deepcopy(array)
    for i in range(N): # 열처리
        for j in range(M):
            if array[i][j] == -1:
                continue

            if array[i][j] == array[i][(j+1)%M]: # 열은 첫번째와 끝에가 연결되어 있음
                new_array[i][j] = -1
                new_array[i][(j+1)%M] = -1
                tag = False

    for i in range(M):
        for j in range(N-1): # 행 돌리기
            if array[j][i] == -1:
                continue
            if array[j][i] == array[j+1][i]:
                new_array[j][i] = -1
                new_array[j+1][i] = -1
                tag= False

    # 못찾으면 tag = True
    if tag: # 인접하면서 수가 같은 것이 없으면
        total_value = 0 # 전체 값 더하기
        cnt = 0 # 개수 세기
        for i in range(N):
            for j in range(M):
                if array[i][j] == -1:
                    continue
                total_value += array[i][j]
                cnt += 1

        # 평균처리
        if total_value == 0:
            mean_value = 0
        else:
            mean_value = total_value / cnt

        for i in range(N):
            for j in range(M):
                if new_array[i][j] == -1:
                    continue
                if mean_value < new_array[i][j]: # 평균보다 크면 -1
                    new_array[i][j] -= 1
                elif mean_value > new_array[i][j]: # 평균보다 작으면 +1
                    new_array[i][j] += 1

    return new_array

def solve(array,info):

    for x,d,k in info:
        new_array=trun_direction(array,x,d,k) # x의 배수 원판을 찾아 회전
        array=find_near(new_array) # 근처에 인접한 수 처리

    answer = 0

    for i in range(N):
        for j in range(M):
            if array[i][j] == -1:
                continue
            answer += array[i][j]

    return answer

>>>>>>> 74127a70fd1e2dbd7981056854a74139055968b6
print(solve(array,info))