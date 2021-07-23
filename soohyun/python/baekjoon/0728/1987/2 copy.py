import sys
sys.setrecursionlimit(10000) 

input = sys.stdin.readline
def start_game(N, M, grid):
    visited = [False for _ in range(26)]
    visited[grid[0][0]] = True
    def recursive(row, col, count):
        #print(row, col, count)
        #print("count", count)
        value = count
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < M:
                alpha = grid[nr][nc]
                if not visited[alpha]:
                    visited[alpha] = True
                    return_value = recursive(nr, nc, count+1)
                    if return_value > value:
                        value = return_value
                        #return value
                    visited[alpha] = False
        return value
    return recursive


def main():
    N, M = map(int, input().rstrip().split(" "))
    #grid = list()
    grid = [list(map(lambda x:ord(x) - 65, input().rstrip())) for _ in range(N)]
    result = start_game(N, M, grid)
    print(result(0, 0, 1))
    

if __name__ == "__main__":
    main()