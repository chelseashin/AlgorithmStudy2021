import sys 
input = sys.stdin.readline

def start_game(N, M, grid):
    visited = [False for _ in range(26)]
    visited[ord(grid[0][0]) -65] = True
    def recursive(row, col, count):
        #print("count", count)
        value = count
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < M:
                alpha = ord(grid[nr][nc]) - 65
                if not visited[alpha]:
                    visited[alpha] = True
                    #for i in range(len(visited)):
                    #    if visited[i]:
                    #        print(chr(i+65),end="")
                    #print()
                    return_value = recursive(nr, nc, count+1)
                    if return_value > value:
                        value = return_value

                    visited[alpha] = False
        return value
    return recursive


def main():
    N, M = map(int, input().rstrip().split(" "))
    grid = list()
    grid = [grid.append(list(input().rstrip())) for _ in range(N)]
    result = start_game(N, M, grid)
    print(result(0, 0, 1))
    

if __name__ == "__main__":
    main()