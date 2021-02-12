# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH
# 3:51 시작
# 4:50 디버깅 시작
# 5:04 끝
# 1시간 13분 소요
"""
풀이
1. 1차원 check 배열을 활용해서 이미 경사로를 설치한 위치에는 설치하지 못하게 함.
2. 앞에 현재보다 1큰게 위치했을 때 뒤로체크 (뒤로가면서 check 배열에 -1이 있으면 이미 설치된 곳이니 False)
3. 앞에 현재보다 1작은게 위치했을 때 앞으로 체크. (앞으로가면서 check에 -1 처리 -> 뒤로 왔을 때 확인 가능하도록)
"""
import copy
import sys
sys.stdin = open("4014.txt")


def check_road(road):

    check = [0]*len(road) # 이미 만들어진것을 체크. -1이면 경사로 세웠다는 의미

    for i in range(N-1):
        # 2이상 차이나면 절대 못만듦
        if abs(road[i]-road[i+1]) >=2:
            return False

        # 만약 현재 높이보다 1 큰거 만나면 뒤로 x칸 체크
        if road[i] == road[i+1]-1:
            if i+1-X < 0:
                return False

            for j in range(X):# 현재 위치 기준 뒤로 x-1칸 가서 확인
                # 범위 안에 듬
                if check[i-j] == -1 or road[i-j] != road[i]: # 이미 만들어졌거나 이전값과 다르면
                    return False
                else:
                    check[i-j] = -1

        # 현재 높이보다 1작은거 만나면 앞으로 x칸 체크
        elif road[i] == road[i+1]+1:
            if i +X>=N: # i+1+X로 잘못 범위 설정
                return False

            for j in range(X):# 현재 위치 기준 뒤로 x-1칸 가서 확인
                if road[i+1+j] != road[i+1]:
                    return False
                check[i+1+j] = -1

        # 무사히 통과면 True
    return True

TC = int(input())
for tc in range(TC):

    N,X = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(N)]
    answer =0

    for road in array:
        if check_road(road):

            answer +=1

    # 행열 바꿔서 열 확인
    change_array = list(map(list,(zip(*array))))

    for c_road in change_array:
        if check_road(c_road):
            answer +=1
    print('#{0} {1}'.format(tc+1,answer))
