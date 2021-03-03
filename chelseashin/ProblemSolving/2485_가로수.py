# 21:30 start
# 22:03 pass 1400ms로 시간 복잡도 꼴찌 이게 웬 일..
# O(N^2)으로 오래 걸렸기 때문에 당연한 결과
# gcd(Greatest Common Devisor) 최대공약수 구하는 함수 이용해서 148ms로 시간 단축 => 통과(소요시간 30m)

import sys
input = sys.stdin.readline
from math import gcd

n = int(input())
trees = []
gaps = []
for i in range(n):
    trees.append(int(input()))
    if i > 0:
        gaps.append(trees[i] - trees[i-1])

# 최대공약수 구하는 gcd 함수 이용
max_gap = gcd(gaps[0], gaps[1])
for i in range(1, n-1):
    max_gap = gcd(max_gap, gaps[i])     # 최대공약수 갱신

# 두 나무 사이 가장 긴 거리를 간격으로 나눈 몫 + 1이 전체 나무 수.
# 놓을 수 있는 전체 나무 수 - 주어진 나무 수 n을 빼주면 심어야하는 나무 수!
print((trees[-1]-trees[0]) // max_gap + 1 - n)


# 시간 엄청 오래 걸린 코드(시간복잡도 O(N^2))
# max_gap = 1
# for k in range(2, min(gaps)+1):
#     flag = True
#     for gap in gaps:
#         if gap % k:
#             flag = False
#             break
#     if flag:
#         max_gap = max(max_gap, k)

# print((trees[-1] - trees[0]) // max_gap + 1 - n)