# **1. 문제의 핵심(키워드)**
- 분할정복
- L-트로미노 타일링
- 수학적 귀납법
# **2. 문제풀이**
- 수학적 증명(참고:https://rebro.kr/64)
    - n=1일때 2x2 크기 정사각형에 L 트리미노하나넣으면 채울 수 있음
    - n=k일때 L 트리미노를 한칸을 제외하고 채울 수 있음
    - n=k=1일때 L-트리미노로 한변의 길이가 k+1인 정사각형을 채울 수 있음
- 풀이법
    - k행k열이 만족하면 그행에 숫자
    - k행k+1열이 트리미노를 만족하면 그 행에 숫자채움
    - k+1행 k열이 트리미노를 만족하면 그 행에 숫자 채움
    - k+1행 k+1열이 트리미노를 만족하면 그 행에 숫자를 채움


# **3. 코드 설명**
```python
    def recursive(self, row, col, size):
        self.num += 1 
        next_size = size//2
        # 0행0열이 다른숫자로 채워져있지 않다면(L-트리미노를 만족한다면)
        if self.check(row, col, next_size): 
            # 그칸에 숫자를 채운다.
            self.tile[row+next_size-1][col+next_size-1] = self.num
        # 아래도 반복
        if self.check(row+next_size, col, next_size):
            self.tile[row+next_size][col+next_size-1] = self.num
        if self.check(row, col+next_size, next_size):
            self.tile[row+next_size-1][col+next_size] = self.num
        if self.check(row+next_size, col+next_size, next_size):
            self.tile[row+next_size][col+next_size] = self.num
        # 가장 작은 타일이면 반환(2에 1승 2x2)
        if(size==2):
            return
        #그렇지 않으면 사이즈를 줄이면서 다음사이즈로감
        #가장 왼쪽
        self.recursive(row, col, next_size)
        #오른쪽
        self.recursive(row+next_size, col, next_size)
        #좌측 하단
        self.recursive(row, col+next_size, next_size)
        #우측 하단
        self.recursive(row+next_size, col+next_size, next_size)
        

    def check(self, row, col, size):
        for i in range(row, size+row):
            for j in range(col, size+col):
                if self.tile[i][j] != 0:
                    return False
        return True
```

# 복기할것
- 혼자 생각해내지는 못할문제