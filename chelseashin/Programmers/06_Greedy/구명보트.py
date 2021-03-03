# 마지막.. 답 보고 아이디어 얻어서 풀기 가장 깔끔한 풀이
# 오름차순 정렬 후 가장 작은 값과 큰 값 더해
# limit 넘으면 작은 값만 큐에 다시 담고 큰 값은 그대로 pop
# limit 안 넘으면 둘다 pop

from collections import deque
def solution(people, limit):
    result = 0
    Q = deque(sorted(people))
    print(Q)
    while Q:
        left = Q.popleft()
        if not Q:
            return result + 1
        right = Q.pop()
        if left + right > limit:
            Q.appendleft(left)
        result += 1
    return result

# 첫 번째 시도
# 고작 30%만 통과..
# from collections import deque
#
# def solution(people, limit):
#     answer = 0
#     Q = deque(sorted(people))
#     # print(Q)
#     while Q:
#         boat = []
#         while Q:
#             x = Q.popleft()
#             if len(boat) < 2 and sum(boat) + x <= limit:
#                 boat.append(x)
#             else:
#                 Q.appendleft(x)
#                 break
#             if len(boat) == 2:
#                 break
#         # print(boat, Q)
#         answer += 1
#     return answer

# 두 번째 시도.. 또 30%에서 틀림
# def solution(people, limit):
#     start = 0
#     end = 2
#     N = len(people)
#     people.sort()
#     answer = 0
#     while True:
#         if sum(people[start:end]) <= limit:
#             answer += 1
#             start = end
#             if start >= N:
#                 break
#             end = start + 2
#             if end >= N:
#                 end = N
#         else:
#             end -= 1
#         if start > N+1:
#             break
#     return answer

# 다른 정답 풀이
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     N = len(people)
#     print(people)
#     light = 0
#     heavy = N-1
#     while light < heavy:
#         if people[light] + people[heavy] <= limit:
#             answer += 1
#             light += 1
#         heavy -= 1
#         print(light, heavy)
#     return N - answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50],  100))