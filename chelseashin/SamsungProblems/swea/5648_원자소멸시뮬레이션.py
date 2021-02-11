import sys
sys.stdin = open("5648_input.txt")

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    global Q
    result = 0
    while Q:
        info = dict()
        qlen = len(Q)
        for _ in range(qlen):
            r, c, d, k = Q.pop(0)
            nr = r + dr[d] * 0.5
            nc = c + dc[d] * 0.5
            # 격자 밖으로 나가면 더이상 충돌할 수 없기 때문에 그냥 두기
            if not (0 <= nr < 2001 and 0 <= nc < 2001):
                continue
            if (nr, nc) not in info.keys():     # 첫 방문인 경우
                info[(nr, nc)] = [d, k]
            else:                               # 이미 어떤 원자가 간 곳이면
                info[(nr, nc)][0] = -1
                info[(nr, nc)][1] += k
        for (r, c), (d, k) in info.items():
            if d == -1:                         # 처음 도착해 충돌된 원자 소멸 처리
                result += k
            else:
                Q.append((r, c, d, k))
    return result

T = int(input())
for tc in range(T):
    N = int(input())
    Q = []
    for i in range(N):
        c, r, d, k = map(int, input().split())
        # 격자를 수학적으로 일반적인 이차원 배열에 놓인 위치로 계산
        r = 2000 - (1000 + r)
        c = (1000 + c)
        Q.append((r, c, d, k))

    print("#{} {}".format(tc + 1, bfs()))