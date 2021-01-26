from collections import deque
# https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

# 10분 소요
"""
문제 

문제가 무슨 얘기하는지 이해하기 힘들어 예제를 통해 이해했다.
1. 현재 위치에서 마지막 위치까지 탐색하면서 가격이 떨어지는 지점에 break를 건다. 
2. 이를 통해 언제까지 가격이 안떨어지는 지 알 수 있다.

풀이
1. 이중 for 문을 구현해 마지막 까지 탐색하면서 가격이 떨어지는 지점에 break를 걸어 언제까지 가격이 
   안 떨어지나 반환해주었다.

"""
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)

    return answer

print(solution([1,2,3,2,3]))