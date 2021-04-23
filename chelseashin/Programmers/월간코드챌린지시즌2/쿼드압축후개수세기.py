# 분할정복으로 풀이

def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):     # 분할정복
        start = arr[x][y]   # 해당 네모값 중 하나. 모두 같은 숫자여야 함
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != start:  # 하나라도 다르면 압축 불가
                    nn = n//2           # 다음 크기
                    comp(x, y, nn)
                    comp(x, y+nn, nn)
                    comp(x+nn, y, nn)
                    comp(x+nn, y+nn, nn)
                    return
        # 해당 구역에 모두 같은 숫자로 무사 통과 => 압축 가능
        answer[start] += 1      # 압축한 숫자 += 1

    comp(0, 0, N)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))