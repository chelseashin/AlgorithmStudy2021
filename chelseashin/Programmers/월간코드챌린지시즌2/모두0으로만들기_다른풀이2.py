# 참고 링크 : https://sinawi.tistory.com/262?category=649580

# 리프노드부터 연산
def dfs(node, a, edge_info):
    global answer
    # print("시작노드", node, "aaaaaaaaaaa", a, "visited", visited)
    # 무향 그래프를 그대로 사용 => 방문 체크
    if visited[node]:
        return 0
    visited[node] = 1   # 방문하지 않았다면 방문체크
    
    for i in edge_info[node]:   # 인접한 모든 노드 방문
        # print(i)
        a[node] += dfs(i, a, edge_info)
    
    # 모든 노드 방문했으면(리프노드이면)
    temp = a[node]
    a[node] = 0
    answer += abs(temp)
    return temp


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