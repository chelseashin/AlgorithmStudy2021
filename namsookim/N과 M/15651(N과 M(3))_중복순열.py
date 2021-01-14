# https://www.acmicpc.net/problem/15651
# 25분 소요

"""
1. itertools 에 product 는 중복순열을 사용할 수 있는 라이브러리이다.
   문법: product([], repeat = n)   , n은 반복할 횟수

2. M번 만큼 중복을 허용하여 순차적으로 구하면 되는 문제니 중복순열을 사용해서 해결할 수 있다.

3. 파이썬 내장함수 product의 시간복잡도: O(n!)

"""
#import time
from itertools import product
#start_time = time.time()
t = 0
N, M = map(int,input().split())
s = [i for i in range(1,N+1)]
result_list = list(product(s,repeat=M))
for xx in result_list:
    for x in xx:
        print(x,end=' ')
        print()
        #t +=1

    #print()

#end_time= time.time()
#print("time:", end_time - start_time)



