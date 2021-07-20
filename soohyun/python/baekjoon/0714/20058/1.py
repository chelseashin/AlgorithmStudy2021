from collections import deque

def tornado(start_row, end_row, start_col, end_col, grid):
    diff = end_row - start_row
    sample_grid = [[grid[i][j] for j in range(start_col, end_col)] \
                               for i in range(start_row, end_row)]
    for i in range(diff):
        for j in range(diff):
            grid[start_row+j][start_col+(diff-i-1)] = sample_grid[i][j]


def bfs(row, col, grid, visited, N):
    queue = deque([(row, col)])
    visited[row][col] = True
    sum = 0#grid[row][col]
    count = 0
    while queue:
        row, col = queue.popleft()
        #print(row, col)
        count += 1
        sum += grid[row][col]
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc] > 0 and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc]=True

    return sum, count


def start_magic(grid, L):
    N = len(grid)
    for l in L:
        calc = 2**l
        for i in range(0, N, calc):
            for j in range(0, N, calc):
                tornado(i, i+calc, j, j+calc, grid)

        melt_list = list()
        for i in range(0, N):
            for j in range(0, N):
                count = 0
                for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                    nr, nc = i+dr, j+dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] > 0:
                            count += 1
                if count < 3:
                    melt_list.append((i, j))
        for i, j in melt_list:
            grid[i][j] = grid[i][j] - 1 if grid[i][j] > 0 else grid[i][j]

    visited = [[False]*N for _ in range(N)]
    sum = 0
    max_block = 0
    for i in range(0, N):
        for j in range(0, N):
            if grid[i][j] > 0 and not visited[i][j]:
                result = bfs(i, j, grid, visited, N)
                sum += result[0]
                if max_block < result[1]:
                    max_block = result[1]
    return sum, max_block    
        
                
def print_tornado(grid):
    for row in grid:
        print(*row)


def main():
    width, _ = map(int, input().rstrip().split(" "))
    grid = list()
    for _ in range(2**width):
        grid.append(list(map(int, input().rstrip().split(" "))))
    L = list(map(int, input().rstrip().split(" ")))
    result = start_magic(grid, L)
    print(result[0])
    print(result[1])



if __name__ == "__main__":
    main()