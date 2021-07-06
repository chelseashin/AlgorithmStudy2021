import sys
from collections import defaultdict
input = sys.stdin.readline

DIRECTION = {0:(-1, 0), 1:(-1, 1), 2:(0, 1), 3:(1, 1),
             4:(1, 0), 5:(1, -1), 6: (0, -1), 7:(-1, -1)}
class Node:
    def __init__(self, row, col, mass, speed, direction):
        self.row = row
        self.col = col
        self.mass = mass
        self.speed = speed
        self.direction = direction

    def __str__(self):
        return f'({self.row}, {self.col}) m:{self.mass} s:{self.speed} d:{self.direction} '


def add(node_list):
    new_nodelist = list()
    first_node = node_list[0]
    is_all_odd_even = True
    new_mass = 0
    total_mass, total_speed, total_direction = \
        first_node.mass, first_node.speed, first_node.direction
    for node in node_list[1:]:
        total_mass += node.mass
        total_speed += node.speed
        if total_direction % 2 != node.direction % 2:
            is_all_odd_even = False

    directions = [0, 2, 4, 6] if is_all_odd_even else [1, 3, 5, 7]
    for new_direction in directions:
        if total_mass // 5 > 0:
            new_mass += total_mass // 5
            node = Node(
                first_node.row, 
                first_node.col,
                total_mass // 5,
                total_speed // len(node_list),
                new_direction
            )
            new_nodelist.append(node)
    return new_nodelist, new_mass


def move_node(node_list, N):
    loc_dict = defaultdict(list)
    while node_list:
        node = node_list.pop()
        node.row = (node.row + \
            N + (DIRECTION[node.direction][0] * node.speed) % N ) % N   
        node.col = (node.col + \
            N + (DIRECTION[node.direction][1] * node.speed) % N ) % N 
        loc_dict[(node.row, node.col)].append(node)
    return loc_dict


def move(node_list, N, K):
    mass_result = 0

    for _ in range(K):
        loc_dict = move_node(node_list, N)
        node_list = []
        mass_result = 0
        for new_node_list in loc_dict.values():
            if len(new_node_list) > 1:
                new_node_list, mass = add(new_node_list)
                mass_result += mass
            else:
                mass_result += new_node_list[0].mass
            node_list.extend(new_node_list)
    return mass_result


def input_values():
    node_list = list()
    N, M, K = map(int, input().rstrip().split(" "))
    for _ in range(M):
        r, c, m, s, d = map(int, input().rstrip().split(" "))
        node_list.append(Node(r, c, m, s, d))
    return N, K, node_list
        
        
def main():
    N, K, node_list = input_values()
    print(move(node_list, N, K))


if __name__ == "__main__":
    main()