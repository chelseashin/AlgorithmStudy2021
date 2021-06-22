import math
import heapq

class Node():
    def __init__(self, num, weight):
        self.con_node = num
        self.con_weight = weight
    
    def __str__(self):
        return f'[node: {self.con_node}, weight: {self.con_weight}]'


def dijkstra(start_node, nodes_num, graph):
    min_dist = [math.inf] * nodes_num
    min_dist[start_node] = 0
    queue = [(0, start_node)]
    
    while queue:
        weight, popped_node = heapq.heappop(queue)
        for node in graph[popped_node]:
            if weight + node.con_weight < min_dist[node.con_node]:
                min_dist[node.con_node] = weight + node.con_weight
                heapq.heappush(queue, (min_dist[node.con_node], node.con_node))
    #print(min_dist)

    return min_dist

def main():
    num_of_person, num_of_road, destination = map(int, input().rstrip().split(" "))
    graph = [list() for _ in range(num_of_person)]
    for _ in range(num_of_road):
        start, end, weight = map(int, input().rstrip().split(" "))
        graph[start-1].append(Node(end-1, weight))

    #for idx, node_list in enumerate(graph):
    #    print(idx, *node_list)

    arr_dest_to_start = dijkstra(destination-1, num_of_person, graph)
    #print(arr_dest_to_start)
    max_num = 0
    for i in range(num_of_person):
        if i == (destination-1):
            continue
        start_to_dest = dijkstra(i, num_of_person, graph)[destination-1]
        max_num = max(start_to_dest + arr_dest_to_start[i], max_num)
    return max_num

if __name__ == "__main__":
    print(main())