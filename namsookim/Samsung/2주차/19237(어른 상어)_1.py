# https://www.acmicpc.net/problem/19237

#1. 02:02 시작
#2. 02:31 코딩 시작
#3. 04:02 움직임 구현
#4. 04:40 디버깅 완료
#5. 2시간 38분 소요

"""
시행착오
1. 현재 상어의 방향 잘못 입력 받음(방향 먼저임)



"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 모든 상어의 위치 방향
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 냄새 정보를 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

# 모든 상어를 이동시키는 함수
def move():
    # 이동 결과를 담기 위한 배열
    new_array = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):

            if array[x][y] != 0: # 상어가 있으면
                direction = directions[array[x][y] - 1] # 현재 상어의 방향
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 존재하지 않는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            # 상어 이동시키기 (만약 이미 다른 상어가 있다면 번호가 낮은 것이 들어가도록)
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found: # 냄새 확인할 필요 없음
                    continue
                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == array[x][y]: # 자신의 냄새가 있는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            # 상어 이동시키기
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array

time = 0
while True:
    update_smell() # 냄새 업데이트
    new_array = move() # 모든 상어 이동
    array = new_array # 맵 갱신
    time += 1

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break
