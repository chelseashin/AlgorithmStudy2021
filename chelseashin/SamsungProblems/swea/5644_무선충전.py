# 18:55 start
# 20:32 finish
# 1h 37m 소요
# BFS + Simulation
# BFS로 각 BC의 충전 범위를 그려줌(다음에 풀 때는 BFS 안 쓰고 위치의 절대값으로 BC의 범위를 그려보자)
# 핵심은 두 개 이상의 BC의 범위가 겹칠 때, 성능이 큰 순으로 내림차순 정렬하는 것.
# 이동할 때, 시작 위치도 포함해야 함.
# 가장 까다로운 부분은 두 사람이 같은 BC에 있는 경우, 케이스를 나눠줌
# A만 있을 때, B만 있을 때, A, B가 둘다 있을 때, 같은 BC일 때, 다른 BC일 때의 경우를 빠짐없이 고려해야 함.

import sys
sys.stdin = open('5644_input.txt')
from collections import deque

# 그대로, 상, 우, 하, 좌
dr = (0, -1, 0, 1, 0)
dc = (0, 0, 1, 0, -1)

def bfs(sr, sc, coverage, performance, num):
    A[sr][sc].append((performance, num))
    visited = [[-1] * 10 for _ in range(10)]
    visited[sr][sc] = 0
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for d in range(1, 5):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < 10 and 0 <= nc < 10):
                continue
            if visited[nr][nc] > 0:
                continue
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] > coverage:
                    continue
                A[nr][nc].append((performance, num))    # 맵에 BC의 성능과 번호를 표시
                Q.append((nr, nc))

# main
T = int(input())
for tc in range(T):
    M, N = map(int, input().split())
    manA = [0] + list(map(int, input().split()))        # 시작 위치에서도 충전 가능하기 때문에 [0]으로 시작
    manB = [0] + list(map(int, input().split()))
    A = [[[] for _ in range(10)] for _ in range(10)]
    for n in range(1, N+1):
        x, y, C, P = map(int, input().split())
        bfs(y-1, x-1, C, P, n)

    for r in range(10):
        for c in range(10):
            A[r][c].sort(reverse=True)      # 성능 좋은 순으로 정렬

    ar, ac = 0, 0
    br, bc = 9, 9
    MAX = 0
    for m in range(M+1):      # M초 동안 이동
        ar += dr[manA[m]]
        ac += dc[manA[m]]
        br += dr[manB[m]]
        bc += dc[manB[m]]
        if A[ar][ac] and not A[br][bc]:     # A는 있고 B는 없으면
            MAX += A[ar][ac][0][0]          # 최댓값에 더하기
        elif A[br][bc] and not A[ar][ac]:   # B는 있고 A는 없으면
            MAX += A[br][bc][0][0]
        elif A[ar][ac] and A[br][bc]:       # A, B 둘 다 있을 때
            if A[ar][ac][0][1] == A[br][bc][0][1]:    # 같은 BC 이면
                MAX += A[ar][ac][0][0]                # 최대값 먼저 더하고
                if len(A[ar][ac]) > 1 and len(A[br][bc]) > 1:
                    MAX += max(A[ar][ac][1][0], A[br][bc][1][0])    # 각 위치의 두 번째 성능의 크기를 비교해 큰 값을 더해줌
                else:
                    if len(A[ar][ac]) == 1 and len(A[br][bc]) > 1:
                        MAX += A[br][bc][1][0]
                    elif len(A[br][bc]) == 1 and len(A[ar][ac]) > 1:
                        MAX += A[ar][ac][1][0]
            else:   # 다른 BC 이면
                MAX += A[ar][ac][0][0] + A[br][bc][0][0]

    print("#{} {}".format(tc+1, MAX))