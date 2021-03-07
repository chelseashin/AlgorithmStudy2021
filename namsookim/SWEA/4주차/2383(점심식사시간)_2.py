# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl&categoryId=AV5-BEE6AK0DFAVl&categoryType=CODE&problemTitle=2383&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 10:21 시작
# 11:06 중단
# 11:24 시작
# 12:07 계단 계산 참고
# 13:25 끝

# 2시간 45분 소요 - 의미 없음
# 참고 : https://mungto.tistory.com/255

"""
풀이
1. dfs로 1번 입구 vs 2번 입구 선택(모든 경우의 수 )
2. 현재 대기중인 것, 내려가는 중인것, 계단으로 이동중인 것 3가지를 나누어서 계산
3. 계단 마다 걸리는 시간 각각 계산 후 가장 오래걸리는 계단이 최종 계단에서 걸리는 시간임.
4. 최종 계단에서 걸리는 시간이 가장 작은 값 출력.

시행착오
1. 모든 경우의 수를 구할 때 백트래킹으로 구했는데 모든 경우의 수가 제대로 구해지지 않았음.
2. 계단에서 내려가는 사람, 대기중인 사람  구현하기가 까다로워서 고통스러웠음.
3. 답안을 참고했는데 전체적인 아이디어는 같았지만, 백트래킹 부분 + (대기,이동,내려감) 부분에서 구현실력이 차이났음.
4. 백트래킹 + 구현능력을 기르자.

"""
import sys

divide_result = []

def dfs(idx):

    #조합이 결정되었다면
    if idx == len(people):
        global answer
        stair_list1, stair_list2 = [], []
        #1번계단, 2번계단 분리하기
        for i in range(len(people)):
            if check[i]: stair_list1.append(people[i][0])
            else : stair_list2.append(people[i][1])

        ans = max(calc(sorted(stair_list1), stair_length[0]), calc(sorted(stair_list2), stair_length[1]))

        answer = min(answer, ans)
        return

    check[idx] = False
    dfs(idx+1)
    check[idx] = True
    dfs(idx+1)


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

    N = int(input())
    people = []
    stair = []
    stair_length = []
    for i in range(N):
        temp = list(map(int,input().split()))

        for j in range(len(temp)):
            if temp[j] == 1:
                people.append([i,j])
            elif 2<=temp[j]<=10:
                stair.append((i,j))
                stair_length.append(temp[j])

    for i in range(len(people)):
        dist1 = abs(people[i][0] - stair[0][0]) + abs(people[i][1] - stair[0][1])
        dist2 = abs(people[i][0] - stair[1][0]) + abs(people[i][1] - stair[1][1])
        people[i][0] = dist1
        people[i][1] = dist2

    check = [False]*len(people)
    dfs(0)
    print("#{0} {1}".format(test_case,answer+1))





