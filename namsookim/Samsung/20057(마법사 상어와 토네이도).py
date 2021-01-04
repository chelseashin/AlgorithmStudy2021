# 오후 8:35 시작
# 오후 8:47 아이디어 정리 끝
# 오후 10:42 끝

# 2시간 7분 소요

"""
1. round 내장함수를 잘못 썼음. round 함수는 반올림 시켜주는 함수. round - > int로 변경
2. spread 함수에서 실수. 먼저 기능확인하고 진행하기.
"""
N = int(input())
array = [list(map(int,input().split())) for _ in range(N)]
answer = 0

dx = [0,1,0,-1] #왼쪽, 아래, 오른쪽, 위쪽
dy = [-1,0,1,0]

def side_direction(dir): # 양쪽 방향 구하는 함수

    if dir == 0:
        return dir+1, 3
    elif dir == 3:
        return 0, dir-1
    else:
        return dir+1, dir-1

def solve():
    x = N//2
    y = N//2
    length = 1
    while True:
        for i in range(4):
            if i==2:
                length +=1
            for _ in range(length):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if array[next_x][next_y] != 0: # 다음 가야할 위치에 값이 0이 아니면 뿌려주기
                    spread(x, y, next_x, next_y, i)
                x = next_x
                y = next_y
                if x == 0 and y == 0:
                    return 
        length +=1 # 실수했음

    
def spread(pos_x,pos_y,next_x,next_y,dir):
    global answer
    total_spread = 0 # 알파 위치에 넣어주기 위해서 이동한 값들을 저장

    # 양쪽 방향 구하기
    side_dir = side_direction(dir)

    sand = array[next_x][next_y]

    array[next_x][next_y] = 0
    alpha_x = next_x + dx[dir]
    alpha_y = next_y + dy[dir]

    for direct in side_dir:

        # 1% 처리
        nx = pos_x+dx[direct]
        ny = pos_y+dy[direct]
        if 0<=nx<N and 0<=ny<N:
            array[nx][ny] += int(sand*0.01)
        else:
            answer += int(sand*0.01)

        total_spread += int(sand * 0.01)

        # 7% 처리
        nnx = next_x+dx[direct]
        nny = next_y+dy[direct]

        if 0<=nnx<N and 0<=nny<N:
            array[nnx][nny] += int(sand*0.07)
        else:
            answer += int(sand*0.07)

        total_spread += int(sand * 0.07)

        # 2% 처리
        n2x = nnx + dx[direct]
        n2y = nny + dy[direct]
        if 0<=n2x<N and 0<=n2y<N:
            array[n2x][n2y] += int(sand*0.02)
        else:
            answer += int(sand*0.02)
        total_spread += int(sand * 0.02)

        # 10% 처리
        n10_x = alpha_x + dx[direct]
        n10_y = alpha_y + dy[direct]

        if 0<=n10_x<N and 0<=n10_y<N:
            array[n10_x][n10_y] += int(sand*0.1)
        else:
            answer += int(sand*0.1)

        total_spread += int(sand*0.1)

    # 5% 처리
    n5_x = alpha_x + dx[dir]
    n5_y = alpha_y + dy[dir]

    if 0<=n5_x<N and 0<=n5_y<N:
        array[n5_x][n5_y] += int(sand*0.05)
    else:
        answer += int(sand*0.05)

    total_spread += int(sand*0.05)

    # 알파처리
    if 0<=alpha_x<N and 0<=alpha_y<N:
        array[alpha_x][alpha_y] += (sand - total_spread)  # += 안하고 = 해서 틀렸음
    else:
        answer += (sand - total_spread)

solve()
print(answer)

