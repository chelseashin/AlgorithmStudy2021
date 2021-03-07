# 17:00 start
# 17:18 finish
# BFS로 풀이

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        Q = deque([i])
        while Q:
            x = Q.popleft()
            for j in range(n):
                if computers[x][j] and not visited[j]:
                    visited[j] = 1
                    Q.append(j)
        answer += 1
    return answer


# DFS로 풀이 - 로직은 BFS와 똑같음

# def dfs(start, computers, visited, n):
#     for i in range(n):
#         if computers[start][i] and not visited[i]:
#             visited[i] = 1
#             dfs(i, computers, visited, n)
#
# def solution(n, computers):
#     answer = 0
#     visited = [0] * n
#     for i in range(n):
#         if visited[i]:
#             continue
#         visited[i] = 1
#         dfs(i, computers, visited, n)
#         answer += 1
#     return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))