# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf
# http://colorscripter.com/s/vvHvBFX
"""
1716번
# 18:51 시작
# 22:06 끝(시간초과)
# 22:52 끝(
# 4시간 소요
"""

# 풀이
"""
1. 선은 4가지 방향중 한 방향으로 이을 수 있다.
2. 이은 선이랑 교차하거나 코어랑 부딪히면 안된다.
3. 전원이 연결되지 않은 코어가 있을 수 있음.
4. 백트래킹을 통해 모든 경우의 수를 확인해가면서 가장 코어가 많을 때 가장 적은 선의 길이를 출력

주의
1. 출력해야 하는 것은 코어가 가장 많을 때의 최소 선의 길이! (코어가 무조건 많은게 우선순위)
2. 모두 연결 안될수도 있음
3. 연결하지 않거나, 4가지 중 하나로 연결하거나 총 5가지 경우의 수가 있음.


시간초과
1. copy.deepcopy 지양하기 -> draw_line() 함수로 해결
2. 커팅 방법
   1. if core_cnt + len(core)-k < max_core: # 커팅해서 시간초과 해결
   2. board에 직접 그리지 말고, 양끝점을 기억해서 선분 교차 판정(수직, 수평 밖에 없으니)으로 possible 체크하기.

"""

"""
def backtrack(k):  # 함수 호출의 depth, 지금 고려할 코어의 번호
    if k == N:
        # 연결된 개수가 이전의 것보다 많으면
        #     코어개수, 길이 저장
        return
    else:
        # k번을 연결하는 경우
        for i in range(4):
            # 상, 하, 좌, 우 중에 한 방향으로 연결
            backtrack(k + 1)
        # k번을 연결하지 않는 경우
        backtrack(k + 1)

"""

import sys
max_core = 0
INF = int(1e9)
min_length = INF

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def possible(k,i): # 선을 이을 수 있는지 체크
    x,y =core[k]
    tag = False
    while True:
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <0 or nx >=N or ny<0 or ny>=N:
            tag = True
            break
        if board[nx][ny] != 0:
            break
        x = nx
        y = ny

    if tag :
        return True
    else:
        return False

def draw_line(k,i,num): # 선 연결하기
    x, y = core[k]
    line = 0
    while True:
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            break
        board[nx][ny] = num
        line += 1
        x = nx
        y = ny

    return line



def back_tracking(k,length,core_cnt): # 현재 코어, 길이, 현재 코어 개수
    global max_core, min_length

    if core_cnt + len(core)-k < max_core: # 커팅해서 시간초과 해결
       return

    if k == len(core):
        if max_core < core_cnt: # 코어개수가 많은 것보다 크면 갱신
            max_core = core_cnt
            min_length = length

        elif max_core == core_cnt: # 코어 개수 같으면 선 길이만 비교
            if min_length > length:
                min_length = length

        return

    else:
        for i in range(4):# 4가지 방향중에 하나
            if possible(k,i): # 만약 그릴 수 있으면
                line = draw_line(k,i,2)
                back_tracking(k+1,length+line,core_cnt+1)
                draw_line(k,i,0) # 그렸던 것을 그대로 원상복구시켜줌. -> 모든 2차원 배열 deepcopy 할 필요 없음.

        # 해당 코어 그리지 않을 경우
        back_tracking(k+1,length,core_cnt)

########################
sys.stdin = open("1767.txt")
input = sys.stdin.readline
testcase = int(input())
for tc in range(testcase):
    N = int(input())
    core = []
    board = []
    for i in range(N):
        array = list(map(int,input().split()))
        for j in range(N):
            if array[j] == 1:
                core.append((i,j))
        board.append(array)
    #print(core)
    #print(board)
    back_tracking(0,0,0)

    print('#{0} {1}'.format(tc+1,min_length))


"""
7    
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
"""