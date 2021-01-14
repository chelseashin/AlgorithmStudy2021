N ,M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
result = [0]*M
check = [False] * N
isused = set([])
def solve(k,num):
    if k == M:
        temp = ''
        for i in range(M):
            temp += str(result[i])
        if temp not in isused:
            for i in range(M):
                print(result[i],end=' ')
            print()
            isused.add(temp)
        return

    for i in range(len(array)):
        if num > array[i]:
            continue
        if check[i] != True:
            result[k] = array[i]
            check[i] = True
            solve(k+1,array[i])
            check[i] = False

solve(0,0)