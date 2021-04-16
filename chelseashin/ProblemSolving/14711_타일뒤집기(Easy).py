# https://www.acmicpc.net/problem/14711
# 20:14 start

from sys import stdin
input = stdin.readline

# main
N = int(input())
graph = [['.'] * N, list(input().rstrip())]

for i in range(1, N):
    graph.append(graph[i][:])
    for j in range(N):
        if graph[i][j] == "#":
            for dx in (-1, 0, 1):
                x = j+dx
                if 0 <= x < N:      # 흑백 뒤집기
                    if graph[i+1][x] == "#":
                        graph[i+1][x] = "."
                    else:
                        graph[i+1][x] = "#"
        if graph[i-1][j] == "#":    # 바로 위 타일이 검은색이면
            if graph[i+1][j] == "#":
                graph[i+1][j] = "."
            else:
                graph[i+1][j] = "#"
        # print((i, j))
        # for row in graph:
        #     print(row)
        # print()

for idx in range(1, N+1):
    print(''.join(graph[idx]))