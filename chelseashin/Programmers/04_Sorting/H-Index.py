# 16:00 start
# 16:27 한 개만 오답..
# 다르게 생각해
#
# 내림차순으로 정렬
def solution(citations):
    N = len(citations)
    citations.sort(reverse=True)  # 인용횟수 많은 순으로 정렬
    for h in range(N):
        # print(citations[h], h)
        if citations[h] <= h:     # h편 이상 인용된 논문이 h편 이상이면
            return h              # 가장 처음 조건 만족한 값이 H-Index
    return N

# 오름차순으로 정렬
# def solution(citations):
#     N = len(citations)
#     citations.sort()
#     for h in range(N):
#         # print(citations[h], N-h)
#         if citations[h] >= N-h:
#             return N-h
#     return 0

print(solution([3, 0, 6, 1, 5]))