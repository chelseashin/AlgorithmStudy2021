# https://www.acmicpc.net/problem/14711
# 20:14 start
# 22:25 pass
# 아직도 이해가 잘 되진 않음....
# 참고링크 : https://jaimemin.tistory.com/1067

from sys import stdin
input = stdin.readline

# main
N = int(input())
graph = [""] * (N+1)
graph[0] = input().rstrip()
visited = [[0] * N for _ in range(N)]
# print(graph)
for i in range(N):
    for j in range(N):
        if graph[i][j] == "#":
            if j > 0:   # 좌
                visited[i][j-1] ^= 1    # ^= : XOR(다르면 1 같으면 0)
            if j < N-1: # 우
                visited[i][j+1] ^= 1
            if i < N-1: # 하
                visited[i+1][j] ^= 1

    for j in range(N):
        if visited[i][j]:
            graph[i+1] += "#"
        else:
            graph[i+1] += "."
    
    print(graph[i])
    

# for idx in range(1, N+1):
#     print(''.join(graph[idx]))