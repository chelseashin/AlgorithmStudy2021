# from 8:20

bridge_length = 2
weight = 10
truck_weight = [7, 4, 5, 6]

def solution(N, W, trucks):
    answer = 0
    bridge = [0] * N
    while trucks:
        if sum(bridge[1:]) + trucks[0] <= W:
            bridge.append(trucks.pop(0))
        else:
            while bridge[1] == 0:
                bridge.pop(0)
                bridge.append(0)
                answer += 1
            bridge.append(0)
        answer += 1
        bridge.pop(0)
        # print(answer, bridge, trucks)
    answer += N
    return answer

print(solution(bridge_length, weight, truck_weight))