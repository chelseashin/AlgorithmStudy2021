# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
# 10:40
# 11:07
# 27분 소요. 쓸데없이 시간 오래 걸렸음.

"""
1. heappush 선언이 필수이다. 그냥 heappop만 하면 힙구조로 되지 않음.

"""
import heapq
scoville = [1,2,3,9,10,12]
K = 7

def solve(scoville,K):

    cnt = 0
    q = []
    for x in scoville:
        heapq.heappush(q,x) # heappush 선언 필수!!

    while True: # 1개 이상일 때 실행

        a = heapq.heappop(q)
        if a>=K:
            return cnt

        if len(q)<1:
            return -1
        b= heapq.heappop(q)
        temp = a+(b*2)
        heapq.heappush(q,temp)
        cnt +=1

    return -1


print(solve(scoville,K))
