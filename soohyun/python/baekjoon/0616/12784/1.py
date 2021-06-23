from collections import defaultdict, deque
import sys
input = sys.stdin.readline
class Node():
    def __init__(self):
        self.parent = 0
        self.num_child = 0
        self.weight = 0
        self.calc_weight = 0
    def __str__(self):
        return f'parent:{self.parent} num_child:{self.num_child} weight:{self.weight} {self.calc_weight}'


def solution(graph, leaf_set):
    while len(leaf_set) > 0:
        leaf_node = leaf_set.pop()
        #print(leaf_node)
        parent = graph[leaf_node].parent
        if graph[leaf_node].calc_weight > 0 and graph[leaf_node].weight > graph[leaf_node].calc_weight:
            graph[parent].calc_weight += graph[leaf_node].calc_weight
        else:
            graph[parent].calc_weight += graph[leaf_node].weight
        
        graph[parent].num_child -= 1
        if graph[parent].num_child <= 0 and parent > 0: leaf_set.add(parent)
    return graph[1].calc_weight


def make_leafset(node_num):
    leaf_set = dict()
    for i in range(node_num+1):
        if i > 0:
            leaf_set[i] = True
    return leaf_set


def make_tree(bigraph, node_num):
    tree = [Node() for _ in range(node_num+1)]
    leaf_set = make_leafset(node_num)
    #print(leaf_set)
    tree[1].parent = 0
    queue = deque()
    queue.appendleft(1)
    while queue:
        parent = queue.popleft()
        for child, dynamite in bigraph[parent]:
            if child != 1 and tree[child].parent == 0:
                tree[child].weight = dynamite
                tree[child].parent = parent
                tree[parent].num_child += 1
                if leaf_set.get(parent, None):
                    leaf_set.pop(parent)
                queue.appendleft(child)
    return tree, leaf_set


def TC_input():
    N = int(input().rstrip())
    tree = []
    bigraph = defaultdict(list)
    for _ in range(N):
        node_num, edge_num = map(int, input().rstrip().split(" "))
        bigraph = [[] for i in range(node_num+1)]
        for _ in range(edge_num):
            start, end, dynamite = map(int, input().rstrip().split(" "))
            bigraph[start].append((end, dynamite))
            bigraph[end].append((start, dynamite))

        tree = make_tree(bigraph, node_num)
        yield tree


def main():
    for graph, leaf_set in TC_input():
        print(solution(graph, set(leaf_set.keys())))

if __name__ == "__main__":
    main()