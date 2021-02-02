# https://www.acmicpc.net/problem/17140

# 2시간 27분 소요
# 문제이해 20분
# 30분 디버깅

"""
문제
1. 초기 3x3 배열
2. R연산(행의 개수>=열의개수), C연산(행의 개수<열의개수) 중 하나 수행.
3. R연산 시 모든 행에 대해 정렬, C연산 시 모든 열에 대해 정렬
4. 정렬기준 :
    1. 수의 등장 횟수 (오름차순)
    2. 수 (오름차순)

풀이
1. 요구사항대로 구현

시행착오
1. 문제 -> 런타임에러. 처음 입력받을때 3x3 범위 밖의 값을 입력받을 수 있음.
   해결 -> 범위 초과할 때 배열값 참조 안하도록 설정

2. 문제 -> 열 정렬을 어떻게 할지 오래걸림
   해결 -> col_list = [i[n] i in array] 를 해주어 행과 똑같이 처리 후 다시 열로 변환


1. 중복되는 코드는 함수로 빼자
"""

r,c,k = map(int,input().split())

array = [list(map(int,input().split())) for _ in range(3)]

def check(array):
    R = len(array)
    C = len(array[0])
    if R>=C:
        return 'R'
    else:
        return 'C'

def calc(RC,array):
    new_array = []
    max_length = 3  # 범위 제한
    row_array = [] # 행 담기
    col_array = [] # 열 담기

    if RC == 'R':
        # R연산
        for arr in array:
            temp = []
            sort_list = [] #(수,해당 수가 나온 횟수) 저장

            for C in arr: # 해당하는 숫자 개수 세기
                if C!=0: # 0은 정렬 x
                    sort_list.append((C,arr.count(C)))

            set_list = list(set(sort_list))
            sort_list = sorted(set_list,key=lambda x: (x[1],x[0]))

            for n,c in sort_list: # 튜플을 리스트로 채워주기
                temp.append(n)
                temp.append(c)


            temp_length = len(temp)
            tag = False # 100넘었는지 체크 . 최대 크기제한을 100으로 두기 위해
            if temp_length > max_length:
                if temp_length>100:
                    max_length =100
                    tag = True

                else:
                    max_length = temp_length

            if tag:
                row_array.append(temp[:100])
            else:
                row_array.append(temp)

        # 끝에 0으로 채우기
        for arr in row_array:
            R_length = len(arr)
            if R_length < max_length:
                arr.extend([0] * (max_length - R_length))
            new_array.append(arr)

        return new_array

    # C연산
    else:
        for c in range(len(array[0])):
            col_list=[i[c] for i in array]
            temp = []
            sort_list = []

            for R in col_list:
                if R != 0:
                    sort_list.append((R, col_list.count(R)))

            set_list = list(set(sort_list))
            sort_list = sorted(set_list, key=lambda x: (x[1], x[0]))

            for n, c in sort_list:  # 튜플을 리스트로 채워주기
                temp.append(n)
                temp.append(c)

            # 최대 크기제한을 100으로 두기
            temp_length = len(temp)
            tag = False  # 100넘었는지 체크
            if temp_length > max_length:
                if temp_length > 100:
                    max_length = 100
                    tag = True

                else:
                    max_length = temp_length

            if tag:
                col_array.append(temp[:100])
            else:
                col_array.append(temp)

        for arr in col_array:
            # 끝에 0으로 채우기
            R_length = len(arr)
            if R_length < max_length:
                arr.extend([0] * (max_length - R_length))

        for c in range(len(col_array[0])):
            r_list = [i[c] for i in col_array]

            new_array.append(r_list)

    return new_array

def solve():
    cnt = 0
    global array
    while cnt<=100:
        row = len(array)
        columns=len(array[0])
        out_tag = False

        if r>row or c>columns:
            out_tag= True

        if out_tag == False: # 범위 내면 확인
            if array[r-1][c-1] == k:
                return cnt

        RC=check(array) # R 연산 or C 연산
        new_array = calc(RC,array)

        array = new_array
        cnt +=1

    return -1

print(solve())