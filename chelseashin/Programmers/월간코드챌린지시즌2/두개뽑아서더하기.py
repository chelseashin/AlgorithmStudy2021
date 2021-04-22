# 라이브러리 사용한 첫 번째 풀이
# from itertools import combinations
# def solution(numbers):
#     answer = set()
#     for comb in combinations(numbers, 2):
#         answer.add(sum(comb))
#     return sorted(list(answer))

# 두 번째 풀이
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    return sorted((answer))     # set도 sorted가 된다!

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))