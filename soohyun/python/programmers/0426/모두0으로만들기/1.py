def solve(tree, a, visited, node):
    answer = 0
    if len(tree[node]) == 1: # is leaf node
        return 0, a[node]
    child_node = tree[node]
    for child in child_node:
        if not visited[child]:
            visited[child] = True
            count, node_value = solve(tree, a, visited, child)
            answer += (count + node_value)
            a[node] += node_value
    return answer, a[node]
    

def solution(a, edges):
    answer = -2
    
    tree = dict()
    visited = []
    for i in range(len(a)):
        tree[i] = list()
        if i == 0:
            visited.append(True)
        else: visited.append(False)
        
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    
    if sum(a) == 0:
        result = solve(tree, a, visited, 0) 
        return result[0]
        
    else:
        return -1

