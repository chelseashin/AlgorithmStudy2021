# https://www.acmicpc.net/problem/15666

"""
1. ' '.join 활용. 1 11 1111 같은 경우 temp += str(result[i]) 를 사용했을 때 같은 것으로 인식함
  join은 "11 11" "1 111" 이런식으로 공백이 포함되니 해결가능하다.

2. join 쓰임이 많으니 잘 활용할 수 있도록 숙달하자.
"""
N, M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
isUsed = set([])
result = [0]*M

def solve(k,num):
    if k==M:
        temp = ' '.join(map(str,result))

        if temp not in isUsed:
            isUsed.add(temp)
            for i in range(M):
                print(result[i],end= ' ')
            print()

        return

    for i in range(N):
        if num > array[i]:
            continue
        result[k] = array[i]
        solve(k+1,array[i])

solve(0,0)
#print(isUsed)