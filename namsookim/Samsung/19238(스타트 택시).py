# https://www.acmicpc.net/problem/19238

# 4시간 10분 소요

"""
문제

1. 택시에 승객을 태운 뒤 목적지까지 이동하면서 기름 양이 변한다.
2. 택시를 기준으로 가장 거리가 가까운 승객을 태운다. (단, 거리가 가까운 승객이 2명 이상일 경우 행과 열이 낮은 곳을 선택한다)
3. 이동 도중 연료가 음수가 되면 종료(-1)되고, 승객을 태우고 목적지까지 무사히 이동시켰을 때 이동거리에 2배를 연료에 더한다.
4. 최종적으로 남은 연료의 양은?

시행착오

1. 종료시점 잘못 설정
  -> 승객을 태우고 나면 승객배열을 -1로 변경, 도착하면 도착정보가 담긴 배열을 -1로 변경해주었는데, 승객을 기준으로 모두 -1이 되었을 때 종료하도록 코드를 작성.
     종료시점은 승객이 모두 탑승했을 때가 아닌, 모두 도착했을 때이다.

2. 도착지점까지 거리 반환 실수
  -> move_table 배열에 (현재 택시 좌표 -> 가고자 하는 위치의 최소거리) 를 저장하였는데, 갈 수 없는 위치는 -1로 저장하였다.
    하지만 이 정보가 들어있는 move_table 배열을 사용하지 않고 tourlist 배열과 목적지 배열을 참조함.
    그래서 도착지점까지 가지 못하는 경우도 갈 수 있다고 처리되었음.
"""
from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

N,M,oil = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]
taxi_x, taxi_y = map(int,input().split())

# 택시 현재 위치
taxi_x -= 1
taxi_y -= 1

INF = int(1e9)

passenger = [0 for i in range(M)] # 승객
destination = [0 for i in range(M)] # 목적지

for i in range(M):
    tx,ty,dest_x ,dest_y = map(int,input().split())
    passenger[i] = (tx-1,ty-1)
    destination[i] = (dest_x-1,dest_y-1)

# 거리
move_table = [0 for _ in range(M)]

def bfs(x,y,li): # 승객 최소 거리 찾기 or 목적지 최소 거리 찾기

    check = [[False] * N for _ in range(N)]
    new_array = [[-1] * N for _ in range(N)] # 최소 거리 정보
    q = deque([(x,y,0)])
    check[x][y] = True
    new_array[x][y] = 0

    while q:
        x,y,dist=q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if check[nx][ny] != True and array[nx][ny] == 0:

                    new_array[nx][ny] = dist + 1
                    check[nx][ny] = True
                    q.append((nx,ny,dist+1))

    for i in range(len(li)):
        if li[i] == -1: # 이미 처리된 것
            move_table[i] = -1
            continue

        move_table[i]= new_array[li[i][0]][li[i][1]] # 최소 거리 저장

def taxi_move(x,y,dist,oil):

    oil -= dist
    if oil<0:
        return -1
    else:
        return oil

def shortest_find(li,move_table):
    px, py = N,N
    shorest_value = INF
    index = N
    for i in range(len(li)):
        if li[i] == -1 or move_table[i] == -1: # 이거 안해줘서 틀림, 거리가 -1이면 못감
            continue
        x,y = li[i][0], li[i][1]
        if shorest_value > move_table[i]:
            px , py = x,y
            shorest_value = move_table[i]
            index = i

        elif shorest_value == move_table[i]:
            if px> x:
                px, py = x,y
                shorest_value = move_table[i]
                index = i

            elif px == x:
                if py > y:
                    px,py = x,y
                    shorest_value = move_table[i]
                    index = i

    if shorest_value == INF: # 이동할 수 있는 승객이 없으면
        return -1
    else:
        li[index] = -1 # 가장 가까운 위치 -1로 태깅해 사용 못하도록
        return px,py,shorest_value, index

def taxi_move_destination(x,y,dist,oil):

    oil -= dist
    if oil < 0:
        return -1
    else:
        oil += 2*dist
        return oil

def finish(destination):

    for i in range(len(destination)):
        if destination[i] != -1:
            return False
    return True

def fail_to_land(check,tourlist):

    for tour in tourlist:
        if tour == -1:
            continue
        else:
            if check[tour[0]][tour[1]] == False:
                return True
    return False

def solve():

    global oil
    global taxi_x, taxi_y

    for _ in range(M):
        bfs(taxi_x,taxi_y,passenger) # 현재 택시 기준으로 최소거리 승객 위치 테이블 갱신
        find= shortest_find(passenger,move_table) # 최소 거리 승객 위치 반환

        if find == -1: # 이동할 수 있는 승객이 없으면
            return -1
        taxi_x, taxi_y, dist, index = find[0], find[1], find[2], find[3]
        oil=taxi_move(taxi_x,taxi_y,dist,oil) # 택시 이동

        if oil == -1: # 기름 0보다 작으면 -1 반환.
            return -1

        # 승객 태우고 목적지까지 이동 #
        else:

            bfs(taxi_x,taxi_y,destination) # 현재 택시 기준으로 목적지 까지 거리 세팅
            dist=move_table[index] # 목적지까지 거리 , 목적지 까지 갈 수 없으면 -1 반환
            if dist == -1:
                return -1

            taxi_x,taxi_y = destination[index] # 택시 위치 이동
            oil=taxi_move_destination(taxi_x, taxi_y,dist,oil)

            if oil == -1: # 기름이 음수가 되면 -1 반환
                return -1

            destination[index] = -1 # 목적지 까지 이동했으면 테이블 -1로 갱신

    if finish(destination): # 모든 목적지 탐색했으면 현재 기름양 반환
        return oil
    else: # 모든 목적지를 탐색 못했으면 -1 반환
        return -1


print(solve())

"""

틀린 케이스 

3 1 100
0 1 0
0 1 0
0 1 0
1 1
1 3 3 3

1 1 에서 1 3으로 못가는데 종료 안해줌
 
"""
