# https://www.acmicpc.net/problem/16234
# 인구 이동

# # 1시간 26분 소요


"""
풀이
1. bfs 돌릴 때, 연합 이동이 가능하면 연합 국가 수, 연합의 인구수 구한 뒤 바로 처리
2. 종료 조건: index = n*n 일때. -> 연합수가 n*n이면 서로 이동할 수 없다는 뜻

"""

from collections import deque

# 땅의 크기(N), L, R 값을 입력받기


# 전체 나라의 정보(N x N)를 입력 받기
graph = []


N, L, R = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(N):

    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def bfs(x, y, index,union):


    united = [] # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트

    united = [] # 연합 정보를 담는 리스트(좌표값)

    united.append((x, y))

    q= deque([(x, y)])
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수

    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여

            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:

                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count

def solve():
    total_count = 0
    # 더 이상 인구 이동을 할 수 없을 때까지 반복
    while True:

        union = [[-1] * n for _ in range(n)]
        index = 0
        for i in range(n):
            for j in range(n):

        union = [[-1] * N for _ in range(N)]
        index = 0
        for i in range(N):
            for j in range(N):

                if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                    bfs(i, j, index,union)
                    index += 1
        # 모든 인구 이동이 끝난 경우

        if index == N * N:

            break
        total_count += 1

# 인구 이동 횟수 출력
    print(total_count)
solve()