# 22:40 start
# 23:09 pass
# 어제는 왜 이렇게 못 풀었는지 이해가 안 된다,, 
# Heap으로 접근하니 30분만에 pass했다.
# 요새 시뮬레이션 문제에 소홀했더니, 이런 결과가ㅠㅠ 더 더 정진하자 

from sys import stdin
input = stdin.readline
from heapq import heappush, heappop

# 4방향
dr = (-1, 0, 0, 1)
dc = (0, -1, 1, 0)

# 인접한 학생 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000
def satisfied():
    result = 0
    for r in range(N):
        for c in range(N):
            if not A[r][c]:
                continue
            cnt = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if A[nr][nc] in likeInfo[A[r][c]]:  # 좋아하는 학생 인접한 칸에 있으면
                    cnt += 1
            if cnt:     # 이게 계속 틀린 이유,,, cnt 있을 때만 결과에 더함(0이면 10의 -1승도 더해지므로 답이 틀린다!)
                result += 10 ** (cnt-1)
    return result

def drawIdx(idx):
    priorityQueue = []     # 최대 힙 사용(우선순위 큐로 활용)
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                continue
            likeCnt, emptyCnt = 0, 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if A[nr][nc] in likeInfo[idx]:  # 좋아하는 학생 Set에 있으면
                    likeCnt += 1
                if not A[nr][nc]:   # 빈 공간이면
                    emptyCnt += 1
            heappush(priorityQueue, (-likeCnt, -emptyCnt, r, c))   # 최대 heap에 넣어줌(우선순위 : likeCnt > emptyCnt > 행 > 열)
    
    like, empty, r, c = heappop(priorityQueue)     # 가장 높은 우선순위의 값 뽑은 정보
    A[r][c] = idx   # 자리 배치

# main
N = int(input())
A = [[0] * N for _ in range(N)]

likeInfo = dict()   # 학생 번호별 좋아하는 학생 정보 {학생 번호 : 좋아하는 학생 Set}
for _ in range(N**2):
    info = list(map(int, input().split()))
    likeInfo[info[0]] = set(info[1:])

# 주어진 순서대로 학생 자리 배치
for idx in likeInfo.keys():
    drawIdx(idx)

print(satisfied())     # 만족도 조사 결과 출력