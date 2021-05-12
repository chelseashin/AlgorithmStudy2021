import heapq
from collections import defaultdict
def solution(t, r, result):
    result = []
    wait_queue = []
    time = 0
    answer = []
    info = defaultdict(list)
    i = 0
    for time, pri in zip(t, r):
        heapq.heappush(info[time], i)
        #heapq.heappush(result, (time, pri))
    while result:
        time, pri = heapq.heappop(result)
        answer.append(time)
    return answer

print(solution([0,1,3,0],[0,1,2,3],[0, 1, 3, 2]))
