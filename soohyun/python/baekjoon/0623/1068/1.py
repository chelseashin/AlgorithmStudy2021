# 걸린시간 1시간
import sys
from collections import defaultdict
input = sys.stdin.readline

def remove_graph(graph, remove_node):
    def recursive(remove_node):
        if graph.get(remove_node, None) is None:
            return
        else:
            children = graph[remove_node]
            graph.pop(remove_node)
            for child in children:
                recursive(child)
    recursive(remove_node)
    

def count_graph(graph, remove_node):
    count = 0
    for _, value in graph.items():
        if len(value) == 0:
            count += 1
        elif len(value) == 1 and value[0] == remove_node:
            count += 1
    return count


def main():
    graph = dict()
    N = int(input().rstrip())
    for i in range(N):
        graph[i] = list()
    nodes = list(map(int, input().rstrip().split(" ")))
    for node, parent in enumerate(nodes):
        if parent != -1:
            graph[parent].append(node)
    remove_node = int(input().rstrip())
    remove_graph(graph, remove_node)
    print(count_graph(graph, remove_node))


if __name__ == "__main__":
    main()
