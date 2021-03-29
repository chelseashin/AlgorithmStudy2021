# 12:10 start
# 12:57 finish
# 47m 소요

import sys
sys.stdin = open("2382_input.txt")

# 상하좌우
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
rev = (0, 2, 1, 4, 3)

# main
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    microbe = [list(map(int, input().split())) for _ in range(K)]

    # M시간 움직임
    for _ in range(M):
        info = dict()
        for idx in range(K):
            r, c, n, d = microbe[idx]
            if not n:   # 소멸된 미생물은 검사 X
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            microbe[idx][0], microbe[idx][1] = nr, nc
            if not (1 <= nr < N-1 and 1 <= nc < N-1):
                n //= 2         # 미생물 수 절반
                d = rev[d]      # 방향 전환

            # 미생물 수, 방향 저장
            if (nr, nc) not in info.keys():
                info[(nr, nc)] = [(idx, n, d)]
            else:
                info[(nr, nc)].append((idx, n, d))

        # microbe 갱신 - 충돌하지 않았을 때, 충돌했을 때 처리
        for values in info.values():
            if len(values) == 1:    # 충돌 X
                i, n, d = values[0]
                microbe[i][2] = n
                microbe[i][3] = d
            else:                   # 충돌 O
                total = 0
                maxIdx, maxCnt = -1, -1
                for i, n, d in values:
                    total += n
                    if maxCnt < n:
                        maxIdx = i
                        maxCnt = n
                microbe[maxIdx][2] = total
                for i, n, d in values:
                    if i != maxIdx:
                        microbe[i][2] = 0   # 미생물 흡수
    remains = 0
    for r, c, n, d in microbe:
        remains += n
    print("#{} {}".format(tc+1, remains))

    # 1 145
    # 2 5507
    # 3 9709
    # 4 2669
    # 5 3684
    # 6 774
    # 7 4797
    # 8 8786
    # 9 1374
    # 10 5040