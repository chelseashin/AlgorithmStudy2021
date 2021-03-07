# 20:20 start
# 21:12 finish
# 52m 소요.
# Brute Force
# 어렵지 않은 문제.. 다음에 풀 땐 시간 더 줄일 수 있을 것 같다!

from itertools import permutations

def isPrimeNumber(N):
    if N < 2:
        return False
    # 소수의 절반에 해당하는 제곱근까지만 살피기
    # 수가 수를 나누기 위해서는 그 몫이 항상 필요하며 나누는 수와 몫 중 어느 하나는 반드시 √n 이하이기 때문이다.
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    possible = set()        # 만들 수 있는 숫자 조합 리스트. set으로 중복 제거
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            possible.add(int(''.join(perm)))

    answer = 0
    for temp in possible:
        if isPrimeNumber(temp):
            answer += 1
    return answer

print(solution("17"))
print(solution("011"))