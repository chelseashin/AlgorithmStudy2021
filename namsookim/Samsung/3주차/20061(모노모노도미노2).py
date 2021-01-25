# https://www.acmicpc.net/problem/20061

# 7시간 소요
# 디버깅 포기
# 1시간 40분 소요

# 총 8시간 40분 소요

"""
문제
1. 파란블록, 초록블록을 이용해서 총 점수를 구하는 문제

2. 점수획득
  - 파란블록일 경우 열을 기준으로 1개의 열에 블록이 가득찰 경우 1점 획득
  - 초록블록일 경우 행을 기준으로 1개의 행에 블록이 가득찰 경우 1점 획득

3. 점수는 각 배열을 한번에 계산하는 것이 아니라, 1점씩 계산해나간다.(중요)

4. 연한부분에 블록이 찰 경우 연한칸에 블록이 위치한 행(초록색),열(파란색) 기준으로 아래(초록), 오른쪽(파랑)으로 민다.

풀이
1. 배열 3개(빨간색, 파란색, 초록색) 만듦.
2. 문제 요구사항 그대로 구현

시행착오
1. 파란색배열, 초록색배열 기준으로 점수를 한번에 계산하고 내려주었다. 한번에 계산하고 처리해주는것이 아니라 하나씩 계산 해주면서 내리는 식으로 해야한다.

2. 지역변수 선언을 인자값으로 받은 변수명과 동일한 문제.(39)
  - 인자로 받은 값이 예상치 못한 결과를 가져왔음.

"""
array = [[0] * 4 for _ in range(4)] # 빨간색 배열
blue_array = [[0]*6 for _ in range(4)] # 파란색 배열
green_array = [[0]*4 for _ in range(6)] # 초록색 배열

N = int(input()) # 블록을 놓을 횟수
info = [list(map(int,input().split())) for _ in range(N)]

def blue_input(t,x,y,array): # 파란색 집어 넣기

    # t==1이면 1x1 블록을 (x,y)에 놓음
    if t==1:
        ny = 5 # y로 받아서 틀렸었음.
        for j in range(1,len(array[0])): # 열 끝까지 탐색
            if array[x][j] != 0:
                ny = j-1
                break

        array[x][ny] = 1

    # t==2이면 1x2 블록을 (x,y),(x,y+1)에 놓음
    elif t==2:
        ny=4 # y, y+1
        for j in range(2,len(array[0])):
            if array[x][j] != 0:
                ny= j-2
                break
        array[x][ny] = 1
        array[x][ny+1] = 1


    # t==3이면 2x1 블록을 (x,y),(x+1,y)에 놓음
    elif t ==3:
        ny = 5
        for j in range(1, len(array[0])):
            #print(j)
            if array[x][j] != 0 or array[x+1][j] !=0:
                ny = j - 1
                break

        array[x][ny] = 1
        array[x+1][ny] = 1

def green_input(t,x,y,array): # 초록색 집어넣기

    # t==1이면 1x1 블록을 (x,y)에 놓음
    if t==1:
        nx = 5
        for i in range(1,len(array)):
            if array[i][y] != 0:
                nx = i-1
                break
        array[nx][y] = 1

    # t==2이면 1x2 블록을 (x,y),(x,y+1)에 놓음
    elif t == 2:
        nx = 5 # x로 그대로 쓰지말고 nx라는 새로운 변수로

        for i in range(2,len(array)):
            if array[i][y] != 0 or array[i][y+1] != 0 :  # != 0 조건 안넣음
                nx= i-1
                break

        array[nx][y] = 1
        array[nx][y + 1] = 1  # 이 안에 안넣고 바깥에 넣음. 인자로 받은 x y가 처리됨. 지역변수 실수하기 쉬우니 변수선언 잘해주기.

    # t==3이면 2x1 블록을 (x,y),(x+1,y)에 놓음
    elif t ==3:
        nx = 4
        for i in range(len(array)-1):
            if array[i + 1][y] != 0:
                nx = i - 1 # nx라고 안함
                break

        array[nx][y] = 1
        array[nx+1][y] = 1

