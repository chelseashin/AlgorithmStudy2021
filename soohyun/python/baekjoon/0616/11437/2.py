import sys
from collections import defaultdict, deque
from enum import Enum
input = sys.stdin.readline

class CMD(Enum):
    GRAPH = 0
    QUERY = 1

def solution(graph, depth):
    def LCA(start, end):
        while True:
            if depth[start] == depth[end]:
                if start == end:
                    return start
                else:
                    start, end = graph[start], graph[end]
            elif depth[start] > depth[end]:
                start = graph[start]
            else:
                end = graph[end]

    for start, end in input_value(CMD.QUERY):
        yield LCA(start, end)


def input_value(cmd):
    N = int(input().rstrip()) - 1 if cmd == CMD.GRAPH else int(input().rstrip())
    for _ in range(N):
        start, end = map(int, input().rstrip().split(" "))
        yield start, end


def make_pgraph(graph):
    pgraph = [0] * (len(graph.keys())+1)
    depth_info = [0] * (len(graph.keys())+1)
    queue = deque()
    queue.appendleft((1, 0))
    while queue:
        parent, depth = queue.popleft()
        childs = graph[parent]
        for child in childs:
            if child != 1 and pgraph[child] == 0:
                pgraph[child] = parent
                depth_info[child] = depth + 1
                queue.append((child, depth+1))
    return pgraph, depth_info


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
    graph, depth = make_graph()
    for sol in solution(graph, depth):
        print(sol)
    

if __name__ == "__main__":
    main()