# 35분 소요
from heapq import heappush, heappop, heapify

def solution(t, r):
    answer = []
    info = dict()
    N = len(t)
    minT = float('inf')
    for idx in range(N):
        minT = min(minT, t[idx])
        if t[idx] not in info.keys():
            info[t[idx]] = []              # hq
            heappush(info[t[idx]], (r[idx], idx))
        else: heappush(info[t[idx]], (r[idx], idx))

    time, cnt = minT, 0
    while cnt < N:
        if time not in info.keys():
            time += 1
            continue
        r, i = heappop(info[time])
        answer.append(i)
        cnt += 1        # 탑승한 사람
        if info[time]:  # 값이 남았을 때
            if time+1 in info.keys():   # 다음 시간에 값이 있으면
                info[time+1].extend(info[time])
                heapify(info[time+1])   # heapify
                del info[time]
            else:   # 다음 시간에 없으면
                info[time+1] = info[time]
                del info[time]
        time += 1
        # print("현재 info 상태", info, "answer 상태", answer)
    
    return answer

print(solution([0,1,3,0], [0,1,2,3]))
print(solution([7,6,8,1], [0,1,2,3]))