# **1. 문제의 핵심**
- 구현
    - 회전 하는코드
    - 인접한곳 숫자세는 코드
- bfs
# **2. 사용 자료구조**
- grid: 2차원 배열
- visited: 2차원 배열
- bfs의 큐: deque

# **3. 알고리즘**
- L만큼 반복
    - 회전한다
    - 녹인다.
- bfs를 실행한다.
# **4. Code Snippet**
1. 회전하는 코드
    - 첫행이 마지막 열로
    - 행이 마지막으로 갈수록 열은 처음으로 간다.
```python
    for i in range(0, N, calc):
        for j in range(0, N, calc):
            tornado(i, i+calc, j, j+calc, grid)
    diff = end_row - start_row
    sample_grid = [[grid[i][j] for j in range(start_col, end_col)] \
                               for i in range(start_row, end_row)]
    for i in range(diff):
        # grid의 열은 열이 진행할수록 작아짐 start_col+(diff-i-1)
        for j in range(diff):
            # grid의 열은 행으로 행은 열로진행
            grid[start_row+j][start_col+(diff-i-1)] = sample_grid[i][j]

```

# **5. 참고할만한 코드**
- dfs 버전
```python
def dfs(r, c):
    res = 1
    ices[r][c] = 0 # 방문한 노드는 제거해주기때문에  
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        # 4번모두 방문한경우 다음으로 들어가지 않아
        if 0 <= nr < N_ and 0 <= nc < N_ and ices[nr][nc] > 0:
            res += dfs(nr, nc)
    # 만약 네곳 모두 방문했다면 1을 반환한다.
    return res
```
# **4. 복기할것**
- 회전하는 코드는 여러번 볼것
    - 띄어넘을경우 row, col 이 어디를 향하는지 확인할것
- melt할때 다른 melt된것에 영향을 받으면 안됨
    - list에 append하고 나중에 한꺼번에 제거해야함
    - 혹은, 리스트를 복사해서 제거해야함
