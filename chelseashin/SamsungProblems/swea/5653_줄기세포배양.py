# 9:05 start
# 9:30 문제 이해 완료하면서 설계해보지만 잘 되지 않음
# 10:00 이전 코드 참고..하며 어렵지 않은 문제라는 것을 깨달음
# 11:20 end
# 2h 15m 별 의미 없는 시간. 다음에 풀면 내 힘으로 풀 수 있을 것 같다!!!!!

# 1. X시간 동안 비활성
# 2. X시간 지나는 순간 활성 => 활성 되는 순간 4방향 번식(이미 있음 번식x, 동시=> 생명력 높은 아이로)
# 3. X시간 후 죽음

import sys
sys.stdin = open("5653_input.txt")
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    time = 0
    while Q and time < K:      # K 시간 동안 배양
        qlen = len(Q)
        for _ in range(qlen):
            r, c = Q.popleft()
            origin = raw[r][c][0]   # 원래 가진 값
            life = raw[r][c][1]     # 세포 죽을 때까지 남은 시간
            if life == 0:           # 남은 시간 0이면 죽은 세포
                continue
            if origin != life:
                raw[r][c][1] -= 1       # 남은 시간 1 감소 후
                if raw[r][c][1] > 0:    # 살아있는 세포들만 큐에 담기
                    Q.append((r, c))
                continue

            for d in range(4):      # 활성화 되는 순간 4방향 번식
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N+K and 0 <= nc < M+K):
                    continue
                if raw[nr][nc] == 0:
                    # 번식 : [생명력, 활성화되기까지 남은 시간, 번식된 시간]
                    raw[nr][nc] = [origin, 2*origin, time]
                    Q.append((nr, nc))
                # 번식하려는 곳이 이미 방문된 상태인데,
                # 현재 생명력이 기존 생명력보다 크고, 현 시간이 기존의 번식된 시간과 같다면
                elif origin > raw[nr][nc][0] and time == raw[nr][nc][2]:
                    raw[nr][nc] = [origin, 2*origin, time]
            raw[r][c][1] -= 1       # 남은 시간 1 감소 후
            if raw[r][c][1] > 0:    # 살아있는 것만 큐에 담기
                Q.append((r, c))
        time += 1
        # print(time, "시간 후")
        # for a in raw:
        #     print(a)

# main
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    raw = [[0] * (K+M) for _ in range(K+N)]    # 줄기세포 초기 상태
    start = K//2
    for r in range(N):
        raw[start + r][start:start+M] = list(map(int, input().split()))

    Q = deque()
    for r in range(start, start+N):
        for c in range(start, start+M):
            if raw[r][c]:
                Q.append((r, c))        # 확인할 세포 좌표 담기
                raw[r][c] = [raw[r][c], raw[r][c] * 2, 0]

    bfs()    # 줄기세포 번식

    print("#{} {}".format(tc+1, len(Q)))