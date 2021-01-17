# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

# 8:18 시작
# 9:11 종료
# 50분 소요
"""
문제
1. 삽입, 최대값 삭제, 최솟값 삭제 명령어가 있을 때 이러한 명령어를 사용한 뒤 남아있는 최대값과 최소값을 구하는 문제

풀이
1. 최소힙, 최대힙 2개를 사용해서 관리한다.

2. 최대힙, 최소힙에 같은 값만이 담기도록 조작해준다.
   - 최대힙에서 최대값 추출 시 , 최소힙에서 동일한 값을 삭제
   - 최소힙에서 최소값 추출 시 , 최대힙에서 동일한 값을 삭제

3. 최대힙에서의 최대값, 최소힙에서의 최소값을 반환한다.
"""
import heapq
def solution(operations):
    answer = [] # 답을 담을 변수

    min_queue=[] # 최소힙에 사용
    max_queue=[] # 최대힙에 사용

    for a in operations:
        temp=list(a)
        op = str(temp[0])
        number = int(''.join(temp[2:]))

        if op == 'I': # 삽입
            heapq.heappush(min_queue, number)
            heapq.heappush(max_queue, -1*number) # 최대힙을 사용하기 위해 *-1 처리

        elif op == 'D': # 추출해라
            if number == 1: # 최대힙에서 추출
                if len(max_queue) == 0:
                    continue

                max_value=heapq.heappop(max_queue)
                min_queue.remove(-1*max_value)

            elif number == -1: # 최소값에서 추출
                if len(min_queue) == 0:
                    continue
                min_value = heapq.heappop(min_queue)
                max_queue.remove(-1*min_value)

    max_result = 0
    min_result = 0

    if len(max_queue)!=0:
        max_result = heapq.heappop(max_queue)
    if len(min_queue)!=0:
        min_result = heapq.heappop(min_queue)

    answer.append(-1*max_result)
    answer.append(min_result)

    return answer

#print(solution(["I 16","D 1"]))
#print(solution(["I 7","I 5","I -5","D -1"]))