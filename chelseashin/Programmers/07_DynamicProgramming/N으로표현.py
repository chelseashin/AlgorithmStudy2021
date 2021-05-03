def solution(N, number):
    if N == number:
        return 1
    # 1. [SET * 8 초기화], 각 set마다 기본 수 "N" * i 수 초기화
    A = [set([int(str(N)*i)]) for i in range(1, 9)]
    print("A", A)
    # 2. n 일반화
    #   { 
    #       "n" * i U 
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set, 
    #    }

    # number를 가장 최소로 만드는 수 구함
    for i in range(1, 8):
        for j in range(i):
            for op1 in A[j]:
                for op2 in A[i-j-1]:
                    A[i].add(op1+op2)
                    A[i].add(op1-op2)
                    A[i].add(op1*op2)
                    if op2 == 0:
                        continue
                    A[i].add(op1//op2)
        print(A[i])
        if number in A[i]:
            return i+1
    return -1

print(solution(5, 12))
print(solution(2, 11))
# print(solution(5, 31168))