def score_check(array,color):

    # 행과 열 검사 후
    score=0
    if color == 'blue':
        # 열 검사
        for j in range(2,6): # 진한 파란부분 열 검사
            tag = True
            for i in range(len(array)):
                if array[i][j]!= 1: # 열 검사
                    tag =False
                    break

            if tag: # 전체 열이 1이라면
                # 현재 열 기준으로 전체 1칸씩 내리기
                down_blue(j)
                score+=1

    elif color == 'green':

        # 행 검사
        for i in range(2, 6):  # 진한 초록부분 검사
            tag = False
            if sum(array[i]) == 4:
                tag = True

            if tag:  # 전체 행이 1이라면
                down_green(i)
                score += 1

    return score

def down_blue(line): # 파란색 오른쪽으로 1칸씩 밀어주기
    for j in range(line,0,-1):
        for i in range(4): # 행 4개 열 6개
            blue_array[i][j] = blue_array[i][j-1]


def down_green(line): # 초록색 아래쪽으로 1칸씩 밀어주기
    for i in range(line,0,-1):
        for j in range(4):
            green_array[i][j] =green_array[i-1][j]


def print_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=' ')
        print()


def special_check(blue_array,green_array):

    # 파란부분

    blue_cnt = 0 # 몇개 행에 있는 지 체크
    # 파란색은 열의 개수로 따짐
    for j in range(2):
        for i in range(4):
            if blue_array[i][j] == 1:
                blue_cnt +=1
                break

    # 개수만큼 밀기
    if blue_cnt == 1:
        for j in range(4,-1,-1):  # 열
            for i in range(len(blue_array)):  # 행
                blue_array[i][j+1] = blue_array[i][j]

        for i in range(len(blue_array)):
            blue_array[i][0] = 0 # 처음 행 0으로 초기화

    elif blue_cnt == 2:
        for j in range(3,-1,-1):  # 열
            for i in range(len(blue_array)):  # 행
                blue_array[i][j+2] = blue_array[i][j]

        for j in range(0,2): # 회색열 2개 처리
            for i in range(len(blue_array)):  # 행
                blue_array[i][j] = 0



    # 초록색 부분

    green_cnt = 0 # 몇개 행인지 체크

    # 초록색은 행의 개수로 따짐
    for i in range(2):
        if sum(green_array[i]) != 0:
            green_cnt += 1

    # 개수만큼 밀기
    if green_cnt == 1:
        for i in range(4, -1, -1):  # 행
            for j in range(len(green_array[0])):  # 열
                green_array[i+1][j] = green_array[i][j]

        for j in range(len(green_array[0])): # 열
            green_array[0][j] = 0 # 처음 열 0으로 초기화

    elif green_cnt == 2:
        #print_array(green_array)
        for i in range(3, -1, -1):  # 행
            for j in range(len(green_array[0])):  # 열
                green_array[i+2][j] = green_array[i][j]

        for i in range(2):
            for j in range(len(green_array[0])):
                green_array[i][j] = 0

def board_count(array,color):
    cnt = 0
    if color == 'blue':
        for i in range(4):
            cnt += sum(array[i])

    elif color =='green':
        for i in range(6):
            cnt += sum(array[i])
    return cnt


def solve(info):

    # 블록의 점수
    total_score = 0
    total_cnt = 0
    # 해당 블록을 놓음
    for t,x,y in info:

        # 파란 부분
        blue_input(t,x,y,blue_array)
        # 초록 부분
        green_input(t,x,y,green_array)
        # 행과 열 검사 (점수 획득할 수 있을 때0까지)

        blue_score = score_check(blue_array, 'blue')
        green_score = score_check(green_array, 'green')

        total_score += blue_score
        total_score += green_score

        # 연한 부분 검사
        # 오른쪽 밀기 또는 아래로 밀기
        special_check(blue_array,green_array) # 연한부분 있으면


    #얻은 점수, 초록색 보드+파란색보드 칸의 개수 출력
    total_cnt += board_count(blue_array,'blue')
    total_cnt += board_count(green_array,'green')

    print(total_score)
    print(total_cnt)


solve(info)
