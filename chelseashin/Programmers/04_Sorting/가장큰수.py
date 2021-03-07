# 금방 짰으나 시간초과로 광탈한 오답..
# from itertools import permutations
#
# def solution(numbers):
#     ans = 0
#     N = len(numbers)
#     for perm in permutations(list(map(str, numbers)), N):
#         ans = max(ans, int(''.join(perm)))
#     return str(ans)

# 다른 사람 풀이.. 와 이런 생각은 어떻게 하는 거지..
def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(nums)))

# 아니 이게 대체 무슨 뜻인지.. 어렵다 이것도..
# def solution(numbers):
#     nums = [str(n) for n in numbers]
#     longest = max([len(n) for n in nums])
#     nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
#     print(nums, longest)
    # return str(int(''.join(nums)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))