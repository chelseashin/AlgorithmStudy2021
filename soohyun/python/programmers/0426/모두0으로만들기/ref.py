
"""Solution code for "Programmers 76503. 모두 0으로 만들기

- Problem link: https://programmers.co.kr/learn/courses/30/lessons/76503
- Solution link: http://www.teferi.net/ps/problems/programmers/76503
"""

import sys

sys.setrecursionlimit(10**9)


def solution(a, edges):
    def dfs(u, parent=None):
        answer = 0
        for child in graph[u]: # 리프노드까지 이동
            if child != parent:
                answer += dfs(child, u)
        if parent is None: # 부모노드까지 온경우
            if a[u] != 0: # 부모노드가 0이 아닌경우
                return -1 
        else: # 부모노드가 아닌경우
            answer += abs(a[u]) # 답은 노드 값을 돌려줌
            a[parent] += a[u] # 부모값도 현재값을 더함
            print(answer, a)
        return answer

    graph = [[] for _ in a]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return dfs(0)
#a	edges	result


solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])
solution([0,1,0],[[0,1],[1,2]])