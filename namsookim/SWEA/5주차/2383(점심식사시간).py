
# 10:21 시작
# 11:06 잠시 중단
# 11:24 시작
# 11:27 중단
# 11:34 시작
# 12:07 계단 계산 참고

import sys
from collections import deque

divide_result = []
def back_tracking(index,first_stair,second_stair):
    global divide_result
    global min_time
    if index == len(people):
        result = []
        result.append(sorted(first_stair))
        result.append(sorted(second_stair))
        divide_result.append(result)

        return

    # 1번에 넣기
    print(people[index] , stair[0])
    one_length = abs(people[index][0] - stair[0][0]) + abs(people[index][1] - stair[0][1])

    first_stair.append(one_length)
    back_tracking(index+1,first_stair,second_stair)
    first_stair.pop()


    # 2번에 넣기
    two_length = abs(people[index][0] - stair[1][0]) + abs(people[index][1] - stair[1][1])

    second_stair.append(two_length)
    back_tracking(index + 1, first_stair, second_stair)
    second_stair.pop()


def calc(move_person,down_time):
    wait_people ,cnt = 0,0

    down_people = []

    while move_person or wait_people>=1 or down_people:

        while wait_people:
            # 기다리는 사람 있으면
            if len(down_people) ==3:
                break
            # 사람이 3미만이면
            down_people.append(down_time)
            wait_people -=1


        for i in range(len(down_people)-1,-1,-1):
            down_people[i] -= 1
            if down_people[i] == 0:
                down_people.pop(i)

        for i in range(len(move_person)-1,-1,-1):
            move_person[i] -= 1
            if move_person[i] == 0:
                wait_people +=1
                move_person.pop(i)


        cnt +=1

    return cnt


sys.stdin = open("2383.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
INF = int(1e9)
for test_case in range(1, T + 1):
    ####################
    answer = INF
    ####################
    print('=======================')
    print(test_case, ' 번 테케')
    print('=======================')
    N = int(input())
    people = []
    stair = []
    stair_length = []
    for i in range(N):
        temp = list(map(int,input().split()))
        print(temp)

        for j in range(len(temp)):
            if temp[j] == 1:
                people.append((i,j))
            elif 2<=temp[j]<=10:
                stair.append((i,j))
                stair_length.append(temp[j])
    print('============================')

    back_tracking(0,[],[])

    # 백트래킹으로 1번 입구 vs 2번 입구 선택(모든 경우의 수 )

    # 가장 가까운 놈부터 계단을 내려가게끔 하기 위해서 heapq에 거리들 넣음
    # heapq에서 꺼내면서(해당 초로 바뀌고) queue에 삽입(큐가 3명보다 적으면) , 계단의 길이저장.
    one_queue = deque([])
    two_queue = deque([])

    # 계단을 내려가는데 걸리는 최종 시간

    for stair1,stair2 in divide_result:
        print(stair1, stair2)
        if stair1 == [2, 2, 2, 3]:
            print('=======================')

            print('=======================')

            ans =max(calc(stair1,stair_length[0]),calc(stair2,stair_length[1]))

            print(ans)
            answer = min(answer, ans)


    # 대기(3명 이상이면)
    # queue는 1초씩 감소

    # 큐에 아무도 없으면 종료: 최소 시간을 기록(가지치기 가능, 현재 시간을 가지고)
    print(answer)




