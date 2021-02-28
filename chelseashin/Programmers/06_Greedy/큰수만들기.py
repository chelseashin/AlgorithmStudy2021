# 순열 완전탐색 - 시간초과
# from itertools import combinations
#
# def solution(number, k):
#     N = len(number)
#     MAX = 0
#     for comb in combinations(number, N-k):
#         MAX = max(MAX, int(''.join(comb)))
#     return str(MAX)

# stack 으로 Greedy한 풀이.. 어려워서 다른 사람 풀이를 참고했다.
# Greedy는 순간에만 가장 큰 이득을 취하기 때문에
# 늘 최적해를 보장하는 것은 아니다!

def solution(number, k):
    stack = []
    for value in number:
        while stack and stack[-1] < value and k > 0:
            stack.pop()
            k -= 1      # 뽑아낸 갯수 -1 
        stack.append(value)
        # print(stack, k)
    if k > 0:       # k가 남아 있는 경우
        stack = stack[:-k]

    return ''.join(stack)

# print(solution("1924", 2))
# print(solution("1231234", 3))
print(solution("4177252841", 4))