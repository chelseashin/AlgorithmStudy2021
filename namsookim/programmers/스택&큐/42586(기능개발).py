# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# 23분 소요
"""
문제
1. 배포되어야 하는 순서대로 진행해야 된다. 첫번째가 안끝났는데 2번째가 끝났다고 해서 배포하는 것이 아니라 기다려야함.
2. 동시에 배포되는 기능의 개수를 리스트 형태로 출력

풀이
1. 현재 처리해야되는 기능이 100 이상이 될때까지 더해준다.
2. 100 이상이 되면 빠져나와 현재 기능부터 몇번쨰까지 100이상인지 개수를 센 뒤 출력한다. 동시에 개수를 셀 때 방문처리를 해주어
   시간을 절약한다.

"""
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    check = [False] * n # 100이 넘었는지 체킹

    for i in range(n):
        if check[i] == True: # 100 넘은 기능은 넘어감
            continue

        while True: #100이 안넘은 기능을 기준으로 100이상이 될 때까지 더해줌.
            if progresses[i] >= 100:
                break
            for j in range(len(progresses)):
                progresses[j] += speeds[j]


        cnt = 0
        for k in range(i,n): # 현재 기능을 기준으로 몇개가 100이 넘는지 체크
            if progresses[k]>=100:
                cnt +=1
                check[k] = True
            else:
                break
        answer.append(cnt)

    return answer

print(solution([95, 90, 99, 99, 80, 99]	, [1, 1, 1, 1, 1, 1]))