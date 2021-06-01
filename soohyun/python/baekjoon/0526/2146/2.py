import sys
import math
input = sys.stdin.readline

def find_same_island(i, j, kmap, N, island_num):
    queue = [(i, j)]
    island_info = {(i, j)}
    kmap[i][j] = island_num
    while len(queue) > 0:
        row, col = queue.pop(0)
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1 ,1]):
            nr = row + dr
            nc = col + dc
            if nr >= 0 and nc >= 0 and nr < N and nc < N:
                if kmap[nr][nc] == 1 and (nr, nc) not in island_info:
                    kmap[nr][nc] = island_num
                    queue.append((nr, nc))
                    island_info.add((nr, nc))
    return list(island_info)


def make_island(kmap, N):
    island_num = 2
    island = dict()
    for i in range(N):
        for j in range(N):
            if kmap[i][j] == 1:
                island_info = find_same_island(i, j, kmap, N, island_num)
                island[island_num] = island_info
                island_num += 1

    return island


def bridge_bfs(island_info, kmap, island_num, N):
    queue = island_info
    visited = dict()
    result = 0
    for i, j in queue:
        visited[(i,j)]=True

    while len(queue) > 0:
        size = len(queue)
        for _ in range(size):
            row, col = queue.pop(0)
            for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                nr = row + dr
                nc = col + dc
                if nr >= 0 and nc >= 0 and nr < N and nc < N:
                    if kmap[nr][nc] == 0 and not visited.get((nr, nc), False):
                        visited[(nr, nc)] = True
                        queue.append((nr, nc))
                    if kmap[nr][nc] != 0 and kmap[nr][nc] != island_num:
                        #print("result:", result)
                        return result
        result += 1
    return result

                
def make_bridge(kmap, N, island):
    min_bridge = math.inf
    for island_num in island.keys():
        island_info = island[island_num]
        bridge = bridge_bfs(island_info, kmap, island_num, N)
        if min_bridge > bridge:
            min_bridge = bridge
    return min_bridge

def print_map(kmap):
    for i in range(len(kmap)):
        print(*kmap[i])
    print("==")


def main():
    N = int(input())
    kmap = [ list(map(int, input().rstrip().split(" "))) for _ in range(N)]

    island = make_island(kmap, N)
    #print(island)
    #print_map(kmap)
    result = make_bridge(kmap, N, island)
    print(result)


if __name__ == "__main__":
    main()