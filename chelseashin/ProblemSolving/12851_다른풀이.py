# 50% 에서 틀림..

from sys import stdin
input = stdin.readline
from collections import deque

def bfs(n):
    global check, time
    check = [-1] * 100001
    check[n] = 0
    time = 0
    Q = deque([n])
    while Q:
        x = Q.popleft()
        for nx in [x-1, x+1, 2*x]:
            if not (0 <= nx < 100001):
                continue
            # 첫 방문
            if check[nx] == -1:
                check[nx] = check[x] + 1
                Q.append(nx)
                if nx == K:
                    time = 1
            # 한 번 이상 들리는 경우
            elif check[nx] >= check[x] + 1 and nx == K:                
                time += 1

    print(check[K])     # 최단거리
    print(time)         # 경우의 수

# main
N, K = map(int, input().split())
if N >= K:      # K가 N보다 작거나 같으면 -1로 가는 한 가지 방법 뿐
    print(N-K)
    print(1)
else:
    bfs(N)