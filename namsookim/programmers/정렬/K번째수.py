"""
https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
"""

def solution(array, commands):
    answer = []
    for start,end,k in commands:
        temp=sorted(array[start-1:end])
        answer.append(temp[k-1])
    return answer
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))