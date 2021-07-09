from  collections import deque
class EarlyAdapter:
    def __init__(self, edapter, propagate, leaf_node):
        self.num_eadapter = edapter
        self.num_propagate = propagate
        self.num_leaf_node = leaf_node
    
    def __str__(self):
        return f'{self.num_eadapter}, {self.num_propagate}, {self.num_leaf_node}'


def calc_leaf_node(leafs, node, vertex):
    node[vertex] += 1
    if node[vertex] == 1:
        leafs[vertex] = True
    elif node[vertex] > 1 and leafs.get(vertex, None):
        leafs.pop(vertex)

def make_tree(num_node, graph):
    tree = dict()
    parent = [-1 for _ in range(num_node+1)]
    for i in range(1, num_node+1):
        tree[i] = list()
    for root in range(1, num_node+1):
        if parent[root] == -1:
            queue = deque([root])
            parent[root] = 0
            while queue:
                parent = queue.popleft()
                for child in graph[parent]:
                    if parent[child] == -1:
                        parent[child] = parent
                        tree[parent].append((parent, child))
                        queue.append(child)
    return tree, parent

    
def input_values():
    graph = dict()
    num_node = int(input().rstrip())
    leafs = dict()
    node = [0 for _ in range(0, num_node+1)]
    for i in range(1, num_node+1):
        graph[i] = list()
    for _ in range(num_node-1):
        u, v = map(int, input().rstrip().split(" "))
        graph[u].append(v)
        graph[v].append(u)
        calc_leaf_node(leafs, node, u)
        calc_leaf_node(leafs, node, v)
    tree, parent = make_tree(num_node, graph)
    return tree, parent, leafs


def get_min_early_adapter(graph, leafs, parent):
    nodes = [EarlyAdapter(0, 0, len(graph[i])) for i in range(1, len(graph)+1)]
    leaf_node = set(leafs.keys())
    while leaf_node:
        node = leaf_node.pop()
        nodes[node].num_propagate += 1
        if nodes[node].num_propagate < len(graph[node])+1:
            nodes[node].num_propagate = len(graph[node])
            nodes[node].num_eadapter = 1
        elif nodes[node].num_propagate == len(graph[node])+1:
            if nodes[node].num_eadapter >= 1:
                 nodes[node].num_propagate = len(graph[node])
                 nodes[node].num_eadapter = 1
        nodes[parent[node]].num_propagate += nodes[node].num_propagate
        nodes[parent[node]].num_eadapter += nodes[node].num_eadapter
        nodes[parent[node]].num_leaf_node -= 1
        if nodes[parent[node]] <= 0:
            leaf_node.add(parent)

       

        if nodes[parent[node]] == 0:
            leaf_node.add(parent[node])
        


def main():
    graph, parent, leafs = input_values()
    print(leafs)
    print(get_min_early_adapter(graph, leafs, parent))


if __name__ == "__main__":
    main()