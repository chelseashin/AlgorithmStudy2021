# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
# 참고 : https://github.com/byeongjulee222/problems/blob/27261b617192b2163dabb2215d2e33429e0665d5/2105_%EB%94%94%EC%A0%80%ED%8A%B8%EC%B9%B4%ED%8E%98.py#L15

# 10:51 시작
# 12:04 끝
"""
문제

1. 대각선 방향으로 탐색을 해야한다.
2. 길 중 같은번호의 카페가 있으면 안된다.
3. 최대 디저트를 많이 먹을 때의 디저트 수 구하기

풀이

1. back_tracking으로 풀이.
2. cnt개수가 4이면 방향횟수 초과 = return
3. check 배열에 카페를 기록하면서 dfs하는데 같은 카페가 있으면 return
4. 2가지 경우가 있다.
      1. 방향 그대로 갈 수도 있고,
      2. 방향을 바꿀 수 있다. (방향 3번바꾸면 시작위치로 올 수도 있음)


"""
# 좌상, 우상, 좌하, 우하
import sys

sys.stdin= open("2105(디저트카페).txt")

dx = [-1,-1,1,1]
dy = [1,-1,-1,1]


def dfs(x,y,cnt,check):

    global MAX
    if cnt == 4:
        return

    nx ,ny = x + dx[cnt], y + dy[cnt]
    if 0<=nx<N and 0<=ny<N:
        if nx == i and ny == j and MAX <=len(check):
            MAX= len(check)
            if len(check) == 5:
                print(check)
            return

        if array[nx][ny] not in check:
            check.append(array[nx][ny])
            dfs(nx,ny,cnt,check)
            dfs(nx,ny,cnt+1,check)
            check.pop()

        # 같은게 있으면 RETURN


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    # 왼쪽위 대각, 오른쪽 위 대각
    MAX = -1
    for i in range(N):
        for j in range(N):

            dfs(i,j,0,[array[i][j]])

    print('#{0} {1}'.format(tc,MAX))