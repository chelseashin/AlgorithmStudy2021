# 15:30 start
# 다시 풀자..
# 집의 갯수 N은 최대 200,000개. 집의 좌표는 1,000,000,000까지 있음.
# 이진 탐색을 이용하여 O(NlogX)에 문제 해결 가능.
# 가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾음.
# 이진탐색으로 찾기 => 반복문 이용


from sys import stdin
input = stdin.readline

N, C = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()    # 오름차순 정렬
# print(A)

left = 1
right = A[-1] - A[0]
# print(left, right)

result = 1
while left <= right:
    mid = (left + right) // 2       # 두 공유기 사이의 거리 의미
    value = A[0]                    # 가장 왼쪽에 설치
    cnt = 1
    for i in range(1, N):
        if A[i] >= value + mid:     # 설치 간격 충족
            value = A[i]
            cnt += 1
        if cnt >= C:
            break
    if cnt >= C:        # C개 이상의 공유기 설치할 수 있는 경우
        left = mid + 1
        result = max(result, mid)
    else:
        right = mid - 1
print(result)