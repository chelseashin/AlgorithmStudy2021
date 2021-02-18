# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
"""
3분 소요
논문의 수 : 1000개

개수가 적어 O(N^2)으로 해결.

1. 현재 h-index 이상인 개수를 센다.
2. 같을 경우 break해줌. h_index를 늘리고 계속 반복.
3.반복문을 통과해도 개수를 충족 못시키면 현재까지의 최대값을 리턴한다.
"""

def solution(citations):
    answer = 0 # h-index
    while True:
        cnt = 0
        answer += 1

        for i in range(len(citations)):
            if citations[i] >= answer:
                cnt += 1
            if cnt == answer: # h_index 더 늘려도 됨.
                break
        else: # h_index까지 도달 못하면 break하고 최대값 -1을 해줌
            break

    return answer - 1
