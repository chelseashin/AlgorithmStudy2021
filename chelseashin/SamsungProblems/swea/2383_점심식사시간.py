# 21:30 start
# 21:58 계단 선택 완료 - comb 함수
# 23:13 50개 tc 중 45개만 맞음.. 하..
# 다음 날 아침 1시간 디버깅해서 성공! 거의 3시간 꼬박 걸림..
# 내 힘으로 풀어서 뿌듯 ㅎ
# 틀린 이유가 명확했다. 처리 순서가 이상했다.

""" downStairs 함수에서 시행착오
1. 이번에 계단 내려가는 큐에 들어갈 타이밍인데 이미 꽉 차서 다음 시간에 들어가야하는 상황에서 
    나의 계단 입장 시간과 현 시각이 같은데 큐 길이가 3이면 매 턴마다 +1 해줌
    이 때, 모든 대기 큐의 원소를 해주는 게 아니라, 내 입장시간과 현 시간이 같을 때에만! +1 해줘야 함
 
2. 계단에서 처리 먼저 해주고 >> 계단 위에서 대기하는 사람 순으로 처리해줘야 하는데
    계단 위 대기 인원 먼저 처리하고 계단에서 빠져나가는 사람을 처리하니까 계속 오차가 발생
    동시에 계단 내려가는 사람 발생 문제가 생겨서 처리 위치를 바꿈

3. 함수 내에서 크게 3가지 작업 처리
    계단 내려가는 사람 처리 => 계단 위에서 대기하는 사람 처리 => 자기 타이밍인데 못 들어간 사람 대기시간 +1 처리
    순으로 재정비하니 pass

4. 변수명을 너무 못 지음.. 계단 내려가는 큐를 waitA라고 지어서 자꾸 헷갈림,, 결국 그대로 쓰긴 했다
"""

import sys
sys.stdin = open("2383_input.txt")
from collections import deque

def comb(depth):
    if depth == personCnt:
        A, B = [], []  # 계단별로 사람이 계단에 내려가기까지 걸리는 시간
        for num in range(personCnt):
            if not selection[num]:  # 0번 계단 선택
                sr, sc = stairs[0]
                pr, pc = person[num]
                A.append(abs(pr-sr) + abs(pc-sc) + 1)  # 계단 도착 후 1분 대기 후 내려갈 수 있으므로 + 1
            else:                   # 1번 계단 선택
                sr, sc = stairs[1]
                pr, pc = person[num]
                B.append(abs(pr-sr) + abs(pc-sc) + 1)
        downStairs(A, B)
        return
    for i in range(2):
        selection[depth] = i
        comb(depth+1)
        selection[depth] = 0

def downStairs(A, B):
    global MIN
    # 계단별로 일찍 도착한 순서대로 정렬
    A = deque(sorted(A))
    B = deque(sorted(B))
    waitA, waitB = deque(), deque()
    time = 0
    cnt = 0     # 탈출시킨 사람
    while cnt != personCnt:     # 크게 3가지 작업 처리
        time += 1
        # 계단 내려가는 사람 처리
        awlen, bwlen = len(waitA), len(waitB)
        for _ in range(awlen):
            if waitA and waitA[0] == time:
                waitA.popleft()
                cnt += 1
        for _ in range(bwlen):
            if waitB and waitB[0] == time:
                waitB.popleft()
                cnt += 1

        # 계단 위에서 대기하는 사람 처리
        alen, blen = len(A), len(B)
        for _ in range(alen):
            if A[0] == time and len(waitA) < 3:
                waitA.append(A.popleft() + stair1)
        for _ in range(blen):
            if B[0] == time and len(waitB) < 3:
                waitB.append(B.popleft() + stair2)
                
        # 들어갈 타이밍인데 못 들어간 경우, 해당 원소만 +1 처리
        if len(waitA) == 3:
            for i in range(len(A)):
                if A[i] == time:
                    A[i] += 1
        if len(waitB) == 3:
            for j in range(len(B)):
                if B[j] == time:
                    B[j] += 1
    MIN = min(MIN, time)    # 최솟값 갱신

# main
T = int(input())
for tc in range(T):
    N = int(input())
    stairs = []
    person = []
    personCnt = 0
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
        for j in range(N):
            if A[i][j] == 1:
                person.append((i, j))
                personCnt += 1
            elif 2 <= A[i][j] <= 10:
                stairs.append((i, j))
    # 2개의 계단 내려가는 시간
    stair1, stair2 = A[stairs[0][0]][stairs[0][1]], A[stairs[1][0]][stairs[1][1]]
    MIN = float('inf')
    selection = [0] * personCnt
    comb(0)
    print("#{} {}".format(tc+1, MIN))