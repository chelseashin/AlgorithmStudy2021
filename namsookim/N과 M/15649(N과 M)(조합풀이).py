from itertools import permutations

N , M = map(int,input().split())
S = [i for i in range(1,N+1)]
#print(S)
ans=list(permutations(S,M))
for result in ans:
    for res in list(result):
        print(res,end=' ')
        #print()
    print()