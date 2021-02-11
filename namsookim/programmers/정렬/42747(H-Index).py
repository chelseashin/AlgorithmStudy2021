# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3
"""
3분 소요
1. 오름차순으로 정렬한 뒤, 현재 h-index 이상인 개수를 센다.
2. 같을 경우 break해주고 반복문을 통과해도 개수를 충족 못시키면 현재까지의 최대값을 리턴한다.
"""

def solution(citations):
    answer = 0
    citations.sort()
    while True:
        cnt = 0
        answer += 1
        for i in range(len(citations)):
            if citations[i] >= answer:
                cnt += 1
            if cnt == answer:
                break
        else:
            break
    return answer - 1
