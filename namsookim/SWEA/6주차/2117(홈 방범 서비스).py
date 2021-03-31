# 6:51 시작
# 8:35 종료

# 1시간 45분 소요
"""
풀이
1.마름모 범위에 house들이 속하는 지 판단.
2.total_score 이상이면 개수 갱신
3.완전탐색 ㄱㄱ

시행착오
1. total_money>= (k*k) + (k-1)*(k-1):  이상이어야 함.(문제 똑바로 읽기)
2. k범위를 잘못 설정
"""
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu

def install(x,y,k,house):

    up_x,up_y = x-k+1 , y
    down_x,down_y = x+k-1, y

    left_up_x, left_up_y = up_x, up_y
    left_down_x, left_down_y = down_x, down_y

    ans = 0

    # 한번만 더하도록
    tag= False

    while True:
        if up_x > down_x:
            break

        for house_x, house_y in house:

            # 오른쪽
            if up_x <= house_x <= down_x and up_y == house_y:
                ans +=1

            # 첫 빵은 한번만 더함
            if tag:
                if left_up_x <= house_x <=left_down_x and left_up_y == house_y:
                    ans +=1


        tag = True
        up_x += 1
        down_x -= 1
        up_y += 1

        left_up_x += 1
        left_down_x -= 1
        left_up_y -= 1

    total_money=ans * M

    if total_money>= (k*k) + (k-1)*(k-1): # 이부분 때문에 틀림

        return ans
    else:
        return 0


import sys

sys.stdin= open("2117(홈 방범 서비스).txt")

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    answer = 0
    array = [list(map(int,input().split())) for _ in range(N)]

    house = []
    for i in range(N):
        for j in range(N):
            if array[i][j] == 1:
                house.append((i,j))

    # 보안회사가 손해를 보지 않고 서비스 가능한 최대 집의 수 구하기
    for k in range(1,N+2):
        for x in range(N):
            for y in range(N):

                answer=max(install(x,y,k,house),answer)


    # 0,0 부터 N-1 , N-1 까지
    # K는 1부터 N까지
    # k가 1일 때 몇개의 집을 포함하는 지 체크 후 계산
    # k가 2일 때 몇개의 집을 포함하는 지 체크 후 계산 ....
    print('#{0} {1}'.format(tc,answer))

