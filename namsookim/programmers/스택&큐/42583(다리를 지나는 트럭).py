# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3
"""
문제
1. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는 지 구하는 문제
2. 다리에 있는 트럭의 합이 주어진 weight 보다 크면 안됨.
3. 트럭의 개수는 1개 이상

풀이
1. q라는 리스트에는 다리의 길이만큼 늘려준다. 이 리스트의 길이가 0일 때까지 반복문이 진행되고 시간을 1씩 증가시키면서 배열 길이를 줄여준다.
2. 트럭이 있으면 현재 트럭의 값과 전체 리스트 내의 트럭의 합을 더한 뒤 weight와 비교한 뒤. 다리가 지탱할 수 있는 무게보다
    같거나 작으면 트럭을 리스트에 더해주고
    크면 시간이 늘어야 하니 q의 길이를 늘려준다.

"""
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0]*bridge_length
    while q:
        time +=1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))

            else:
                q.append(0)
    return time

#print(solution(100,100,[10]))