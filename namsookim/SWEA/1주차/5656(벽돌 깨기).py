# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo
# 18:07 시작

# 3시간 34분 소요
"""
문제
1. 구슬을 쏘아 벽돌을 깨트리는 문제.
2. 구슬은 총 N번 쏠 수 있고, 순서를 고려해야한다.(순서가 다르면 벽돌의 상태가 바뀌기 때문에)
3. 벽돌의 값에 따라 제거되는 범위가 다르다.
4. 빈 공간이 있으면 벽돌은 밑으로 떨어진다.
5. 최대한 벽돌을 부술 때 남은 벽돌의 개수

풀이
1. 백트래킹으로 풀었다.(최대한 많은 벽돌을 경우의 수를 전부 고려하여 부셔야하기 때문에)
2. pos_index에 현재까지 구슬을 어떤 위치(열)에 쏘았는 지 기록하고 N번 쏘았을 때 값의 비교를 통해 최대 벽돌 꺠트린 것을 기록
3. 시작 전 전체 벽돌 개수 구한 뒤 최대 벽돌 깨트린 횟수를 빼서 정답 출력

시행착오
1. 벽돌 떨어트리는 것을 구현 안했다.(예제까지 꼼꼼히 읽어보기)
2. 백트래킹할 때 array 복사 위치를 잘못 설정. (복사 위치가 뒤에 있으면 첫번째 위치에 구슬 쏜것을 계속 반영하는 문제)

"""
import copy
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def block_crash(ind, array):
    find_x, find_y = H, ind
    for i in range(H):
        if array[i][ind] != 0:
            find_x = i
            break
    if find_x == H:
        return 0
    else:
        cnt=bfs(find_x,find_y,array)
        return cnt

def bfs(x,y,array):

    cnt = 0 # 벽돌 몇개 깨부셨는지 기록
    check = [[False]*W for _ in range(H)]
    q = deque([(x,y,array[x][y])])
    check[x][y] = True
    #array[x][y] = 0
    while q:
        x,y,dist=q.popleft()
        array[x][y] = 0 # 벽돌 부순거 기록
        cnt += 1 # 벽돌개수 증가
        if dist == 1:
            continue
        else: # 0이 아니면
            for i in range(4):  # 4방향
                for length in range(1,dist):
                    nx = x + dx[i]*length
                    ny = y + dy[i]*length
                    if nx<0 or ny<0 or nx>=H or ny>=W:
                        continue
                    if array[nx][ny] != 0 and check[nx][ny] !=True :# 0이 아니고 방문 아직 안했으면
                        check[nx][ny] = True # 체크처리
                        q.append((nx,ny,array[nx][ny])) # 좌표값과 벽돌정보(길이)보냄

    return cnt


def down_array(array): # 벽돌 꺠트리고 아래부터 채워주기 위한 함수
    for j in range(W):
        temp = []
        for i in range(H):
            if array[i][j] != 0:
                temp.append(array[i][j])
                array[i][j] = 0
        for i in range(H-1,-1,-1):
            if len(temp) == 0:
                break
            array[i][j]= temp.pop()


pos_index = [] # 구슬을 어떤 위치에 쏘았는지 기록

def solve(array,count): # 현재 개수
    if len(pos_index) == N: # N번 만큼 쏘면 횟수 비교후 종료
        global crash_cnt
        if crash_cnt < count:
            crash_cnt = count
        return

    else:
        for i in range(W): # 모든 열 탐색
            new_array = copy.deepcopy(array)  # 위치 실수(뒤에 있으면 첫번째 위치에 구슬 쏜것을 계속 반영)
            cnt = block_crash(i, new_array)  # 벽돌 부수기
            down_array(new_array) # 전체 내리기 (부순 벽돌 내려주기), 이거 생각을 못했음.
            pos_index.append(i) # 구슬 쏜거 기록
            count+= cnt # 현재까지 벽돌 부순거에 더함

            solve(new_array,count)
            # 원상복구
            pos_index.pop()
            count -= cnt

def check_total(array): # 전체 벽돌 개수 찾기
    cnt = 0
    for i in range(H):
        for j in range(W):
            if array[i][j]>=1:
                cnt +=1
    return cnt


import sys
sys.stdin = open("5656.txt")
input = sys.stdin.readline

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N,W,H = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(H)]
    total_block=check_total(array) # 전체 블록 개수 찾기
    crash_cnt = 0 # 최대 벽돌 깨트리는 횟수 기록
    solve(array,0)
    print("#{0} {1}".format(test_case,total_block-crash_cnt))
