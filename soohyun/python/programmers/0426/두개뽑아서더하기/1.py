import heapq

def solution(numbers):
    answer = []
    num_sum = dict()
    for i, value_1 in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            result = value_1 + numbers[j]
            if not num_sum.get(result, False):
                num_sum[result] = True
                answer.append(result)
    return sorted(answer)