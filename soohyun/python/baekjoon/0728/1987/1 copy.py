from collections import deque

def start_game(N, M, grid):
    visited = [[set() for _ in range(M)] for _ in range(N)]
    #alpha_visited = dict()
    visited[0][0].add(grid[0][0])
    #alpha_visited.add((grid[0][0],1))
    queue = deque([(0, 0,  1)])
    while queue:
        row, col, count = queue.popleft()
        print(row, col, visited, count)
        for dr, dc, in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < M:
                if grid[nr][nc] in visited[row][col]:
                    continue
                visited[nr][nc] = visited[nr][nc].union(visited[row][col])
                visited[nr][nc].add(grid[nr][nc])
                queue.append((nr, nc, count+1))
    return count

def main():
    N, M = map(int, input().rstrip().split(" "))
    grid = list()
    for _ in range(N):
        grid.append(list(input().rstrip()))
    print(start_game(N, M, grid))
    

if __name__ == "__main__":
    main()