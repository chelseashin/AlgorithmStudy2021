def make_pascal(N, M):
    graph = [[0] * (N+1) for _ in range (N+M+1)]
    if N == 0:
        return graph
    graph[0][0] = 1
    graph[1][1] = 1
    graph[1][0] = 1
    for i in range(2, N+M+1):
        for j in range(0, N+1):
            if j == 0 or j == i:
                graph[i][j] = 1
            else:
                num = graph[i-1][j] + graph[i-1][j-1]
                if num > 10**9:
                    num = 10**9
                graph[i][j] = num
    return graph


def calc(A, Z, C, K):
    N, R = A + Z, A
    data = []
    if A > 0:
        for _ in range(1, A+Z+1):
            if R <= 0 or N == R:
                continue
            if C[N-1][R-1] >= K:
                data.append('a')
                N, R = N-1, R-1
            else:
                K -= C[N-1][R-1]
                data.append('z')
                N, R = N-1, R

        left_a = R
        while left_a > 0:
            left_a -= 1
            data.append('a')

    while len(data) < A+Z:
        data.append('z')

    return ''.join(data)


def main():
    N, M, K= map(int, input().rstrip().split(" "))
    pascal = make_pascal(N, M)
    if pascal[-1][-1] < K:
        print(-1)
    else:
        result = calc(N, M, pascal, K)
        print(result)


if __name__ == "__main__":
    main()