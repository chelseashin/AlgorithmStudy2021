# 14:10 start
# 14:14 understand problem & coding
# 14:31 pass

def solve(blocks):
    result = []
    A = []
    for floor in range(len(blocks)):    # 몇 층
        A.append([0] * (floor+1))
        idx, value = blocks[floor]      # 몇 번째, 값
        A[floor][idx] = value           # 주어진 정보 배열 A에 표시

        # 해당 층에서 유일하게 알고 있는 값을 기준으로 오른쪽, 왼쪽으로 정보 완성시킴
        # 오른쪽 탐색
        for x in range(idx+1, floor+1):
            A[floor][x] = A[floor-1][x-1] - A[floor][x-1]
            
        # 왼쪽 탐색
        for x in range(idx-1, -1, -1):
            A[floor][x] = A[floor-1][x] - A[floor][x+1]
        
        # print(A[floor])     # 완성된 행
        result += A[floor]    # 결과 리스트에 바로 추가
        
    return result

print(solve([[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]))
print(solve([[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]))