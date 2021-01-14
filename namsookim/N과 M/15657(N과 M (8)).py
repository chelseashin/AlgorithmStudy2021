# https://www.acmicpc.net/problem/15657
"""
1. 비내림차순으로 정렬해야한다. 같을 수는 있지만 뒤에수가 앞에번호보다 낮으면 안됨.
2. 이전 값에대한 정보가 필요하다. 즉, 현재값의 정보를 저장해야 하는데 num이라는 인자를 통해서
   정보를 전달한 뒤, array[num] 값 보다 작은 수는 무시해준다.

"""
N,M = map(int,input().split())

result = [0] * M
#print(result)
array = list(map(int,input().split()))
array.sort()
#print(array)

def solve(k,num):
    if k == M:
        for res in result:
            print(res,end=' ')
        print()

        return  # return 안해줘서 개뻘짓함

    for i in range(N):
        #print(k,i)
        if array[num] > array[i]:
            continue
        result[k] = array[i]
        solve(k+1,i)

solve(0,0)
