# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3
"""
문제
1. 가장 앞에 문서를 꺼낸 뒤, 나머지 문서와 전체 비교를 진행.

2. 만약 뒤에쪽에서 앞에서 꺼낸거보다 중요도가 높은 문서가 있으면 가장 앞의 문서를 가장 뒤로 보냄

3. 그렇지 않으면 앞에를 인쇄

풀이

1. 대기목록에 문서가 있으면 계속 반복문을 실행한다.

2. pop연산을 통해 가장 앞에문서를 구하고 현재 대기목록에 있는 문서를 반복문으로 돌리면서 가장 앞 문서보다 큰게 있는 지 찾는다.
   2-1) 큰게 있으면 뒤로 보내고 다시 앞에서 부터 반복문 시작
   2-2) 큰게 없으면 우선순위가 대기열 중 가장 빠른것이니 answer_list 리스트에 append

"""
def solution(priorities, location):
    answer = 0
    answer_list = []
    wait_list = []
    for num,prior in enumerate(priorities):
        wait_list.append((num+1,prior))

    while wait_list:
        index, first =wait_list.pop(0)
        tag = False
        for j in range(len(wait_list)):
            if wait_list[j][1]> first:
                wait_list.append((index,first))
                tag = True
                break
        if tag:
            continue
        else:
            answer_list.append((index,first))

    for i in range(len(answer_list)):
        if answer_list[i][0] == location+1:
            return i+1

#print(solution([2, 1, 3, 2],2))