# from 12:30 to 14:27
# 1h 57m
# bfs를 여러 번 사용해야 하는 문제
# 문제를 풀기 전에 어떤 부분에 어떤 자료구조, 알고리즘을 어떤 용도로 쓸지 정하고 시작해야 코드를 치며 흔들리지 않는다.
# 태울 승객을 고를 때 현 위치에서 최단 거리가 가장 짧은 승객, 같다면 행 작은 순, 같다면 열 작은 순
# heapq 사용해야 함. 우선순위 큐를 만들어 중요도 순으로 넣어줌
# 이전에 풀었던 문제라 이번에는 시간, 메모리 효율을 좀더 고려하고 코드를 깔끔하게 짜려고 노력
# 승객 고르는 부분과 택시 이동 부분을 함수로 만들어 원하는 답이 나오면 바로 리턴하는 방식

import sys
sys.stdin = open("19238_input.txt")
input = sys.stdin.readline
from collections import deque
import heapq

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 태울 승객 고르기
def bfs(sr, sc):
    visited = [[-1] * N for _ in range(N)]
    for wr, wc in info.keys():
        if (wr, wc) == (sr, sc):    # 현 위치에 탑승을 기다리는 다른 승객이 있다면
            return (0, sr, sc)      # 승객까지의 거리 (0, 현 위치) 리턴
        visited[wr][wc] = 999       # 탑승 기다리는 승객 위치 표시
    visited[sr][sc] = 0
    Q = deque([(sr, sc)])
    priority = []
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc]:
                continue
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
            elif visited[nr][nc] == 999:
                heapq.heappush(priority, (visited[r][c]+1, nr, nc))      # 거리 > 행 > 열
    if priority:
        # return heapq.heappop(priority)
        return priority[0]      # 먼저 태울 승객까지의 거리, 승객의 위치 리턴
    return False

# 승객 택시로 이동
def taxi_move(sr, sc):
    visited = [[-1] * N for _ in range(N)]
    visited[sr][sc] = 0
    gr, gc = info[(sr, sc)]
    visited[gr][gc] = 999
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N) or A[nr][nc]:
                continue
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
            elif visited[nr][nc] == 999:
                return visited[r][c] + 1    # 목적지까지의 거리 리턴
    return False

def solve():
    global fuel, br, bc
    cnt = 0
    while fuel:
        if cnt == M:  # 태운 승객 수가 M명 이면 탈출
            return fuel
        # 태울 승객을 고르기
        available = bfs(br, bc)
        if available:  # 승객까지의 거리, 태운 위치 리턴
            dis, pr, pc = available
            if dis <= fuel:  # 태우기까지 거리가 보유한 연료보다 작거나 같으면 태울 수 있음
                fuel -= dis
                temp = taxi_move(pr, pc)    # 택시 타고 이동한 거리 리턴
                if temp and temp <= fuel:
                    fuel += temp    # 이동한 만큼 연료 빼고, 이동 완료하면 *2 만큼 연료 충전(즉, temp 만큼 충전됨)
                    br, bc = info[(pr, pc)]     # 백준 승객의 목적지로 위치 이동
                    del info[(pr, pc)]          # 승객 정보 삭제
                    cnt += 1                    # 태운 승객 수 + 1
                else: return -1     # 이동 불가능한 곳이라면
            else: return -1         # 태우러 가다가 연료 떨어짐
        else: return -1             # 태울 고객 못 찾으면

# main
N, M, fuel = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
br, bc = map(int, input().split())
br -= 1
bc -= 1
info = dict()       # 승객 현황 관리
for _ in range(M):
    sr, sc, gr, gc = map(int, input().split())
    info[(sr-1, sc-1)] = (gr-1, gc-1)
print(solve())