import math

class Node():
    def __init__(self, row, col, count):
        self.row = row
        self.col = col
        self.count = count
    
    def __str__(self):
        return '({0}, {1})'.format(self.row, self.col)


def find_min(start, kmap, N, island_num):
    queue = [Node(start[0], start[1], 0)]
    visited = {start:0}
    final_result = math.inf
    while queue:

        node = queue.pop(0)
        row, col, count = node.row, node.col, node.count
        if kmap[row][col] > 0 and kmap[row][col] != island_num:
            print("end", (row, col), kmap[row][col], "count:",count)
            if final_result > count:
                final_result = count
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nrow = row + dr
            ncol = col + dc
            #print(visited, (nrow, ncol))
            if 0 <= nrow < N and 0 <= ncol < N:
                if visited.get((row, col), 1) <= node.count: 
                    continue
                    #print("true", (row, col),(nrow, ncol))#, visited)
                else:
                    #print("in", (row, col), (nrow, ncol))
                    print(visited)
                    count = node.count+1 if kmap[nrow][ncol]==0 else node.count
                    visited[(nrow, ncol)] = count
                    queue.append(Node(nrow, ncol, count))
                    #for i, value in enumerate(queue):
                    #    print(i, value, end=' ')
                    #print()
    return final_result


def bfs(kmap, N, start, island_num):
    queue = [start]
    kmap[start[0]][start[1]] = island_num
    while queue:
        row, col = queue.pop(0)
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nrow = row + dr
            ncol = col + dc
            if 0 <= nrow < N and 0 <= ncol < N:
                if kmap[nrow][ncol] == 1:
                    kmap[nrow][ncol] = island_num
                    queue.append((nrow, ncol))


def separate_island(N, kmap):
    island_rep = []
    island_num = 2
    for i in range(N):
        for j in range(N):
            if kmap[i][j] == 1:
                island_rep.append((i, j))
                bfs(kmap, N, (i, j), island_num)
                island_num += 1
    return island_rep


def make_min_bridge(island_rep, N, kmap):
    min_bridge = math.inf
    for i, j in island_rep:
        print("start==", (i, j), kmap[i][j])
        num_bridge = find_min((i, j), kmap, N, kmap[i][j])
        print("count", num_bridge)
        if min_bridge >= num_bridge:
            min_bridge = num_bridge
    return min_bridge
        

def print_map(kmap):
    print("========")
    for i in range(len(kmap)):
        print(*kmap[i])
    print("==========")


def main():
    N = int(input())
    kmap = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
    
    # map 변경하기
    island_rep = separate_island(N, kmap)
    #
    print_map(kmap)
    # 하나씩 바꿔보기
    min_value = make_min_bridge(island_rep, N, kmap)
    return min_value



if __name__ == "__main__":
    print(main())
