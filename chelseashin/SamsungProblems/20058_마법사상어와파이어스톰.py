# from 22:35 to 25:10
# 2h 15m 까지 다 푼 줄 알았지만 이 tc 틀려서 이후 20분 정도 더 디버깅.(2h 35m)
# 회전만 1시간 30분..
# 요새 추세가 진짜 simulation 인 듯. 시뮬레이션에서 시간 잡아먹히지 않도록 많이 풀어보기.
# 뒷 부분은 금방 풀 줄 알았지만 촘촘하게 짜지 않고 대강 구상만 하고 시작하여 잔 실수가 많았음
# 특히 얼음 녹이는 부분을 제대로 이해하지 못해 계속 답이 틀림.
# 문제 꼼꼼하게 읽고 풀기 전에 고려할 부분들 미리 적어놓기
# 각 동작 함수화한 것이 시간, 메모리 단축에 도움

import sys
sys.stdin = open("20058_input.txt")
input = sys.stdin.readline
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def firestorm(A):
    # (0, 0)에서 간격(2**size)만큼이 배열 회전의 시작위치(r, c)가 됨
    new = [[0] * 2**N for _ in range(2**N)]
    gap = 2 ** size
    for r in range(0, 2**N, gap):
        for c in range(0, 2**N, gap):
            for i in range(gap):
                temp = A[r+i][c:c+gap]
                for j in range(gap):
                    new[r+j][c + gap-i-1] = temp[j]
    return new

def melting_ice():
    melt = []  # 얼음 녹는 좌표 저장 리스트
    for sr in range(2**N):
        for sc in range(2**N):
            if A[sr][sc]:
                cnt = 0  # 주변이 0인 것의 갯수
                for d in range(4):  # 4방향 탐색
                    nr = sr + dr[d]
                    nc = sc + dc[d]
                    if not (0 <= nr < 2**N and 0 <= nc < 2**N):
                        continue
                    # 여기서 시간 많이 걸림.
                    # 주변이 0인 것을 세다 보니 모서리가 안 세졌음..
                    if A[nr][nc]:
                        cnt += 1
                    if cnt >= 3:  # 이 부분을 이상하게 해석..
                        break
                if cnt < 3:  # 3면 이상이 얼음이 아니라면 melt에 담기
                    melt.append((sr, sc))
    # 얼음 녹이기
    for (mr, mc) in melt:
        A[mr][mc] -= 1

# main
N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

# 파이어스톰 총 Q번 시전
for size in L:
    # 시전
    A = firestorm(A)
    # 시전 후 얼음 녹이기
    melting_ice()

# 얼음의 칸 세는 함수
def bfs(sr, sc):
    island = 1
    visited[sr][sc] = 1     # 실수 금지
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
            # 얼음 덩어리 칸의 갯수 리턴
            maxCnt = max(maxCnt, bfs(i, j))
print(iceCnt)
print(maxCnt)