# 19:42 start
# 20:17 finish
# 20:23 52%에서 틀렸습니다..

from sys import stdin
input = stdin.readline
from collections import deque

N, K = map(int, input().split())
if N >= K:      # K가 N보다 작거나 같으면 -1로 가는 한 가지 방법 뿐
    print(N-K)
    print(1)
    exit()

check = [-1] * 100001
check[N] = 0
Q = deque([N])

time = 0
while Q:
    x = Q.popleft()
    if x == K:
        time += 1
    for nx in [x-1, x+1, 2*x]:
        if not (0 <= nx < 100001):
            continue
        # 첫 방문이거나 현 위치 + 1 값으로 갱신할 수 있는 경우
        if check[nx] == -1 or check[nx] >= check[x] + 1:
            check[nx] = check[x] + 1
            Q.append(nx)
                
print(check[K])     # 최단거리
print(time)         # 경우의 수