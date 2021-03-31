# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH
# 5:15 시작
# 7:50 종료

# 2시간 35분 소요
"""
문제
1. 자석 수 4개, 각 자석은 8개의 날
2. 1개 자석 회전할 때 서로 붙은 날의 자성이 다를 경우에만 반대 방향으로 1칸 회전
3. 시계방향 1, 반시계 방향 -1
4. n극 0, s극 1

출력: 획득한 점수의 총 합


풀이
1. 매 턴마다 어떤 자석을 어떤 방향으로 회전시켜야 하는지 기록
2. 기록한 자석들 회전

시행착오
1. 문제를 잘못이해-> 자석은 모두 동시에 회전해야 되는데 처음 구현할 때는 하나씩 순차적으로 회전시켰음.
2. 변수명을 안바꾸고 여러번 사용해서 꼬였음.


"""

import sys
sys.stdin = open("4013.txt")

def check(array):

    ans = 0
    score = [1,2,4,8]
    for i in range(4):
        if array[i][0]:
            ans += score[i]
    return ans


def solve():
    for num,dir in turn_list:
        possible_index = [] # (가능한 톱니바퀴, 방향)

        # 현재 위치는 턴 가능
        possible_index.append((num,dir))

        # 현재 위치랑 겹친 부분 체크
        pos_right, pos_left = num, num
        next_right,next_left = num+1, num-1
        ldir,rdir = dir,dir

        # 왼쪽
        while next_left >=0:
            if array[pos_left][-2] != array[next_left][2]:
                ldir = 1 if ldir == -1 else -1
                possible_index.append((next_left,ldir))
                pos_left = next_left
                next_left -=1
            else:
                break

        # 오른쪽
        while next_right<4:
            if array[pos_right][2] != array[next_right][-2]:
                rdir = 1 if rdir == -1 else -1
                possible_index.append((next_right,rdir))
                pos_right=next_right
                next_right +=1
            else:
                break

        for x,dir in possible_index:
            array[x].rotate(dir)

    answer =check(array)
    return answer

from collections import deque
T = int(input())
for tc in range(T):
    K = int(input())
    array = []
    turn_list = []
    for _ in range(4):
        array.append(deque(list(map(int,input().split()))))

    for _ in range(K):
        temp = list(map(int,input().split()))
        turn_list.append([temp[0]-1,temp[1]])

    print('#{0} {1}'.format(tc+1,solve()))
