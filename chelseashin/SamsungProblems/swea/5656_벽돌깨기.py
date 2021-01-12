# from 16:31 to 18:43
# 2h 12m
# 여러 번 풀었던 문제임에도 시간이 꽤 걸림
# 깨트린 벽돌 갯수 셀 때 초기 값(cnt)을 1로 해주지 않아 답이 자꾸 틀림..(여기서 한 20분 소요 후 바로 정답)
# 벽돌 깨트리고 복원 후 break로 나가야 제대로 돌아감. 이 부분은 항상 헷갈림..

import sys
sys.stdin = open("5656_input.txt")
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 폭탄 터트리고 땅으로 내려주기
def bfs(sr, sc, sp):
    visited = [[0] * W for _ in range(H)]   # 깨트린 벽돌 표시
    visited[sr][sc] = 1
    raw[sr][sc] = 0
    Q = deque([(sr, sc, sp)])   # 벽돌의 좌표, 폭발의 범위
    cnt = 1     # 깨트린 벽돌 갯수
    while Q:
        r, c, p = Q.popleft()
        for d in range(4):
            for power in range(1, p):
                nr = r + dr[d] * power
                nc = c + dc[d] * power
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if raw[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    Q.append((nr, nc, raw[nr][nc]))
                    raw[nr][nc] = 0     # 깨트릴 때마다 0으로 바꾸기
                    cnt += 1
    # 중력
    for i in range(W):
        remain = []     # 남은 벽돌
        for j in range(H-1, -1, -1):
            if raw[j][i]:
                remain.append(raw[j][i])
                raw[j][i] = 0
        for k in range(len(remain)):
            raw[H-k-1][i] = remain[k]
    return cnt      # 깨트린 벽돌 갯수 리턴

def dfs(depth, total):
    global raw, MIN
    if depth == N or total == 0:    # 구슬 다 썼거나 모든 벽돌을 깼다면
        MIN = min(MIN, total)       # 최솟값 갱신
        return
    R = [x[:] for x in raw]         # 현 상태 저장
    for w in range(W):
        for h in range(H):
            if raw[h][w]:                      # 세로 탐색하다가 값이 있으면
                temp = bfs(h, w, raw[h][w])    # 폭탄 터트리고, 중력 처리.
                dfs(depth+1, total-temp)
                raw = [r[:] for r in R]        # 복원
                break                          # 해당 열 구슬 작업 끝났다면 나가기
# main
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    bricks = 0  # 최초 상태의 전체 벽돌 수
    raw = []
    for h in range(H):
        raw.append(list(map(int, input().split())))
        for w in range(W):
            if raw[h][w]:
                bricks += 1
    MIN = bricks
    dfs(0, bricks)
    print("#{} {}".format(tc+1, MIN))