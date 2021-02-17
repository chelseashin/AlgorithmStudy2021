# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo
# 10:35
# 12:29 성공

# 1시간 54분 소요
"""
풀이
1. 좌표값을 기준으로 어떤 bc에 속하는 지 판단한 뒤, 합이 최대가 되게끔 해야된다.
2. 겹치는 부분이 없을 경우는 간단하게 범위내 P값을 더하면 된다.
3. 겹치는 부분일 경우 경우의수를 따져가며 가장 합이 크게 되는 값을 반환한다.

값 처리
1. 두개가 같은곳이면 하나만 더함. => /2를 해서 더해야되니
2. 두개가 다른곳이면 각각 더함

시행착오
1. 겹치는 부분을 어떻게 처리해야될 지 고민을 많이 하였다.
2. 좌표값 실수. (행열이라고 생각해서 반대로 함)

"""

import sys

sys.stdin = open('5644.txt')

def check_BC(x1,y1,x2,y2):
    pos_A = [0] # 충전기 어디와 인접하는 지 기록
    pos_B = [0]
    max_result = 0
    for i in range(len(BC)):
        BC_X,BC_Y,C,P= BC[i][0],BC[i][1],BC[i][2],BC[i][3]

        if abs(BC_X-x1) + abs(BC_Y-y1) <=C: # 접속가능
            pos_A.append(i+1)
        if abs(BC_X-x2) + abs(BC_Y-y2) <=C:
            pos_B.append(i+1)

    # 가능한 곳의 최대값 구해주기
    for i in range(len(pos_A)):
        a = pos_A[i]

        for j in range(len(pos_B)):
            b = pos_B[j]

            if a == b:
                temp = charge[a]
            else:
                temp = charge[a]+charge[b]

            max_result = max(temp,max_result)
        max_result = max(a,max_result)

    return max_result


def solve():

    dx = [0,0,1,0,-1] # 이동x, 상,우,하,좌
    dy = [0,-1,0,1,0]
    x1,y1 = 1,1
    x2,y2 = 10,10
    answer = 0

    ans = check_BC(x1, y1, x2, y2) # 첫 좌표 범위내 드는 지 확인
    answer += ans

    for i in range(len(people[0])):
        dir1=people[0][i]
        dir2=people[1][i]

        nx1,ny1 = x1+dx[dir1],y1+dy[dir1]
        nx2,ny2 = x2+dx[dir2],y2+dy[dir2]

        # BC들 범위 안에 드는 지 체크
        ans = check_BC(nx1, ny1, nx2, ny2)

        answer += ans
        x1,y1,x2,y2 = nx1,ny1,nx2,ny2

    return answer

tc = int(input())
for t in range(tc):
    M,A = map(int,input().split())
    people=[list(map(int,input().split())) for _ in range(2)]

    BC = []
    charge = [0] # 인덱스 맞춰주기 위해 충전량 0을 추가

    for _ in range(A):
        temp = list(map(int,input().split()))
        BC.append(temp)
        charge.append(temp[3]) # P값 인덱스에 맞춰 추가

    print('#{0} {1}'.format(t+1,solve()))
