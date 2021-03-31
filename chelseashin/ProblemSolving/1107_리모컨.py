# 20:10 start
# 20 50 풀이 보기..
# 21:30 pass

# Brute Force
# 처음에 DFS or BFS로 풀어야하나 고민함.. 

from sys import stdin
input = stdin.readline

# main
N = int(input())
M = int(input())
buttons = [1] * 10  
broken = list(map(int, input().split()))
for n in broken:
    buttons[n] = 0      # 고장난 버튼은 0, 아니면 1

# case1 (100번에서 +, - 로만 움직이는 경우)
minCnt = abs(N-100)

# case2 (1,000,000 채널까지 브루트 포스 진행)
for num in range(1000001):
    if abs(num-N) > minCnt:     # 가지치기
        continue
    num = str(num)
    for i in range(len(num)):
        if not buttons[int(num[i])]:   # 고장난 버튼이라면
            break
        elif i == len(num)-1:     # 마지막 자릿 수에서
            # 타겟 넘버를 뺀 값의 절댓값과 전체 자릿 수를 더한 값과 최솟값 비교
            minCnt = min(minCnt, abs(N-int(num)) + len(num))    # 최솟값 갱신
            # print(num, abs(N-int(num)) + len(num))
print(minCnt)