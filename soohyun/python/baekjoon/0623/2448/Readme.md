# 문제의 핵심
- 분할정복

# 사용자료구조
- 별 구조: 행이 N 열이 2*N-1인 2차원 배열

# 알고리즘
- N이 3인경우
    - 맨꼭대기부터 상대적인 위치로 별을 찍는다.
- N이 3보다 큰경우
    - 아래 세개로 나누어 별을 찍는다.
        - 가운데
        - 왼쪽
        - 오른쪽 

# 복잡도
- 시간복잡도 O(3*N//3): 가운데, 왼쪽, 오른쪽 찍기, N//3만큼 나누어져서 찍기
- 공간복잡도 O(2*N-1 * N): 행, 렬

# Code Snippet
```python
    def recursive(row, col, N):
        if N == 3:
            arr[row][col] = '*'

            arr[row+1][col-1] = '*'
            arr[row+1][col+1] = '*'

            arr[row+2][col-2] = '*'
            arr[row+2][col-1] = '*'
            arr[row+2][col] = '*'
            arr[row+2][col+1] = '*'
            arr[row+2][col+2] = '*'
            return

        recursive(row, col, N//2)
        recursive(row + N//2, col + N//2, N//2)
        recursive(row + N//2, col - N//2, N//2)
        return
```

# 복기할것
- 틀렸습니다: *row 로출력하면 에러남 
    - 왜? 적당한 공백을 주기때문에 1개의 공백이 출력된다는 보장이 없음
- 시간초과:
    - join후 출력하지 않고 row, col 로 반복하여 출력하면 시간 초과남
