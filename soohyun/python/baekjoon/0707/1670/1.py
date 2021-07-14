def dfs(N):
    def recursive(visited, start, end, left_visited):
        result = 0
        if left_visited == 0:
            print(start, end)
            return 1
        else:
            for nend in range(start+1, end, 2):
                for nstart in range(start+1, N):
                    recursive()

            return result
    return recursive



def main():
    N = int(input())
    result = dfs(N)
    visited = [False for _ in range(N)]
    start, end = 0, N-1
    print(result(visited, -1, -1, N))


if __name__ == "__main__":
    main()