"""
heapq는 일반적인 리스트와는 다르게,
가지고 있는 요소를 push, pop할 때마다 자동으로 가장 작은 값이 0번 자리로 온다.
정렬 비용을 줄이기 위한 문제 해결에 주로 사용
완전이진트리 기반의 자료구조로
모든 부모 노드가 자식 노드보다 작거나 같은 값을 가짐
가장 작은 요소가 항상 루트인 heap[0]
"""

"""
시행착오 
1. scoville 리스트를 계속 heapify 해줌(시간초과 원인)
2. answer += 1 위치 고침
3. try - except 문 별로 사용 안 해봄.. 
"""
scoville, K = [1, 2, 3, 9, 10, 12], 7


# 개선된 코드
import heapq

def solution(scoville, K):

    heapq.heapify(scoville)     # heapify 함수 이용
    answer = 0
    while scoville[0] < K:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            answer += 1
        else:
            return -1
    return answer

print(solution(scoville, K))


# 최초 통과 코드
"""
import heapq

def solution(scoville, K):
    pq = []
    for degree in scoville:
        heapq.heappush(pq, degree)
    answer = 0
    while pq[0] < K:

        try:
            heapq.heappush(pq, heapq.heappop(pq) + heapq.heappop(pq) * 2)
        except:
            return -1
        answer += 1
    return answer
"""