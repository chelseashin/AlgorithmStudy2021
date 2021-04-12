# 17:00 start
# 17:39 finish
# Binary Search로 구현

from sys import stdin
input = stdin.readline

N = int(input())
numLst = list(map(int, input().split()))    # 상근이가 가진 숫자 리스트
M = int(input())
chkLst = list(map(int, input().split()))    # 체크해야 할 숫자 리스트
numInfo = {v: i for i, v in enumerate(chkLst)}
# print(numInfo)

# 오름차순 정렬
numLst.sort()
chkLst.sort()

findLst = [0] * M     # 찾은 숫자 1로 표시

for i in range(M):
    num = chkLst[i]     # 찾을 숫자
    left, right = 0, N-1
    while left <= right:
        mid = (left+right) // 2
        if num < numLst[mid]:
            right = mid - 1
        elif num > numLst[mid]:
            left = mid + 1
        else:   # 숫자 일치
            findLst[numInfo[num]] = 1
            break

print(*findLst)