# 11:25
# 11:29 끝
# 4분 소요
from itertools import permutations
N, M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
result_list=list(permutations(array,M))

for xx in result_list:
    for x in xx:
        print(x,end = ' ')
    print()
print()


