# 문제의 핵심
- 구현
- 회전하는코드
- 방향 전환 코드

# 헷갈렸던것
- 남은것은 버린다
- 버린것은 움직이는것이 아닌것!

# code Snippet
1. 회전하는 코드
```python
def start_tornado(maze, N):
    start = ((N-1)//2, (N-1)//2)
    count = 0
    sand_count = 0
    # 좌 하 우 상으로 반복함
    direction = [(0, 1, 0, -1), (-1, 0, 1, 0)]
    for i in range(1, N+1):
        # 1부터 N+1 까지 반복
        # 마지막은 한번만 반복되고 나머지는 
        # 1,1 2,2, 이렇게감
        repeat = 2 if i < N else 1
        for _ in range(repeat):
            for _ in range(i):
                # 방향이동
                nr = start[0] + direction[0][count]
                nc = start[1] + direction[1][count]
                # 시작을 바꿈
                start = (nr, nc)
            # i번 돌았으면 바꿈
            count = (count + 1) % 4
    return sand_count
```
2. 방향 바꾸는 코드
```python
def blow_sand(count, sand, maze, start_loc, N):
    out_sand = 0
    left_sand = sand
    for direction, percentage in BLOW.items():
        if count == 1: # 하
            # 음양반전, 숫자위치 변경
            dr, dc = -direction[1], -direction[0]
        elif count == 2:# 우
            # 열만 음양 반전
            dr, dc = direction[0], -direction[1]
        elif count == 3: # 상
            # 숫자위치만 변경
            dr, dc = direction[1], direction[0]
        else: # 좌
            #그대로
            dr, dc = direction
        nr, nc = start_loc[0] + dr, start_loc[1] + dc
    return out_sand

```
