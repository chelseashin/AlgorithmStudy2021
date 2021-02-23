from collections import deque

def solution(priorities, location):
    answer = 0
    Q = deque([(value, idx) for idx, value in enumerate(priorities)])
    while Q:
        value, idx = Q.popleft()
        if Q and value < max(Q)[0]:     # 남은 값들 중 가장 큰 값보다 작다면 
            Q.append((value, idx))
        else:                           # 가장 큰 값이면 그대로 프린트
            answer += 1
            if idx == location:         # 확인해야 한 값이면 탈출
                break
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))