def dfs(graph, nodes):
    min_result = 100
    child_list = list()
    for node in nodes:
        if not graph.get(node, False) or len(graph[node]) <= 0:
            continue
        child_list.extend(graph[node])
    if len(child_list) <= 0:
        return len(nodes)
    else:
        for _ in range(len(child_list)):
            node = child_list.pop(0)
            result = dfs(graph, child_list)
            child_list.append(node)
            if result < min_result:
                min_result = result
        return min_result + len(nodes)
            

def main(n, edges):
    graph = dict()
    for edge in edges:
        parent, child = tuple(edge)
        if graph.get(parent) is None:
            graph[parent] = [child]
        else:
            graph[parent].append(child)
    result = dfs(graph, [0])
    print(result)
    return 

main(19, [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]])
main(14, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]])
main(10,[[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]])
        


