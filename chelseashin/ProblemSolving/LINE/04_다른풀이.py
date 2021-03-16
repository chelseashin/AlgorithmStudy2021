# 다른 풀이

# 상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

def solution(maze):
    cnt = 0
    N = len(maze)
    r, c, d = 0, 0, 2
    while True:
        if (r, c) == (N-1, N-1):
            return cnt
        # 왼쪽 확인하고 갈 수 있으면 가고 못 가면 나머지 3방향 탐색
        ld = (d+3) % 4
        lr = r + dr[ld]
        lc = c + dc[ld]
        # 격자 안이고 빈 공간이면 왼쪽으로 갈 수 있음
        if (0 <= lr < N and 0 <= lc < N) and not maze[lr][lc]:
            r, c = lr, lc
            d = ld
        # 격자 밖으로 나가거나 벽 만나면 그 방향으로 못 감
        else:
            for _ in range(3):
                lr = r + dr[d]
                lc = c + dc[d]
                if (0 <= lr < N and 0 <= lc < N) and not maze[lr][lc]:
                    r, c = lr, lc
                    break
                d = (d+1) % 4
        # print(cnt, (r, c), d)
        cnt += 1

print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
# print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
# print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))