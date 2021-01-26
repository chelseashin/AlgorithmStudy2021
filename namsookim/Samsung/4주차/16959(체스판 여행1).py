# https://www.acmicpc.net/problem/16959
# 참고 : https://github.com/injae-kim/injae-kim.github.io/blob/219b008e0f4ebaaa709d00171c94bc0c9d082597/_posts/2020-03-06-baekjoon-16959.markdown

# 2시간 14분 (의미없음 해설 참고함)

"""
처음에 모든 경우의 수를 탐색해야 되는 문제라고 생각해서 dfs 문제인 줄 알았다. 접근 방법을 모르겠어서 풀이방법을 이해한 뒤 코딩하였다.

문제
1. 1에서 출발하여 나이트, 비숍, 룩 중 하나의 말을 이동시켜 2,3,..., N^2 -1 방문한 뒤 N^2까지 도착하는데까지 걸리는 최소시간 구하는 문제
2. 1초동안 할 수 있는 일
    - 말 이동시키기
    - 말 교체하기

풀이
1. bfs를 통해 최소 거리를 구해준다.
2. 말, 비숍, 룩이 갈 수 있는 위치 좌표를 구한 뒤, 갈 수 있는 곳을 모두 queue에 넣어줘서 bfs.

1. check[x][y][next][kind] 배열이 핵심.
2. next가 있는 이유
   = 룩의 경우 next가 없으면, 좌우로 방문했던 곳을 왔다갔다 할 수 있음.
"""

from collections import deque

N = int(input())
array = [list(map(int,input().split())) for _ in range(N)]

night_x = [-2,-2,-1,-1,1,2,1,2] # 8가지
night_y = [-1,1,-2,2,-2,-1,2,1]

bishop_x = [-1,-1,1,1] # 대각선
bishop_y = [-1,1,1,-1]

look_x = [0,0,1,-1] # 상하좌우
look_y = [1,-1,0,0]

def bfs(x,y):

    check = [[[[False] * 3 for _ in range(N*N+2)] for _ in range(101)] for _ in range(101)] # x,y,next,kind

    q=deque([])

    q.append((x,y,0,2,0)) # x,y,cnt,next,kind
    q.append((x,y,0,2,1))
    q.append((x,y,0,2,2))

    while q:
        x,y,cnt,next,kind=q.popleft()
        # 종료조건
        if next == N*N + 1: # 해당 위치를 찾으면 next+1을 해주어 큐에 넣기 때문에
            return cnt

        # 방문처리
        check[x][y][next][kind] = True

        # 말 바꾸기
        for k in range(3):
            if kind == k:
                continue
            if check[x][y][next][k] == True:
                continue
            q.append((x,y,cnt+1,next,k)) # 종류 바꾸기

        # 나이트
        if kind == 0:
            for i in range(8): # 방향 8가지
                nx = x + night_x[i]
                ny = y + night_y[i]
                if nx<0 or nx>=N or ny<0 or ny>=N: # 범위 넘으면
                    continue

                if check[nx][ny][next][kind] != True:
                    #print(nx,ny)
                    if array[nx][ny] == next:
                        q.append((nx,ny,cnt+1,next+1,kind))
                        check[nx][ny][next+1][kind] = True
                    else:
                        q.append((nx, ny, cnt + 1, next, kind))
                        check[nx][ny][next][kind] = True

        elif kind == 1:
            for i in range(4): # 4가지 방향으로
                for dist in range(1,N+1):

                    nx = x + (bishop_x[i]*dist)
                    ny = y + (bishop_y[i]*dist)
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위 넘으면
                        break

                    if check[nx][ny][next][kind] != True:
                        if array[nx][ny] == next:
                            q.append((nx, ny, cnt + 1, next + 1, kind))
                            check[nx][ny][next + 1][kind] = True
                        else:
                            q.append((nx, ny, cnt + 1, next, kind))
                            check[nx][ny][next][kind] = True


        elif kind == 2:
            for i in range(4):  # 4가지 방향으로
                for dist in range(1, N + 1):
                    nx = x + (look_x[i] * dist)
                    ny = y + (look_y[i] * dist)

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위 넘으면
                        continue

                    if check[nx][ny][next][kind] != True:
                        if array[nx][ny] == next:
                            q.append((nx, ny, cnt + 1, next + 1, kind))
                            check[nx][ny][next + 1][kind] = True
                        else:
                            q.append((nx, ny, cnt + 1, next, kind))
                            check[nx][ny][next][kind] = True

def solve():
    x,y = -1,-1
    for i in range(N):
        for j in range(N):
            if array[i][j] == 1:
                x,y = i,j
                break

    print(bfs(x,y)) # 현재 1인 위치에서 bfs 시작

solve()
