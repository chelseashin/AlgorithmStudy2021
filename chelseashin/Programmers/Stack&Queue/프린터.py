priorities = [2, 1, 3, 2]
location = 2

from collections import deque

def solution(priorities, location):
    answer = 0
    Q = deque((value, idx) for idx, value in enumerate(priorities))
    while True:
        i, v = Q.popleft()
        if Q and v < max(Q)[0]:
            Q.append((i, v))
        else:
            answer += 1
            if i == location:
                break
        answer +=1
    print(Q, max(Q))
    return answer

print(solution(priorities, location))