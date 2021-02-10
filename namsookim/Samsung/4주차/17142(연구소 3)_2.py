import sys
from itertools import combinations
from collections import  deque
# https://www.acmicpc.net/problem/17142

# 14:36 시작
# 16:01 디버깅
# 16:37 끝

# 2:01 소요

"""
문제
1. 바이러스는 활성, 비활성 상태가 있음
2. 처음 바이러스는 모두 비활성
3. 활성상태의 바이러스는 상하좌우로 인접한 빈칸으로 동시에 복제 . 1초 소요
4. M개를 활성 상태로 변경하려고 함.
5. 모든 빈 칸에 바이러스 퍼트리는 시간의 최소값은?
6. 모든 빈칸 처리 못하면 -1 

풀이
1. 내장함수 combinations 사용해서 경우의 수를 구함
2. 활성화 바이러스에서 bfs를 통해 최소 거리 찾음.(바뀜)
3. bfs를 통해 구한 최대 시간을 반환한 뒤, 현재까지의 최솟값과 비교(바뀜)
4. 모든 경우의 수를 따졌는데 빈칸에 바이러스 못 퍼뜨리면 -1 반환 (바뀜)

시행착오
1. 비활성화된 바이러스를 통과하지 못한다고 구현했음.

스터디 후기

바뀐 부분
1. 맵, bfs 부분 바로 처리. (따로 하지 않고 한번에) (시간효율 up)
2. 빈칸 개수를 초기에 찾아내서 변수에 저장. total_blank
3. check= [[-1]*N for _ in range(N)] 으로 해서 활성부분만 0으로 바꿈. 이것으로 거리 구함
4. cnt가 total_blank가 되었을 때 바로 값 return 이때가 최고 시간 값임.

"""

# 0은 빈칸, 1은 벽, 2는 바이러스

input = sys.stdin.readline
INF = int(1e9)
N, M = map(int,input().split())
virus = []
total_blank = 0
array = [list(map(int,input().split())) for _ in range(N)]
for i in range(len(array)):
    for j in range(len(array[0])):

        if array[i][j] == 2:
            virus.append((i,j)) # 0은 이동거리값(bfs에서 활용)
        elif array[i][j] == 0:
            total_blank += 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(virus,array):
    global total_blank

    cnt = 0

    check = [[-1]*N for _ in range(N)]
    for vx, vy in virus:
        check[vx][vy] = 0

    q=deque(list(virus))

    while q:
        vx,vy=q.popleft()

        for i in range(4):
            nx = vx+dx[i]
            ny = vy+dy[i]
            if 0<=nx<N and 0<=ny<N: # 범위 안에 들고
                if check[nx][ny] == -1 and (array[nx][ny] == 0 or array[nx][ny] == 2): # 바이러스도 건너뛸 수 있음. 이거 처리 못했음.

                    if array[nx][ny] == 0:
                        cnt += 1

                    check[nx][ny] = check[vx][vy] +1
                    if cnt == total_blank:
                        return check[nx][ny]

                    q.append((nx,ny))

    return INF

def solve():
    global total_blank

    answer = INF
    virus_combi=list(combinations(virus,M)) # 전체 비활성 바이러스 중 M개를 선택하는 경우의 수
    if total_blank == 0:
        return 0

    for active_virus in virus_combi:

        min_time = bfs(active_virus, array)
        answer = min(min_time,answer)

    if answer == INF:
        return -1
    else:
        return answer

print(solve())
