# from 19:20 to 21:13
# 20:26 tc 다 맞는데, 돌리자마자 틀림..
# 계속 틀린 원인은 변수명.... r, c를 너무 여러군데 쓰면서 꼬임..
# 디버깅으로 거의 1시간 소요ㅜㅜ 이거 해결하니 정답
# 1h 53m.. 쉬운 문제인데 너무 오래 걸렸다 반성하자!

import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def move():
    global flag
    visited = [[0] * N for _ in range(N)]
    for sr in range(N):
        for sc in range(N):
            if A[sr][sc] and not visited[sr][sc]:
                nations = [(sr, sc)]    # 국가 리스트
                visited[sr][sc] = 1
                Q = deque([(sr, sc)])
                cnt = 1
                total = A[sr][sc]       # 연합 국가의 인구 합
                while Q:
                    r, c = Q.popleft()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if not (0 <= nr < N and 0 <= nc < N):
                            continue
                        if visited[nr][nc]:
                            continue
                        if L <= abs(A[r][c] - A[nr][nc]) <= R:     # 인구 차이
                            visited[nr][nc] = 1
                            Q.append((nr, nc))
                            nations.append((nr, nc))
                            cnt += 1
                            total += A[nr][nc]
                            flag = True
                if cnt > 1:     # 연합 있으면 평균값으로 채워주기
                    new_num = total // cnt
                    for r, c in nations:
                        A[r][c] = new_num      # 새 값으로 갱신

# main
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = 0
while True:
    flag = False
    move()      # 인구이동
    if flag:
        result += 1
    else:
        break
print(result)