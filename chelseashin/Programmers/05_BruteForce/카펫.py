# 21:20 start
# 21:46 finish
# 26m 소요
# Brute Force

def solution(brown, yellow):
    total = brown + yellow
    # 노란 타일 최소 1개이므로 3부터 시작, 가로로 긴 직사각형이므로 제곱근까지 확인해도 무방
    for n in range(3, int(total**0.5)+1):
        if total % n:   # 정수로 나누어 떨어져 가로 * 세로 직사각형 이룸
            continue
        m = total // n
        if (n-2) * (m-2) == yellow:     # 안쪽 노란 타일의 갯수 조건 맞으면 바로 리턴
            return [m, n]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))