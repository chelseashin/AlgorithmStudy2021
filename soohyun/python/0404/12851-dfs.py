# 1시 10분
import sys
import heapq


def find_sister(N, limit, visited, K):
    if N <= 1 or N > limit:
        return 0, 0
    elif visited[N]:
        return 0, 0
    elif N == K:
        return 1, 1
    else:
        visited[N] = True
        return_value = list()
        return_value.append(find_sister(N*2, limit, visited, K))
        return_value.append(find_sister(N+1, limit, visited, K))
        return_value.append(find_sister(N-1, limit, visited, K))

        min_second = 10000000000
        min_count = 0
        for second, count in return_value:
            if second == 0:
                continue
            if min_second > second:
                min_second = second
                min_count = 1
            elif min_second == second:
                min_count += 1
        visited[N] = False

        if min_second == 10000000000:
            return 0, min_count
        return min_second + 1, min_count
    

def main():
    N, K = map(int, sys.stdin.readline().rstrip().split(" "))
    i = 0
    while True:
        if (N * (i-1) < K) and (N * i >= K):
            break
        i = i + 1
    return find_sister(N, N*i, [False]*(N*i+1), K)


if __name__ == "__main__":
    min_value, min_count = main()
    print(min_value-1)
    print(min_count)