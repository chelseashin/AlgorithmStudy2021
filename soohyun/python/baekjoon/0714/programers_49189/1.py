from collections import deque

def make_graph(n, edge):
    graph = [list() for _ in range(n)]
    for vertexes in edge:
        graph[vertexes[0]-1].append(vertexes[1]-1)
        graph[vertexes[1]-1].append(vertexes[0]-1)
    return graph
        
def solution(n, edge):
    dijkstra = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    graph = make_graph(n, edge)
    queue = deque([0])
    visited[0] = True
    max_value = [0, 0] # 가장 멀리떨어진 거리와 갯수
    while queue:
        vertex = queue.popleft()
        for adjacement_vertex in graph[vertex]:
            if not visited[adjacement_vertex]:
                visited[adjacement_vertex] = True
                queue.append(adjacement_vertex)
                dijkstra[adjacement_vertex] = dijkstra[vertex] + 1
                
                if max_value[0] < dijkstra[adjacement_vertex]:
                    max_value[0] = dijkstra[adjacement_vertex]
                    max_value[1] = 1
                elif max_value[0] == dijkstra[adjacement_vertex]:
                    max_value[1] += 1
    print("=====started=====")
    print("graph", graph)
    print("max_value", max_value)
    print("dijkstra", dijkstra)
    print("visited", visited)
                    
    return max_value[1]

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])==3)
print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]])==4)
print(solution(4, [[1, 2], [2, 3], [3, 4]])==1)
print(solution(2, [[1, 2]])==1)
print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])==2)
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]])==1)
print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]])==3)
print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]])==1)
print(solution(4, [[4, 3], [1, 3], [2, 3]])==2)