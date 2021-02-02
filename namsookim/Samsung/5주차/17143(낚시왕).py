# https://www.acmicpc.net/problem/17143

# 1시간 37분 소요
"""
문제
낚시왕이 가장 오른쪽 열의 오른쪽
1. 낚시왕이 오른쪽으로 한칸 이동함
2. 낚시왕이 있는 열에서 가장 가까운 상어를 잡고 총합 증가시킴/ 상어는 사라짐
3. 상어 이동

풀이
1. 문제 요구사항대로 그대로 구현

시행착오
1. 상어가 벽에 부딪혔을 때 수학적으로 계산하려고 했는데 잘 안됨.
2. 해보다가 시간복잡도 계산해봤는데 반복문으로도 통과할 수 있을 거 같아서 그냥 반복문으로 풀었음

"""
R,C,M = map(int,input().split())
board = [[0]*C for _ in range(R)]
shark_info = {}
for _ in range(M):
    r,c,s,d,z = map(int,input().split()) # r,c 위치 , # s 속력, d 이동방향, z 크기
    board[r-1][c-1] = (s,d,z)
    shark_info.setdefault((r-1,c-1),(s,d-1,z)) # 상어 정보 딕셔너리에 저장

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def shark_move(shark_info): # 상어 이동

    new_board= [[0]*C for _ in range(R)]
    new_shark_info = {} # 새로운 상어 정보
    reverse = [1, 0, 3, 2] # 반대방향

    for rc,sdz in shark_info.items(): # 각 상어들 이동

        shark_x = rc[0]
        shark_y = rc[1]
        shark_speed = sdz[0]
        shark_dir = sdz[1]
        shark_size = sdz[2]

        # 새로운 상어 위치, 방향 정보
        next_x = shark_x
        next_y = shark_y
        new_dir = shark_dir
        pos_speed = shark_speed # 현재 몇 칸 더 이동할 수 있는지

        while pos_speed>0: # 움직일 수 없을 때까지
            next_x = shark_x + dx[new_dir]
            next_y = shark_y + dy[new_dir]

            if next_x<0 or next_y<0 or next_x>=R or next_y>=C: # # 부딪히면 방향 반대
                new_dir = reverse[new_dir]
                next_x = shark_x + dx[new_dir]
                next_y = shark_y + dy[new_dir]

            shark_x, shark_y =next_x, next_y # 상어 위치 갱신
            pos_speed -= 1

        shark = new_shark_info.get((next_x,next_y))
        if shark == None: # 새로운 위치에 상어 없으면
            new_shark_info.setdefault((next_x,next_y),(shark_speed,new_dir,shark_size))
        else: # 상어 있으면
            if shark[2]< shark_size: #새로운 상어가 더 크면
                new_shark_info[(next_x,next_y)] = (shark_speed,new_dir,shark_size)

    for rc,sdz in new_shark_info.items():
        new_board[rc[0]][rc[1]] = (sdz[0],sdz[1],sdz[2])

    return new_board, new_shark_info


def solve(board,shark_info):
    answer = 0 # 상어 총 합
    for man in range(C): # 낚시왕 이동
        # 가장 가까운 상어 잡음
        for x in range(R):
            if board[x][man]!=0: # 상어가 있으면
                answer += board[x][man][2] # 총합 증가
                board[x][man] = 0
                shark_info.pop((x,man)) # 상어 위치를 삭제
                break

        board, shark_info = shark_move(shark_info) # 상어 이동

    return answer

print(solve(board,shark_info))