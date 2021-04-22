# 25분 소요

def solution(n):
    triangle = []   # 삼각형 틀
    total = 0       # 채워야할 숫자 갯수
    for i in range(1, n+1):
        triangle.append([0] * i)
        total += i

    dr = (1, 0, -1)
    dc = (0, 1, -1)
    
    r, c, d = 0, 0, 0         # 시작 좌표, 방향
    triangle[r][c] = 1        # 시작 위치 그리기
    total -= 1                # 그렸으니까 -1 해주기

    while total:              # 다 그릴 때까지
        while True:
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < n and 0 <= nc < len(triangle[nr])) or triangle[nr][nc]:
                d = (d+1) % 3   # 방향 전환
                break
            triangle[nr][nc] = triangle[r][c] + 1   # 새 위치에 +1한 값 그리기
            total -= 1
            r, c = nr, nc
    # print("완성된 삼각형", triangle)

    # 출력
    # answer = []
    # for row in triangle:
    #     for value in row:
    #         answer.append(value)
    return [value for row in triangle for value in row ]     # 한 줄 정답 출력

print(solution(4))
print(solution(5))
print(solution(6))