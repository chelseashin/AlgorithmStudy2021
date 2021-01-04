# from 22:35 to 25:10
# 2h 15m 까지 다 푼 줄 알았지만 이 tc 틀려서 이후 20분 정도 더 디버깅.(2h 35m)
# 회전만 1시간 30분..
# 요새 추세가 진짜 simulation 인 듯. 시뮬레이션에서 시간 잡아먹히지 않도록 많이 풀어보기.
# 뒷 부분은 금방 풀 줄 알았지만 촘촘하게 짜지 않고 대강 구상만 하고 시작하여 잔 실수가 많았음
# 특히 얼음 녹이는 부분을 제대로 이해하지 못해 계속 답이 틀림.
# 문제 꼼꼼하게 읽고 풀기 전에 고려할 부분들 미리 적어놓기

import sys
sys.stdin = open("20058_input.txt")
input = sys.stdin.readline
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

# 파이어스톰 총 Q번 시전
for size in L:
    # (0, 0)에서 간격(2**size)만큼이 배열회전의 시작위치(r, c)가 됨
    new = [[0] * 2**N for _ in range(2**N)]
    gap = 2**size
    for r in range(0, 2**N, gap):
        for c in range(0, 2**N, gap):
            for i in range(gap):
                temp = A[r+i][c:c + gap]
                for j in range(gap):
                    new[r+j][c+gap-i-1] = temp[j]

    A = [x[:] for x in new]     # new에 만든 회전 후 모습 A에 반영

    # 시전 후
    melt = []   # 얼음 녹는 좌표 저장 리스트
    for sr in range(2**N):
        for sc in range(2**N):
            if A[sr][sc]:
                cnt = 0     # 주변이 0인 것의 갯수
                for d in range(4):  # 4방향 탐색
                    nr = sr + dr[d]
                    nc = sc + dc[d]
                    if not (0 <= nr < 2**N and 0 <= nc < 2**N):
                        continue
                    # 여기서 시간 많이 걸림.
                    # 주변이 0인 것을 세다 보니 모서리가 안 세졌음..
                    if A[nr][nc]:
                        cnt += 1
                    if cnt >= 3:    # 이 부분을 이상하게 해석..
                        break
                if cnt < 3:    # 3면 이상이 얼음이 아니라면 melt에 담기
                    melt.append((sr, sc))
    # 얼음 녹이기
    for (r, c) in melt:
        A[r][c] -= 1

# 얼음의 칸 세는 함수
def bfs(sr, sc):
    island = 1
    visited[sr][sc] = 1     # 말도 안 되는 실수.. visited[sr][sr]로 써놓고 오랫동안 못 찾음, 이런 실수 하지 말자
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < 2**N and 0 <= nc < 2**N):
                continue
            if A[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                Q.append((nr, nc))
                island += 1
    return island

# 마지막 작업
visited = [[0] * 2**N for _ in range(2**N)]
iceCnt = 0
maxCnt = 0
for i in range(2**N):
    for j in range(2**N):
        iceCnt += A[i][j]
        if A[i][j] and not visited[i][j]:
        #     # bfs 함수 - 얼음 덩어리 칸의 갯수 리턴
            maxCnt = max(maxCnt, bfs(i, j))
print(iceCnt)
print(maxCnt)