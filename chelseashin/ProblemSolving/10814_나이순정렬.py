# 21:55 start
# 22:09 pass
# 14분 소요

from sys import stdin
input = stdin.readline

N = int(input())
info = dict()       # {나이: [이름1, 이름2, ...]}
for _ in range(N):
    age, name = list(input().split())
    if int(age) not in info.keys():
        info[int(age)] = [name]
    else: 
        info[int(age)].append(name)

ages = sorted(info.keys())      # 나이 순으로 정렬
for age in ages:
    for name in info[age]:
        print(age, name)