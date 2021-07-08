# 1시간 5분
# 코딩시간 30분
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def is_visited(visited, child, is_red):
    return child in visited[not is_red] or child in visited[is_red]


def is_bigraph(graph, num_of_node):

    checked = [False for _ in range(num_of_node+1)]
    for i in range(1, num_of_node+1):
        if checked[i]:
            continue
        root, is_red = i, True
        queue = deque([(root, is_red)])
        visited = defaultdict(set)
        visited[is_red].add(root)
        checked[root] = True
        while queue:
            parent, is_red = queue.popleft()
            for child in graph[parent]:
                if is_visited(visited, child, is_red):
                    if child in visited[is_red]:
                        return False
                else:
                    visited[not is_red].add(child)
                    checked[child] = True
                    queue.append((child, not is_red))
    return True


def input_values():
    N = int(input().rstrip())
    for _ in range(N):
        graph = dict()
        num_vertex, num_edge = map(int, input().rstrip().split(" "))
        for i in range(1, num_vertex+1):
            graph[i] = list()
        for _ in range(num_edge):
            node_1, node_2 = map(int, input().rstrip().split(" "))
            graph[node_1].append(node_2)
            graph[node_2].append(node_1)
        yield graph, num_vertex


def main():
    for graph, num_of_node in input_values():
        print("YES") if is_bigraph(graph, num_of_node) else print("NO")


if __name__ == "__main__":
    main()