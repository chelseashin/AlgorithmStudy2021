# 처음 풀었을 때 바로 시간 초과..

# N이 2가 아닌 짝수라면 두 소수의 합으로 구할 수 있음 (-> 골드바흐의 추측)
# 이것 쓰면 5%에서 시간초과 ㅋㅋㅋㅋㅋ
# 홀수 소수는 짝수 소수(2) + 홀수 소수의 조합으로 밖에 안 됨
# 이 조건 추가하니 49%에서 시간초과,,

# 에라토스테네스 체 미리 만들어놓고 답 구하자
# 참고 https://yuuj.tistory.com/158
#
from sys import stdin
input = stdin.readline

num = 2000000
A = [0, 0] + [1] * (num-1)
primes = []     # 소수 리스트
for i in range(2, num+1):
    if A[i]:
        primes.append(i)
        for j in range(2*i, num, i):
            A[j] = 0

def isPrimeNumber(N):
    # 2000000보다 크면 소수로 나눠지는지 확인
    if N > num:
        for prime in primes:
            if prime >= N:
                break
            elif N % prime == 0:
                return False
        return True
    # 2000000보다 작으면 소수인지 바로 확인
    return A[N]

def solve(N):
    if N < 4:
        return "NO"
    elif N % 2 == 0:   # 골드바흐의 추측
        return "YES"
    else:
        if isPrimeNumber(N-2):      # 홀수 소수는 짝수 소수(2) + 홀수 소수의 조합으로 밖에 안 됨
            return "YES"
        return "NO"

# main
T = int(input())
for _ in range(T):
    N = sum(list(map(int, input().split())))
    print(solve(N))