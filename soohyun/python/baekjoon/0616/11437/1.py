import sys
from collections import defaultdict
from enum import Enum
input = sys.stdin.readline
class CMD(Enum):
    GRAPH = 0
    QUERY = 1

    
def LCA(start, end, graph):
    start_parent = {start}
    end_parent = {end}
    while True:
        if start > 0:
            start = graph[start]
            start_parent.add(start)
            if start_parent.intersection(end_parent):
                break
        if end > 0:
            end = graph[end]
            end_parent.add(end)
            if start_parent.intersection(end_parent):
                break
    return start_parent.intersection(end_parent).pop()

def input_value(cmd):
    N = int(input().rstrip()) - 1 if cmd == CMD.GRAPH else int(input().rstrip())
    for _ in range(N):
        start, end = map(int, input().rstrip().split(" "))
        yield start, end


def make_pgraph(graph):
    pgraph = {1: 0}
    visited = [False]*len(graph.keys())
    visited[0] = True
    queue = [1]
    while queue:
        parent = queue.pop(0)
        childs = graph[parent]
        for child in childs:
            if pgraph.get(child, -1) < 0:
                pgraph[child] = parent
                queue.append(child)
    return pgraph

def make_graph():
    graph = defaultdict(list)    
    # 양방향 그래프 1부터 들어온다는 보장이 없으므로
    for start, end in input_value(CMD.GRAPH):
        graph[start].append(end)
        graph[end].append(start)

    # 부모 그래프
    pgraph = make_pgraph(graph)
    return pgraph


def main():
    graph = make_graph()
    #print(graph)
    for start, end in input_value(CMD.QUERY):
        print(LCA(start, end, graph))



if __name__ == "__main__":
    main()