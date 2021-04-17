# 14:32 start
# 15:25 pass

# (검사할 노드, 바이러스 퍼뜨린 컴퓨터 수, 간선 정보)
def dfs(Q, cnt, edges_info):
    global result
    if cnt >= result:   # 바이러스 퍼뜨린 컴퓨터 수가 이미 최솟값보다 크거나 같으면 가지치기
        return

    nextQ = []          # 바이러스 퍼뜨릴 노드 담기
    for start in Q:
        if start not in edges_info.keys():      # 자식 노드 없으면 continue
            continue
        for end in edges_info[start]:
            nextQ.append(end)       # 다음에 감염될 컴퓨터 번호들
    # print(nextQ, cnt)

    if not nextQ:                   # 더이상 검사할 노드 없으면(== 리프노드에 도달하면)
        result = min(result, cnt)   # 최솟값 갱신

    # 연결 끊기
    for nx in range(len(nextQ)):    # nextQ에 담긴 노드들 중 하나씩 연결 끊으면서 다음 검사 시행
        dfs(nextQ[:nx]+nextQ[nx+1:], cnt + (len(nextQ) - 1), edges_info)   # (끊은 간선 제외 다른 간선 정보, 갯수 넘기기)

def solve(n, edges):
    global result
    result = float('inf')
    edges_info = dict()     # 컴퓨터 간선 정보(시작노드 : [도착 노드들])
    for s, e in edges:
        if s not in edges_info.keys():
            edges_info[s] = [e]
        else: edges_info[s].append(e)
    # print(edges_info)

    dfs([0], 1, edges_info)     # 다음 검사할 컴퓨터들, 감염된 컴퓨터 수, 간선 정보
    return result

print(solve(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))
print(solve(14, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]))
print(solve(10, [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]))

# 7
# 4
# 2