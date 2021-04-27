from collections import defaultdict
# 애초에 두 값이 바뀌면서 올라가야하네
def solve(a, tree, node, visited):
    answer = 0
    if node!=0 and len(tree[node]) == 1:
        return 0, a[node]
    visited[node] = True
    for i in tree[node]:
        if not visited[i]:
            ra, a[i] = solve(a, tree, i, visited)
            answer += (ra + abs(a[i]))
            a[node] += a[i]
    if node == 0:
        if a[node] != 0:
            return -1, a[node]
    return answer, a[node]
        

def solution(a, edges):
    tree = defaultdict(list)
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    return solve(a, tree, 0, [False]*len(a))[0]  

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0],[[0,1],[1,2]]))