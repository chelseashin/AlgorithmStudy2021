# 1. 문제의 핵심
- 구현
# 2. 풀이 알고리즘
1. 위/왼쪽부터 하나씩 붙일수있는지 확인
  - can_attach, is_fit, 
2. 만약 붙일수없다면 위치 바꿈
  - change_location
3. 그래도 불가능하다면 회전
  - rotation
3. 회전에도 붙일수없다면 버림
## 2.0 사용 자료구조
- 노트북: 딕셔너리
- 스티커: 클래스
   인스턴스: 전체 row, 전체 col, 스티커, 스티커 길이
- 좌표: i, j

## 2.2 Code Snippet
- 메인로직
```python
def main():
    notebook = set()
    N, M, K = map(int, input().rstrip().split(" "))
    for _ in range(K):
        sticker_row, sticker_col = map(int, input().rstrip().split(" "))
        sticker = Sticker(sticker_row, sticker_col)
        sticker_set = list()

        # 스티커 입력받음
        for i in range(sticker_row):
            input_row = input().rstrip().split(" ")
            for j in range(sticker_col):
               if input_row[j] == '1':
                   sticker_set.append(Axis(i, j))

        sticker.sticker = sticker_set
        sticker.sticker_length = len(sticker_set)
        # 스티커를 붙일수있는지 확인
        attached_set = can_attach(notebook, sticker, N, M)
        # 반환되는 결과로 스티커를 붙잌
        notebook = notebook.union(attached_set)
        del sticker
    return len(notebook)
```

- 회전하는 코드
```python
 def rotation(self):
        for idx in range(self.sticker_length):
            # rows 규칙: row = N - row - 1
            self.sticker[idx].i = self.row - self.sticker[idx].i - 1 

            # row, col swap
            temp = self.sticker[idx].i
            self.sticker[idx].i = self.sticker[idx].j
            self.sticker[idx].j = temp

        # 현재 row 길이와 column길이 swap    
        tmp = self.row
        self.row = self.col
        self.col = tmp

```
- 붙일수있는지 없는지 확인하는코드 
```python
def can_attach(notebook, sticker, N, M):
    rotation_count = 4 # 회전 최대횟수
    sticker_set = set() 
    if len(notebook) == 0 and sticker.row <= N and sticker.col <= M:
        # 만약 아무것도 채워지지 않았고 노트북크기보다 스티커 크기보다 작아야
        sticker_set = sticker_set.union(change_tuple_set(sticker.sticker))
        # 스티커를 반환한다.
        return sticker_set

    while rotation_count > 0: # 회전갯수가 4번 초과하면 멈춤
        fit_set = change_location(N, M, sticker, notebook) # 위치 변경 (행, 렬을 하나씩 변경해봄)
        if len(fit_set) == 0: # 맞는것이 없다면
            rotation_count -= 1 
            sticker.rotation() # 다시회전
        else:
            sticker_set = sticker_set.union(fit_set) # 맞는것이 있다면 스티커반환
            break
    return sticker_set
```
- 방향 전환코드
```python
def change_location(N, M, sticker, notebook):
    # i, j를 하나씩 증가시켜서
    for i in range(N):
        for j in range(M):
            # 노트북에 제대로 맞는지확인
            fit_set = is_fit(sticker, i, j, notebook, N, M)
            if len(fit_set) > 0:
                return fit_set
    return {}

```
- 노트북이 제대로 맞는지 확인하는 코드
```python
def is_fit(sticker, i, j, notebook, N, M):
    fit_set = set()
    for partial in sticker.sticker:
        row, col = partial.i, partial.j
        nr, nc = row + i, col + j
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            # 범위를 벗어나거나
            return {}
        elif (nr, nc) in notebook:
            # 노트북에 이미 있다면 그냥 아무것도 반환 안함
            return {}
        #그렇지 않으면 더해줌
        fit_set.add((nr, nc))
    return fit_set
```


# 3. 시간 복잡도

# 4. 빨리푼사람 코드
- 비슷하게 풂, 붙일수있는코드를 flag로 해결

# 5. 복기할것
- 생각보다 한번에 통과한문제