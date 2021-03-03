# 나의 풀이(성공)
def dfs(depth, numbers, target, temp):
    global answer
    if depth == len(numbers):
        if temp == target:
            answer += 1
        return
    dfs(depth+1, numbers, target, temp + numbers[depth])
    dfs(depth+1, numbers, target, temp - numbers[depth])

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, target, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))

# 첫 시도 - 시간초과 ..
# def perm(depth, N, L, numbers, target):
#     global answer
#     if depth == N:
#         if eval(''.join(L)) == target:
#             answer += 1
#         return
#     for i in "+-":
#         L.append(i)
#         L.append(str(numbers[depth]))
#         perm(depth+1, N, L, numbers, target)
#         L.pop()
#         L.pop()
#
# def solution(numbers, target):
#     global answer
#     answer = 0
#     N = len(numbers)
#     perm(0, N, [], numbers, target)
#     return answer