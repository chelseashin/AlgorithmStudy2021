from collections import deque

def start_game(N, M, grid):
    queue = set()
    queue.add((0, 0, grid[0][0], 1))
    max_count = 0
    while queue:
        row, col, visited, count = queue.pop()
        max_count = max(count, max_count)
        print("print", row, col, visited)
        for dr, dc, in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < M:
                print(nr, nc, grid[nr][nc], visited)
                if grid[nr][nc] in visited:
                    continue
                #visited += grid[nr][nc]
                #queue.add((nr, nc, visited, count+1))
                visited += grid[nr][nc] # 이렇게되면 visited가 적용됨
                queue.add((nr, nc, visited+grid[nr][nc], count+1))
    return max_count

def main():
    N, M = map(int, input().rstrip().split(" "))
    grid = list()
    for _ in range(N):
        grid.append(list(input().rstrip()))
    #print(grid)
    print(start_game(N, M, grid))
    

if __name__ == "__main__":
    main()