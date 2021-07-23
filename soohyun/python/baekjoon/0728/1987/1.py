from collections import deque

def start_game(N, M, grid):
    #visited = [[False] * M for _ in range(N)]
    #alpha_visited = dict()
    #visited[0][0] = True
    #alpha_visited.add((grid[0][0],1))
    queue = set((0, 0, set(grid[0][0]), 1))
    while queue:
        row, col, visited, count = queue.pop()
        #print(row, col, visited, count)
        for dr, dc, in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < M:
                #print(visited)
                if grid[nr][nc] in visited:
                    continue
                new_visited = set()
                # new_visited = new_visited.union(visited)
                new_visited.add(grid[nr][nc])
                queue.append((nr, nc, new_visited.union(visited), count+1))
    return count

def main():
    N, M = map(int, input().rstrip().split(" "))
    grid = list()
    for _ in range(N):
        grid.append(list(input().rstrip()))
    print(start_game(N, M, grid))
    

if __name__ == "__main__":
    main()