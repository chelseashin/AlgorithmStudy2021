# https://www.acmicpc.net/problem/1520
# https://dirmathfl.tistory.com/204 참고
# 1시간 38분(의미없음. 참고함)
"""
문제
1. 더 낮은 지점으로 이동해가면서 n-1,m-1까지 갈 수 있는 경우의수를 구하여라.

풀이
1. 재귀 호출로 방문 가능한 경로의 수를 반환하면서, 한번 탐색한 곳은 탐색하지 않게 처리.

시행착오
1. 처음에 dp 배열에 값을 저장하면서 갈수 있는지 체크하려고 했는데 위에서 아래로 올라오는 내리막길이 있어서
   문제해결 방법 떠올리기 어려웠음.

"""
N,M = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
check = [[-1]*M for _ in range(N)]

def dfs(x,y):
    # 탈출조건
    if x == N-1 and y == M-1:
        return 1
    if check[x][y] != -1: # 방문 처리된 적이 있으면
        return check[x][y]

    # 방문한 적이 없으면
    check[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if array[x][y] > array[nx][ny]:
                check[x][y] += dfs(nx,ny) # 4방향 탐색하면서 가능한 경로 더해줌
    return check[x][y]

def solve():
    print(dfs(0,0))

solve()