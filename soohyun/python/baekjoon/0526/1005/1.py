import sys
from collections import defaultdict
input = sys.stdin.readline
class Node:
    def __init__(self, id, value):
        self.id = id
        self.next_nodes = set()
        self.from_nodes = set()
        self.min_value = value
        self.value = value


    def __str__(self):
        return "{0}, next_node: {1}, from_node: {2}, min_value: {3}, value: {4}".format(self.id, self.next_nodes, 
                                           self.from_nodes, self.min_value, 
                                           self.value)


def topological_sort(candid_node, node_list, find_node):

    empty_node = [key for key in candid_node.keys()]
    start_node = empty_node[0]
    while len(empty_node) > 0:
        if start_node == find_node:
            break
        start_node = empty_node.pop(0)
        next_nodes = list(node_list[start_node].next_nodes)
        for next_node in next_nodes:
            node_list[next_node].from_nodes.pop()
            if node_list[next_node].value + node_list[start_node].min_value > node_list[next_node].min_value:
                node_list[next_node].min_value = node_list[next_node].value +\
                                                 node_list[start_node].min_value
            if len(node_list[next_node].from_nodes) == 0:
                empty_node.append(next_node)

    return node_list[start_node].min_value 
 
    


def main():
    T = int(input().rstrip())
    for _ in range(T):
        N, K = map(int, input().rstrip().split(" "))
        node_list = list()
        candid_node = dict()
        for i in range(N):
            candid_node[i] = True
        seconds = list(map(int, input().rstrip().split(" ")))

        for i, second in enumerate(seconds):
            node_list.append(Node(i, second))

        for _ in range(K):
            from_node, to_node = list(map(int, input().rstrip().split(" ")))
            node_list[from_node-1].next_nodes.add(to_node-1)
            node_list[to_node-1].from_nodes.add(from_node-1)
            if candid_node.get(to_node-1, None):
                candid_node.pop(to_node-1)
        find_node = int(input())
        result = topological_sort(candid_node, node_list, find_node-1)
        print(result)


if __name__ == "__main__":
    main()