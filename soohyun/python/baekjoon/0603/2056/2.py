DIECTION = {(-1, 0):1, (1, 0):2, (0, -1):3, (0, 1):4}

def dfs(N, visited, start, poss):
    result = 0
    if N[0] == 0:
        return poss
    for i, j in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        nrow, ncol = start[0] + i, start[1] + j
        if not visited.get((nrow, ncol), False):
            visited[(nrow, ncol)] = True

            N[0] -= 1
            semi_result = dfs(N, visited, 
                          (nrow, ncol), 
                          N[DIECTION[(i, j)]] * poss)
            result += semi_result
            visited.pop((nrow, ncol))
            N[0] += 1
    return result


def main():
    N = list(map(int, input().rstrip().split(" ")))
    #print(N)
    visited = {(0, 0):True}
    for i in range(len(N)):
        if i > 0:
            N[i]/=100
    print(dfs(N, visited, (0, 0), 1))

if __name__ == "__main__":
    main()