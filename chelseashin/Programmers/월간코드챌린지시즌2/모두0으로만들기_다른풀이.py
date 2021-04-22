# 문제 : https://programmers.co.kr/learn/courses/30/lessons/76503
# 참고 링크 : https://bladejun.tistory.com/120
# 그림 설명 잘 돼있음..!
# DFS로 풀이

import sys
sys.setrecursionlimit(300000)

# 시작 노드, a, 간선 정보
def dfs(x, a, edge_info):
    global visited, N, answer
    now = a[x]
    visited[x] = 1

    # print("visited", visited, "시작노드", x, "now", now, "answer", answer)
    for i in edge_info[x]:
        if not visited[i]:
            now += dfs(i, a, edge_info)

    answer += abs(now)      # 리프노드일 때 더해줌.
    # print("현재값", answer)
    return now

def solution(a, edges):
    global visited, N, answer
    if sum(a) != 0:     # 불가능한 경우
        return -1

    answer = 0
    N = len(a)
    edge_info = [[] for _ in range(N)]
    for s, e in edges:
        edge_info[s].append(e)
        edge_info[e].append(s)
    # print("edge_info ============================", edge_info)
    # print("aaaaaaaaaaa", a)

    visited = [0] * N
    dfs(0, a, edge_info)        # 0부터 시작
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0], [[0,1],[1,2]]))

# 참고해보자
# https://sinawi.tistory.com/262?category=649580
