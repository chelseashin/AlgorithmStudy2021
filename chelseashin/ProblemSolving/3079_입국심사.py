# 이분탐색 문제
# 참고 : https://data-bank.tistory.com/26
# 1시간 정도 소요

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
time = [int(input()) for _ in range(N)]

left = min(time)                    # 최소 시간
right = answer = max(time) * M      # 최대 시간

while left <= right:
    total = 0       # mid 시간 동안 검사할 수 있는 총 사람의 수
    mid = (left + right) // 2
    for i in range(N):      # 입국심사대별로 검사
        total += mid // time[i]
    if total >= M:          # 검사할 수 있는 총 사람 수가 M보다 크면 가능한 경우
        right = mid - 1     # 오른쪽에서 좁혀주기
        answer = min(answer, mid)   # 최솟값 갱신
    else:
        left = mid + 1      # 왼쪽에서 좁혀주기
    # print(left, right, mid, total)
print(answer)