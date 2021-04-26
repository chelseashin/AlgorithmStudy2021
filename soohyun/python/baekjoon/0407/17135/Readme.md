# 1. 핵심
# 2. 걸린시간
 * 문제 해석 시간: 1시간 30분
 * 계획 시간: 1시 40분 ~ 2시 40분 1시간
 * 코딩 시간: 1시간
 * 디버깅 시간: 2시간
 * 수정 제출 시간: 

# 3.  알고리즘
```python
 max = 0
 while True    
    x, y, z = next_permutation(x, y, z, col)
    if x == -1:
        return max
    while i == 0:# 모든 적을 한턴씩 물리칠때까지
        removed_enemy += attack(x, y, z)
        change_location()
    if max > removed_enemy:
        max = removed_enemy

```
## 1.1 next_permutation
```python
def next_permuation(x, y, z, N):
    if z < N:
        return x, y, z + 1
    else:
        if y < N - 1:
            y = y + 1
            z = y + 1
            return x, y, z
        else:
            if x < N - 2:
                x = x + 1
                y = x + 1
                z = y + 1
                return x, y, z
            else:
                return -1, -1 ,-1
```
## 1.2 attack
```python
    enemy = 0
    find_attack_range(x)# 공격가능범위 찾기
    attack_left(x, y) # 공격 가능한것중 가장 왼쪽
    enemy += remove_enemy(x, y) # 적 지우기
```
### 1.2.1 거리별로 공격
```python
    def find_attack_range(r, c, attack_range):
        start_x, start_y = r-attack_range, c
        check_can_go(start_x, start_y) # 경계선, 적 유무 판단
        can_attack_list = list()
        for i in range(1, 3):
            nx, ny = (start_x - attack_range) + i, start_y - i
            check_can_go(nx, ny)
            can_attack_list.append(nx, ny)
            nx, ny = (start_x - attack_range) + i, start_y + i
            chcek_can_go(nx, ny)
            can_attack_list.append(nx, ny)
```
### 1.2.2 왼쪽것 지움
```python
    def attack_left(x, y):
        가장 왼쪽것을 지운다
    def remove_enemy(x, y):
        MAP[x][y] = 0
        return 1
```

## 1.3 changelocation
```python
    i -= 1 # i 는 row 값
```
# 3. 추측 시간 복잡도 및 공간 복잡도
```
시간복잡도: 
# 4. 실수한것 & 복기할것