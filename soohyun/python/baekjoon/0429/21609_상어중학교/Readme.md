# 문제의 핵심
- 구현 문제
- 조건에 따라 얼마나 정확하고 빠르게 문제를 해결하는가?
- 걸린 시간: 5시간 + a
- 회전 + 중력 합한문제
# 알고리즘
1. 가장큰 블록 그룹 찾기
2. 없어진 블록 계산 
3. -1을 제외한 모든 숫자 아래로 내리기(중력)
4. 반시계방향 돌리기
5. -1을 제외한 모든 숫자 아래로 내리기(중력)
# 사용 자료구조
1. 게임보드: 2차원 배열
2. 블록그룹들(block_groups): dict내 dict ```{student:{1:True}}```
3. max block groups: dict 내 dict ```{num:12, blocks:{(1,2):True}, rainbow:12}```
4. max_block_list, max_rainbow_list: 리스트내 튜플, 튜플내 dict ```[(0, 1, {(1,2):True, (2,5):True}, 12)]```
# 자주사용한 Code Snippet
## 1.1 rotation (counter clock wise)
```python
    board_copy = list() # board 복사
    for i in range(N):
        arr = list()
        for j in range(N):
            arr.append(board[i][j]) 
        board_copy.append(arr)
    # 첫행은 맨 끝열부터 간다.
    for col in range(N-1, -1, -1): 
        for row in range(0, N): 
            # 첫행이(전체가로)  맨끝 열값으로 대체(전체세로)
            board[N-1-col][row] = board_copy[row][col]
            # clock wise라면
            # 첫행이(전체가로)  첫열로 대체(전체 세로)
            board[N-1-col][row] = board_copy[row][N-1-col]
```
## 1.2 gravity
```python
for row in range(N-2, -1, -1):  # 끝행에서부터 첫행까지
    for col in range(N):
        if board[row][col] >= 0:  #만약 떨어지는 원소라면
            input_row = row 
            for nrow in range(row+1, N):  # 시작행부터 끝행까지
                if board[nrow][col] < -1:  # 만약 떨어지지 않는원소를 본다면 
                    input_row += 1  # 넣어야할곳으로 간다.
                else:
                    break
            if input_row != row:  # 현재행에서 이동했다면
                board[input_row][col] = board[row][col]  # 그 원소를 떨어트리고
                board[row][col] = -2  # 현재원소는 -2로 없는것으로 설정
            # 이동하지 않았다면 그대로 냅둠
```


# 추정 복잡도
1. 시간복잡도: O(N^2s) 실제시간 160 ms
    - O(N*N)
        - bfs * 모든 행렬 순회
    - O(NlogN)
        - O(N/2): N의 절반이 블록그룹인경우
        - O(2NlogN): sorted 2번
    - O(N)
        - 한개의 블록그룹제거 
    - O(N*N)
        - -1을 제외한 모든 숫자 아래로 내리기(중력)
        - 모든행을 제외하고 모두 내려야할 수 있으므로
    - O(2N*N)
        - 반시계방향 돌리기
        - 복사후 저장

2. 공간복잡도: O(2N^4)
    - O(N^2) 
        - 보드개수
        - copy board
    - O(N)
        - 블록그룹개수

# 빠르게 푼사람 코드
- rotate와 gravity는 유사
-큰 블록그룹 찾아야함
# 복기할 부분
1. 왜 시간이 많이 소요되었나?
    - 디버깅 시간이 많이 걸림
    - 회전과 중력코드를 작성하는데 오래걸림
1. 실수한부분
    - 문제의 조건을 하나 빼먹음
        - 칸이 많은것 > rainbow > 행큰것 > 열큰것
    - 칸개수를 점수에 더해야하는데 칸 값을 더함