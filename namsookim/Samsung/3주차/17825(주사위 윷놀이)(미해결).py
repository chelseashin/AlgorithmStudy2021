# https://www.acmicpc.net/problem/17825
# 주사위 윷놀이
# 11:23
# 11:58 중단
# 12:25 시작
# 2:02 중단
# 10:40 시작
# 11:56 중단
# 16:21 시작
# 18:15 종료
# 19:18 종료

import sys
input = sys.stdin.readline

board = [[i for i in range(0,42,2)], # 시작부터 도착까지
          [10,13,16,19,25,30,35,40], # 10 밟을 때
         [20,22,24,25,30,35,40], # 20 밟을 때
        [30,28,27,26,25,30,35,40]] # 30 밟을 때

dice = list(map(int,input().split())) # 주사위 값 받기

position = [[0,0] for _ in range(4)]

answer = 0

def possible(section, index):
    global position

    if [section, index] in position: # 현재 구역의 위치에 누가 있으면
        return False

    # 교차하는 지점 체크
    # 다른 구역이지만 말판이 같아지는 경우
    if board[section][index] == 25 or board[section][index] == 30 or board[section][index] == 35 or board[section][index] == 40:

        back_num = len(board[section]) - index  # 뒤에서 몇 번째 인지를 기록

        if board[section][index] == 40: # 40이면 모든 구역에서 뒤에서 1번째
            # section 0,1,2,3 같을 수 있음
            for i in range(4):
                if [i, len(board[i]) - back_num] in position:
                    return False

        else: # 25, 30, 35 일 경우
            # section 0,1,2 같을 수 있음
            for i in range(1,4):
                if [i,len(board[i]) - back_num] in position:
                    return False

    return True


def back_tracking(num,total_score):
    global position  # 현재 말의 구역과 위치정보
    if num == 10: # 주사위 10개 모두 사용시 결과 비교후 저장
        global answer
        if total_score>answer:
            answer = total_score

        return

    # 전체 10개 주사위 돌리기
    #for i in range(num,10):

    for hores in range(4):

        # 도착시킨 말이 있으면 이동시키지 않음
        if position[hores] == [-1,-1]:
            continue

        section, index = position[hores] # 구간과 index 값

        new_index = index + dice[num] # 새로운 위치
        new_score = 0

        if new_index >=len(board[section]): # 범위 벗어나면 도착한 표시
            position[hores] = [-1,-1]

        else: # 범위 내에 있으면
            new_score = board[section][new_index]  # 새로운 값의 점수
            new_section = section
            tag = False # 구역이 바뀌었는 지 체크

            if new_score % 10 == 0 and new_section == 0 and new_score //40 != 1:
                tag = True # 구역이 바뀌었음
                new_section = new_score // 10

            """

            if section == 0: # 실수
                if new_score == 10: # 10을 밟으면
                    tag = True
                    new_section = 1

                elif new_score == 20:
                    tag = True
                    new_section = 2

                elif new_score == 30:
                    tag = True
                    new_section = 3
            """

            if tag: # 만약 구역이 바뀌었으면
                if possible(new_section,0): # 이미 위치에 말이 있는 지 체크   , 말이 없으면 True 반환
                    position[hores] = [new_section,0] # 새로운 구역의 인덱스를 0으로
                else:
                    continue # 이미 차지하고 있으니 다른 말 선택

            else:
                if possible(new_section,new_index):  # 사용하는 지 체크
                    position[hores] = [new_section,new_index]
                else:
                    continue

        back_tracking(num+1,total_score+new_score) # 현재 주사위 위치 올리고, 점수 총합

        # 이동한거 원상복구
        position[hores] = [section,index]


back_tracking(0,0)
print(answer)
