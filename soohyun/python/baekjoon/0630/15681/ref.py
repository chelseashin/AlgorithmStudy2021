import sys

input = sys.stdin.readline

def dfs(n, root, edges):
    visited = [False for _ in range(n+1)]
    result = [1 for _ in range(n+1)]
    stack = [root]
    tmp = []

    while stack:        
        current = stack[-1]
        visited[current] = True
        is_last_node = True

        for node in edges[current]:

            if not visited[node]:
                stack.append(node)
                is_last_node = False
        
        if not is_last_node:
            continue
        

        tmp.append(stack.pop())

    for node in tmp:
        for parent in edges[node]:
            if visited[parent]:
                result[parent] += result[node]
        visited[node] = False

    return result

def main(n, r, q, edges, querys):
    result = dfs(n, r, edges)

    for query in querys:
        print(result[query])


if __name__ == '__main__':
    n, r, q = map(int, input().rstrip().split(' '))
    edges = [[] for _ in range(n+1)]

    for _ in range(n-1):
        node1, node2 = map(int, input().rstrip().split(' '))
        edges[node1].append(node2)
        edges[node2].append(node1)
    
    querys = [int(input().rstrip()) for _ in range(q)]


    main(n, r, q, edges, querys)
