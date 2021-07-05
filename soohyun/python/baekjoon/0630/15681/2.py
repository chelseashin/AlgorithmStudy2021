import sys
from collections import defaultdict, deque
input = sys.stdin.readline

class Input:
    def __init__(self, query, num_node, root, graph):
        self.query = query
        self.graph = self.make_tree(root, graph)
        self.num_node = num_node
        self.number_of_subtree = self.count_subtree(root)
        self.leaf_node = set()
        print(self.number_of_subtree)

    def make_tree(self, root, graph):
        tree = defaultdict(list)
        visited = [False]*(len(graph.keys())+1)
        visited[root] = True
        parent = root
        queue = deque([root])
        while queue:
            parent = queue.pop()
            for child in graph[parent]:
                if not visited[child]:
                    visited[child] = True
                    tree[parent].append(child)
                    queue.append(child)
        return tree

    def count_subtree(self, node):
        print(self.graph)
        sub_trees = [0]*(self.num_node+1)
        queue = deque([node])
        while queue:
            parent = queue[-1]
            if len(self.graph[parent]) == 0:
                queue.pop()
                sub_trees[parent] += 1
            else:
                for child in self.graph[parent]:
                    queue.append(child)
                    self.graph[parent].pop()
                    sub_trees[parent] += 1

        return visited


def input_values():
    bigraph = defaultdict(list)
    num_node, root, query = map(int, input().rstrip().split(" "))
    for _ in range(num_node-1):
        node1, node2 = map(int, input().rstrip().split(" "))
        bigraph[node1].append(node2)
        bigraph[node2].append(node1)
    return Input(query, num_node, root, bigraph)


def query(input_values):
    for _ in range(input_values.query):
        yield input_values.number_of_subtree[int(input().rstrip())]


def main():
    for result in query(input_values()):
        print(result)


if __name__ == "__main__":
    main()
    