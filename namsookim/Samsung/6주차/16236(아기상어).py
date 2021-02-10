from collections import deque

# https://www.acmicpc.net/problem/16236
# 9:35 시작
# 11:51 끝
# 2시간 16분 소요

"""
풀이
while True:
    # 물고기 0개 또는 잡을 수 있는 물고기 없으면 종료
    # 첫 번째 물고기부터 마지막 물고기까지 탐색.(거리 작으면 갱신) 
    # 물고기 잡고 상어위치, 상어크기, 물고기 삭제, 현재 먹은 개수 갱신

시행착오
1. 처음에 bfs해서 첫번째 물고기 만나면(크기가 최소이니) 그 물고기를 잡아먹는 것으로 구현// 위,왼쪽,오른쪽,아래 순으로 방향설정해서
   문제 없을것이라 생각.

2. 반례
   0 9 0 1
   1 0 0 0
   0 0 0 0
   0 0 0 0 
   문제 요구사항대로 하면 오른쪽 위를 먹어야 되지만, 왼쪽 아래 물고기를 먹음. // 해결하다가 잘 안되서 방법 바꿈

"""
dx = [-1, 0, 0, 1]  # 위,왼,오른,아래 순
dy = [0, -1, 1, 0]

N = int(input())
shark = []  # 상어 위치
array = []
fish = []  # 물고기 위치
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 9:
            shark.extend([i, j, 2])
        if 1 <= temp[j] < 9:
            fish.append((i, j))
    array.append(temp)


# 아기상어가 자신의 크기와 같은 수 물고기 먹으면 크기 +1 증가. (현재 먹은 양 기록)
def bfs():
    global shark
    global array
    C = len(array[0])
    R = len(array)
    distance = [[-1] * C for _ in range(R)]
    q = deque([(shark[0], shark[1])])  # 상어 위치기준 거리 탐색
    distance[shark[0]][shark[1]] = 0
    size = shark[2]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if array[nx][ny] > size or distance[nx][ny] != -1:  # 현재 상어보다 크거나 이미 방문했으면
                    continue
                else:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

    return distance


INF = int(1e9)

# 몇초동안 지속되는지 출력. 먹을 물고기 없을떄까지 지속
def solve():
    answer = 0
    global shark
    global array
    global fish
    eat_fish = 0  # 현재 먹은양 기록
    while True:
        if len(fish) == 0:
            break

        distance = bfs()
        shark_x, shark_y = shark[0], shark[1]
        shark_size = shark[2]

        x, y = -1, -1 # 물고기 위치 담기
        time = INF # 물고기 잡아먹으러 가는 시간
        for fx, fy in fish:  #(물고기는 왼쪽 위 순으로 넣었음)
            if array[fx][fy] < shark_size:
                dis = distance[fx][fy]
                if dis == -1: # 갈 수 없으면
                    continue

                if dis < time:
                    x, y = fx, fy
                    time = dis

        if time != INF: # 잡아먹을 물고기가 있으면

            array[shark_x][shark_y] = 0  # 상어 이동
            shark[0], shark[1] = x, y
            answer += time  # 시간 증가
            eat_fish += 1  # 물고기 한마리 먹었으니 증가

            array[shark[0]][shark[1]] = 9  # 물고기 위치에 상어 위치함
            fish.remove((x, y)) # 물고기 제거

            if eat_fish == shark[2]:  # 상어 크기와 같으면
                shark[2] += 1
                eat_fish = 0
        else:
            break
    return answer

print(solve())
