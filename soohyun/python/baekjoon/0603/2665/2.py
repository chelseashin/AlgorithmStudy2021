import sys
input = sys.stdin.readline
class Node():
    def __init__(self):
        self.weight = 0
        self.trailing = []
        self.preceding_num = 0
        self.min_weight = 0

    def __str__(self):
        return str(self.weight) +' '+str(self.trailing)+' '+str(self.preceding_num)


def is_end_of_node(node):
    if node.preceding_num == 0 and len(node.trailing) == 0:
        return True
    return False


def topological_sort(node_list, empty_set, num):
    result = 0
    while len(empty_set) > 0:
        node_num = empty_set.pop(0)
        if is_end_of_node(node_list[node_num]):
           result = max(result, node_list[node_num].min_weight)

        for trailing_node in node_list[node_num].trailing:
            node_list[trailing_node].preceding_num -= 1
            if node_list[trailing_node].preceding_num == 0:
                empty_set.append(trailing_node)
            if node_list[trailing_node].min_weight <= \
                node_list[trailing_node].weight + node_list[node_num].min_weight:
                node_list[trailing_node].min_weight = node_list[trailing_node].weight + node_list[node_num].min_weight

    return result


def main():
    num = int(input().rstrip())
    node_list = [Node() for _ in range(num)]
    empty_set = list()
    for i in range(num):
        info = list(map(int, input().rstrip().split(" ")))
        node_list[i].weight = info[0]
        node_list[i].min_weight = info[0]
        if info[1] == 0:
            empty_set.append(i)

        for j in range(info[1]):
            node_list[info[1+j+1]-1].trailing.append(i)
            node_list[i].preceding_num += 1
    #for i in range(num):
    #    print("Node", i,":", node_list[i])

    print(topological_sort(node_list, empty_set, num-1))
            

if __name__ == "__main__":
    main()