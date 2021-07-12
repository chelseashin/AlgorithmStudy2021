# 문제의 핵심
- 시뮬레이션
- 반사하는 코드

# 반사하는 코드
- 방향과 위치가 몇번만에 되돌아 오는가?
    - row는 (row-1) * 2 번만에 되돌아옴
    - col은 (col-1) * 2 번만에 되돌아옴
    - 따라서 속도가 row와 col을 넘는다면 되돌아오는것을 나머지 계산해주면 된다,
        - s = s % (row-1) * 2
        - s = s % (col-1) * 2
- 그다음 range를 넘겼을때는 어떻게하는가?: 일일히 반복문으로 계산해줘야함
    ```python
           nr, nc = loc[0], loc[1] # 처음 방향 선언
            for _ in range(shark.speed): # 속도만큼
                nr += shark.direction[0] # 방향 이동
                nc +=  shark.direction[1] 
                if out_of_range(nr, nc, row, col): # 범위가 넘어간다면
                    # 반대방향으로 가고
                    shark.direction = (-shark.direction[0], -shark.direction[1])
                    # 두번 방향을 이동해줘야함
                    # 왜? 한번 이동은 제자리이므로! 
                    nr += shark.direction[0]
                    nc += shark.direction[1]
                    nr += shark.direction[0]
                    nc += shark.direction[1]
    ```
# 왜 몰랐는가?
- 공식이 있는줄알고 한참 시간이 걸려서 찾아봄
- 공식은 없음

# 시간을 개선하려면?
- 여전히 배열을 선언한게 빠른듯하다.
- dictionary는 충돌 알고리즘때문에 늦는다.