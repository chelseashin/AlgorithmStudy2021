# https://www.acmicpc.net/problem/17779

# 2시간 45분 소요
"""
게리맨더링2

문제
1. 문제의 조건에 따라 선거구를 정한 뒤 선거구 별 인구수를 파악하여 최대인원과 최소인원의 차이의 최솟값을 구하는 문제

풀이
1. 현재 위치를 기준으로 가능한 d1, d2의 쌍을 완전탐색을 통해 구한다.
2. 문제에서 주어진 조건에 따라 5번 선거구역의 경계값을 구한 뒤, 5번 선거구역을 감싸는 부분을 5번으로 채워준다.(다이아몬드 형태)
3. 나머지 1,2,3,4 번 선거구역을 그려준다.
4. bfs를 통해 입력받은 array, 선거구역 정보가 담긴 new_array를 비교해가며 인구수의 최대값과 최소값을 구한다.
5. 비교를 통해 최종 값을 출력한다.

시행착오
1. 5번 경계값의 빈 부분을 채워주는 데에 시간이 너무 많이 소요됨.

"""
from collections import deque

N= int(input())
array = [list(map(int,input().split())) for _ in range(N)]
#print(array)
INF = int(1e9)

def possible(x,y):
    pos = [] # d1,d2 담기
    global N
    for d1 in range(1,N):
        for d2 in range(1,N):
            if 0<=x  and (x+d1+d2)<=N-1 and 0<=(y-d1) and (y+d2)<=N-1: # 0,0 부터 시작해서 범위 1씩 줄임
                pos.append((d1,d2))

    return pos


def draw_5number(x,y,d1,d2):
    new_array = [[0]*N for _ in range(N)]
    new_array[x][y] = 5

    # 경계값 그리기
    for D1 in range(1,d1+1):
        new_array[x+D1][y-D1] = 5

    for D2 in range(1,d2+1):
        new_array[x+D2][y+D2] =5

    for D2 in range(d2+1):
        new_array[x +d1+D2][y -d1 +D2] = 5

    for D1 in range(d1+1):
        new_array[x + d2 + D1][y + d2 - D1] = 5

    # 경계값 사이 빈 칸을 5로 만들어주기
    for i in range(x+1,x+d1+d2): # x의 범위 지정
        tag = False  # 1번 만나면 True로, 2번 만나면 False
        for j in range(N):
            if new_array[i][j] == 5 and tag == False: # 처음 5를 만나면 다음부터 빈칸은 5로 만들어주기
                tag = True
                continue
            if new_array[i][j] == 5 and tag == True: # 2번째로 5를 만나면 경계값이니 break
                break

            if new_array[i][j] == 0 and tag == True:
                new_array[i][j] = 5

    return new_array

def draw_other(x,y,d1,d2,new_array):

    # 1,2,3,4 번 선거구 그려주기
    for r in range(N):
        for c in range(N):
            if new_array[r][c] == 0:
                if 0<=r<x+d1 and 0<=c<=y:
                    new_array[r][c] = 1
                elif 0<=r<=x+d2 and y-1<c<=N:
                    new_array[r][c] = 2
                elif x+d1<=r<=N-1 and 0<=c<y-d1+d2:
                    new_array[r][c] = 3
                elif x + d2 < r <= N - 1 and y-d1+d2<=c<=N-1:
                    new_array[r][c] = 4



def bfs(array,new_array):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    min_num = INF
    max_num = 0
    check = [[False]*N for _ in range(N)]
    # new_array 돌면서 check 표시
    for i in range(N):
        for j in range(N):
            if check[i][j] != True:
                number = new_array[i][j]
                temp = 0
                check[i][j] = True
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()
                    temp += array[x][y]
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<N and 0<=ny<N:
                            if number == new_array[nx][ny] and check[nx][ny] != True:
                                check[nx][ny] = True
                                q.append((nx,ny))

                # 다 끝나면
                min_num = min(min_num,temp)
                max_num = max(max_num,temp)
    return max_num - min_num

def solve():
    final_answer = INF
    for x in range(N):
        for y in range(N):
            # 가능한 기준점 찾기
            find=possible(x,y) # 현재 구역에 구역 d1,d2 찾기
            if len(find) != 0: # 가능한 곳이 있으면
                for d1,d2 in find:

                    # 기준점을 가지고 새로운 new_array에 경계선을 포함하여 5번 선거구 그리기
                    new_array=draw_5number(x,y,d1,d2)

                    # 5번 선거구가 아닌 지점들. 0으로 되어 있는 것들의 선거구를 번호를 기준으로 그리기
                    draw_other(x,y,d1,d2,new_array)


                    min_people=bfs(array,new_array) # 인구 가장 많은 선거구와 가장 적은 선거구 인구차이 반환(최솟값)
                    final_answer = min(min_people,final_answer)

    return final_answer
print(solve())