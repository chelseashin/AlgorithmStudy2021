def solution(m, n, puddles):
    A = [[0] * (m+1) for _ in range(n+1)]
    A[1][1] = 1				# 시작 위치 표시
    for pr, pc in puddles:	# 물 웅덩이 표시
        A[pc][pr] = -1

    for r in range(1, n+1):
        for c in range(1, m+1):
            if (r, c) == (1, 1):	# 시작 위치
                continue
            if A[r][c] == -1:		# 물 웅덩이면 0으로 바꿔줌
                A[r][c] = 0
            else:
                A[r][c] += (A[r-1][c] + A[r][c-1])	# 좌, 상 방향의 값을 더해줌
        
    return A[n][m] % 1000000007

print(solution(4, 3, [[2, 2]]))