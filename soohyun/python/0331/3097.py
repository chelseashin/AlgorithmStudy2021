import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())
time = [int(input()) for _ in range(N)]
result = 0
left = 0
right = M * max(time)
 
while left <= right:
    mid = (left + right) // 2
    print(left, mid, right)
    judgedPeople = 0
    for t in time:
        judgedPeople += mid // t
        print("judge", judgedPeople, mid, t)
    
    if judgedPeople < M:
        left = mid + 1
    else:
        result = mid
        right = mid - 1
 
print(result)