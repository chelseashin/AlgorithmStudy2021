# deque 사용

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

from collections import deque

def solution(progresses, speeds):
    answer = []
    pq = deque(progresses)
    sq = deque(speeds)
    N = len(progresses)
    while pq and sq:
        for i in range(len(pq)):
            pq[i] += sq[i]
        temp = 0
        while pq and pq[0] >= 100:
            pq.popleft()
            sq.popleft()
            N -= 1
            temp += 1
        if temp:
            answer.append(temp)
    return answer

print(solution(progresses, speeds))