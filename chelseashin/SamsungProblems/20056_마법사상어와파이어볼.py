# from 16:10 to 17:50
# 1h 40m

import sys
sys.stdin = open("20056_input.txt")
from collections import deque
input = sys.stdin.readline

# 8방향
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1)

N, M, K = map(int, input().split())
Q = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    Q.append((r-1, c-1, m, d, s))

# K번 이동
for k in range(K):
    qlen = len(Q)
    info = dict()   # 딕셔너리로 현재 맵에 있는 파이어볼 관리
    for _ in range(qlen):
        sr, sc, sm, sd, ss = Q.popleft()
        nr = (sr + dr[sd] * ss) % N
        nc = (sc + dc[sd] * ss) % N
        if (nr, nc) not in info.keys():
            info[(nr, nc)] = [(sm, sd, ss)]
        else:
            info[(nr, nc)].append((sm, sd, ss))
    # 이동 후 처리
    for key, values in info.items():
        if len(values) == 1:    # 값이 한 개라면 그대로 큐에 담기
            Q.append((key + values[0]))
            continue
        # 같은 위치의 파이어볼이 2개 이상이면
        vlen = len(values)
        tm, td, ts = 0, 0, 0
        for t in range(vlen):
            tm += values[t][0]
            td += values[t][1] % 2      # 홀짝 구분 위해 2로 나눈 나머지를 더해줌
            ts += values[t][2]
        # 질량
        tm //= 5
        if tm == 0:
            continue
        # 속력
        ts //= vlen
        # 방향
        if td == 0 or td == vlen:  # 방향이 모두 홀수이거나 모두 짝수이면(= 나머지의 합이 0이거나 값의 갯수만큼이면)
            dd = [0, 2, 4, 6]
        else:
            dd = [1, 3, 5, 7]
        for cd in dd:               # 큐에 담에 줄 때 이동한 위치를 담아줘서 계속 틀림.. 현 위치를 넣어줘야 위에서 정상적으로 이동 처리됨
            Q.append(key + (tm, cd, ts))

fireball = 0
for qv in Q:
    fireball += qv[2]
print(fireball)