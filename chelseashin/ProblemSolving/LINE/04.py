# 22:25 start
# 23:27 finish
# 1시간 2분

def solution(maze):
    # 상 우 하 좌
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)
    cnt = 0
    N = len(maze)
    A = [[1] * (N + 2)]
    for row in maze:
        A.append([1] + row + [1])
    A.append([1] * (N + 2))
    # for a in A:
    #     print(a)
    r, c, d = 1, 1, 1
    while True:
        if (r, c) == (N, N):     # 탈출
            return cnt
        d = (d+3) % 4
        for _ in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if A[nr][nc] == 1:
                d = (d+1) % 4     # 벽 만나면 시계 방향으로 방향 전환
                continue
            r, c = nr, nc
            cnt += 1
            break

print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]))