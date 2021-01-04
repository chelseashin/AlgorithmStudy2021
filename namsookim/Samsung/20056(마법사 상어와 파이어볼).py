# https://www.acmicpc.net/problem/20056
# 2:32 시작
# 2:55 코딩
# 3:15 좌표 반환 구현
# 4:30 런타임 에러
# 5:17 성공

"""

풀이:

1. array에 있는 모든 파이어볼의 위치, 속력, 방향을 이용해서 이동시킨 후, 새로운 위치에 모든 파이어볼을 저장.
2. 새로운 배열 만들어 파이어볼 개수가 2개 이상이면 문제의 조건에 맞추어 처리한 뒤 append 하고 1인 경우는 그대로 저장.
3. 반복

틀린 원인:
1. 음수일 때 좌표반환 다음과 같이 해서 런타임 에러 .  ny = N - (abs(ny) % N)   // 47분 소요

2. 파이어볼 합칠때 개수가 2개 이상일 경우에만 처리를 하였고 1개일 때는 고려하지 않았다.
   => new_array라는 새로운 배열 만들어서 옮기는 방식으로 구현했기 때문에 개수 1개일때도 처리 해줬어야됨. new_array에 개수 1개짜리는 반영이 안됐음.

3. 벽 넘어가는 부분 구현에서 오래 걸림
"""

N,M,K = map(int,input().split())
array = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    array[r-1][c-1].append((m,s,d)) # 질량, 속도, 방향 순으로 입력

dx = [-1,-1,0,1,1,1,0,-1] # 0~7
dy = [0,1,1,1,0,-1,-1,-1]

def move(x,y,s,d): # 새로운 위치의 좌표 반환해주는 함수 (파이어볼 이동)
    nx = x + s*dx[d]
    ny = y + s*dy[d]

    if nx < 0 or nx >=N:
        if nx >= N: # 양수면
            nx = nx % N
        elif nx < 0: # 음수면
            nx = N-1 - (abs(nx)-1)%N # 수정
    if ny < 0 or ny >=N:
        if ny >= N: # 양수면
            ny = ny %N
        elif ny < 0: # 음수면
            ny = N-1 - (abs(ny)-1)%N
    return nx , ny

def go(array): # 같은 위치의 파이어볼 합치는 함수
    new_array = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if len(array[x][y]) > 1:
                #print(x,y)
                fireball_sum = 0
                fireball_speed = 0
                one_tag = False
                two_tag = False
                for m,s,d in array[x][y]:
                    fireball_sum += m
                    fireball_speed +=s
                    if d % 2 == 1:
                        one_tag = True
                    else:
                        two_tag = True
                new_m = fireball_sum//5
                if new_m == 0:
                    continue # 질량이 0이면 소멸
                new_s = fireball_speed//len(array[x][y])
                direction = []
                if one_tag and two_tag: #둘다 트루면 홀짝 있는거니
                    #새로운 방향 1,3,5,7
                    direction.append([1,3,5,7])
                else:
                    direction.append([0,2,4,6])
                #print(direction[0])
                for dir in direction[0]:
                    new_array[x][y].append((new_m,new_s,dir))
            
            elif len(array[x][y]) == 1: # 1개 있으면 .
                new_array[x][y]=array[x][y]

    return new_array

# 전체 질량을 반환해주는 함수
def check(array):
    answer =0
    for x in range(N):
        for y in range(N):
            if len(array[x][y]) == 0:
                continue
            else:
                for m,s,d in array[x][y]:
                    answer += m
    return answer


# 파이어볼이 K번 이동했을 때의 질량값 구하기
def solve(array):
    for _ in range(K):
        new_array = [[[] for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if len(array[x][y]) != 0: # 개수가 0일 경우 볼 필요도 없음
                    #print(array[x][y])
                    for m,s,d in array[x][y]: 
                        #print(m,s,d)
                        nx,ny =move(x,y,s,d) # 이동한 뒤 새로운 좌표 반환
                        #print(nx,ny)
                        new_array[nx][ny].append((m,s,d)) # 질량, 속력, 방향 저장

        array=go(new_array)

    print(check(array))

solve(array)
