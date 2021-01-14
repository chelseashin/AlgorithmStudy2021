N, M = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
isUsed = set([])
result = []
def solve(k,num):
    if k==M:
        temp = ' '.join(map(str, result))
        if temp not in isUsed:
            isUsed.add(temp)
            print(temp)
        return
    for i in range(N):
        if num > array[i]:
            continue
        result.append(array[i])
        solve(k+1,array[i])
        result.pop() # 끝을 pop 하는 것은 O(1)!
solve(0,0)
#print(isUsed)