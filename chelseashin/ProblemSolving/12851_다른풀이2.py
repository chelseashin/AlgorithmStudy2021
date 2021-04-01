# 최적화 풀이
# 코드 참고 : https://rebas.kr/750
# 코드 참고 X, 좋은 그릠 : https://dirmathfl.tistory.com/145

from sys import stdin
input = stdin.readline
from collections import deque

def bfs():
    check = [-1] * 100001
    check[N] = 0
    Q = deque([N])
    time = 0
    while time == 0:
        qlen = len(Q)
        # 이렇게 해준 이유는 time이 이번 턴에 갱신됐다면 다음 턴을 해볼 필요가 없으므로
        # 즉, 다음 턴과 구분해 while문을 빨리 나가기 위함.
        for _ in range(qlen):
            x = Q.popleft()
            if x == K:      # K에 도달할 때마다 +1
                time += 1
            for nx in (x-1, x+1, x*2):
                if not (0 <= nx < 100001):
                    continue
                # 첫 방문이거나 방문한 적 있을 때 이동 거리가 같다면 큐에 담기
                if check[nx] == -1 or check[nx] == check[x]+1:
                    check[nx] = check[x] + 1
                    Q.append(nx)

    print(check[K])     # 최소 시간
    print(time)         # 경우의 수

# main
N, K = map(int, input().split())
if N >= K:      # K가 N보다 작거나 같으면 -1로 가는 한 가지 방법 뿐
    print(N-K)
    print(1)
else:
    bfs()