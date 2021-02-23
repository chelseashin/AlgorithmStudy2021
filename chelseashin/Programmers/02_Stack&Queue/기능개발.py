# deque 사용

from collections import deque

def solution(progresses, speeds):
    answer = []
    pq = deque(progresses)
    sq = deque(speeds)
    N = len(progresses)
    while N:
        for i in range(N):
            pq[i] += sq[i]
        temp = 0
        while pq and pq[0] >= 100:
            pq.popleft()
            sq.popleft()
            temp += 1
            N -= 1
        if temp:
            answer.append(temp)     # 각 배포마다 몇 개의 기능 배포되는지
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))