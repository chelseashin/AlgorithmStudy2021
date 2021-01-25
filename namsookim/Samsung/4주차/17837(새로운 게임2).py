# https://www.acmicpc.net/problem/17837
# 11:32 시작
# 13:42 종료
# 2시간 10분 소요
"""
문제
1. 체크판의 칸은 흰색(0), 빨간색(1), 파란색(2) 중 하나
2. 말은 1번부터 k번까지 있음.
3. 1번 말 부터 시작~ k번 말 까지
4. 흰색인 경우
   - 위에 있는 말들과 함께 전부 이동

   빨간색인 경우
   - 위에 있는 말들이 역순으로 이동

   파란색 또는 경계를 넘을 경우
   - 방향 반대로 바꾼 뒤 이동
   - 파란색 또는 경계인경우는 이동x

풀이
1. 색 정보를 나타내는 판 : color_board
   말들이 쌓여있는 판 : hores_board
   말들의 현재 좌표값과 방향 정보: position

2. 문제의 요구사항 대로 그대로 품

"""

N, K = map(int,input().split())
color_board = [list(map(int,input().split())) for _ in range(N)] # 0: 흰색, 1:빨간색, 2: 파란색
hores_board = [[[] for _ in range(N)] for _ in range(N)] # (말의 숫자,방향)
position = [0]*(K+1)

for number in range(K):
    r,c,direction = map(int,input().split())
    hores_board[r-1][c-1].append(number+1)
    position[number+1] = (r-1,c-1,direction-1) # x,y좌표, 방향

def reverse_direction(dir):

    if dir == 1 or dir == 3:
        ndir = dir - 1
    else:
        ndir = dir + 1

    return ndir

def print_array(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=' ')
        print()

def move_hores(n,color_board,hores_board):
    global position # 말의 위치(x,y),방향(direction)
    ismove = False # 말이 이동 했는지 체크

    dx = [0, 0, -1, 1] # 오른쪽, 왼쪽, 위, 아래
    dy = [1, -1, 0, 0]

    x,y,dir = position[n]


    temp = hores_board[x][y]

    # 말의 인덱스 찾고 업혀있는 애들 다 가져옴
    start=temp.index(n)
    temp_list=temp[start:]

    # 현재 방향정보를 기준으로 이동
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx<0 or ny<0 or nx>=N or ny>=N: # 경계를 벗어남
        ndir = reverse_direction(dir) # 방향 반대

        ox = x + dx[ndir]
        oy = y + dy[ndir]

        if 0<=ox<N and 0<=oy<N:
            if color_board[ox][oy] == 2:  # 또 파란색이면
                # 방향정보만 바꾸고 이동x
                position[n] = x,y,ndir

            elif color_board[ox][oy] == 1:  # 빨간색이면

                while temp_list:
                    t = temp_list.pop()

                    _, _, d = position[t]
                    position[t] = ox, oy, d # 업혀있는 말들 새로운 위치로 갱신

                    hores_board[x][y].remove(t) # 이전 위치의 말 제거
                    hores_board[ox][oy].append(t) # 새로운 위치로 이동

                ismove = True
                position[n] = ox, oy, ndir

            else:  # 흰색이면

                for t in temp_list:
                    _, _, d = position[t]
                    position[t] = ox, oy, d # 업힌애들 위치 갱신
                    hores_board[x][y].remove(t)
                    hores_board[ox][oy].append(t)

                ismove = True
                position[n] = ox, oy, ndir # 새로운위치, 새로운 방향(기존의 반대방향)으로 갱신

        else: # 범위 벗어나면
            position[n] = x,y,ndir # 방향정보만 업데이트

    else: # 범위 안에 들면
        if color_board[nx][ny] == 1: # 빨간색
            while temp_list:
                t = temp_list.pop()
                _, _, d = position[t]

                position[t] = nx, ny, d
                hores_board[x][y].remove(t)
                hores_board[nx][ny].append(t)

            ismove = True
            position[n] = nx, ny, dir


        elif color_board[nx][ny] == 2: # 파란색
            ndir=reverse_direction(dir)
            bx = x + dx[ndir]
            by = y + dy[ndir]
            if bx<0 or by<0 or bx>=N or by>=N: # 범위를 벗어나면
                position[n] = x,y,ndir # 방향정보만 바꾸고 이동x

            else: # 범위 안에 들면
                if color_board[bx][by] == 2: # 또 파란색이면

                    position[n] = x, y, ndir # 방향정보만 바꾸고 이동x

                elif color_board[bx][by] == 1: # 빨간색이면

                    while temp_list:
                        t=temp_list.pop()

                        _, _, d = position[t]
                        position[t] = bx, by, d

                        hores_board[x][y].remove(t)
                        hores_board[bx][by].append(t)

                    ismove = True
                    position[n] = bx, by, ndir

                else: # 흰색이면
                    for t in temp_list:
                        _, _, d = position[t]
                        position[t] = bx, by, d
                        hores_board[x][y].remove(t)
                        hores_board[bx][by].append(t)

                    ismove = True
                    position[n] = bx, by, ndir

        else: # 흰색이면
            for t in temp_list:
                _, _, d =position[t]
                position[t] = nx,ny,d
                hores_board[x][y].remove(t)
                hores_board[nx][ny].append(t)

            ismove = True
            position[n] = nx, ny, dir

    return ismove # 말 이동했으면 True , 안했으면 False


def check_horse(hores_board):

    for i in range(len(hores_board)):
        for j in range(len(hores_board[0])):
            if len(hores_board[i][j]) >=4:
                return True
    return False

def solve():

    answer = 0
    while True:
        tag = False # 말이 이동했는지를 체크
        answer += 1
        for n in range(1,K+1): # 1번 말부터 K번 말까지 이동
            ismove= move_hores(n,color_board, hores_board) # 이동 있었으면 tag = True로 변화주기

            if ismove == True:
                tag = True

            if check_horse(hores_board):
                return answer

        if answer>1000 or tag == False: # 전혀 이동변화가 없으면
            answer = -1
            return answer


print(solve())