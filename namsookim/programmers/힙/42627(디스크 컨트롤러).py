# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
# https://davinci-ai.tistory.com/35
# 참고: https://seoyoung2.github.io/algorithm/2020/06/04/Programmers-diskcontroller.html

# 시간 체크 다시
# 12:52 시작
# 3:04 끝

"""

풀이
1. 먼저 처음 시작은 가장 처음에 요청한 작업부터 완료시킨다.
2. 그 다음 바로 수행할 수 있는 작업중 작업시간이 가장 짧은 것을 먼저 선택한다.
3. 바로 수행할 수 있는 작업이 없다면 작업 시간을 +1 늘려준다.

시행착오
1. 하드디스크가 작업을 수행하고 있지 않으면 먼저 요청이 들어온 작업부터 처리한다
  -> 가장 처음 요청된 작업부터 처리

"""
import heapq

def solution(jobs):
    
    # last = 최근 작업이 끝난 시간
    # count = 처리한 작업수
    # time = 총 작업시간
    count , last, answer = 0,-1,0
    heap =[]
    jobs.sort()
    # 시작시간 초기화
    time = jobs[0][0]
    while count < len(jobs):
        for s,t in jobs:
            if last < s <= time:
                heapq.heappush(heap,(t,s))
        if len(heap)>0: # 가능한 것이 있으면
            count +=1
            last = time
            term , start = heapq.heappop(heap)
            time += term
            answer += (time - start)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time +=1

    return answer//count

print(solution([[0, 3], [1, 9], [2, 6]]))
