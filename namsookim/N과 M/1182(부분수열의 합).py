
"""
풀이
1. 백트래킹 문제이다...
2. 핵심은 현재 함수를 호출할 때 현재 몇번째 인덱스를 가져 갔는지 체킹해주면서 함수를 불러야한다.
3. 그 함수 이후부터 처리할 수 있도록.
4. return 하면 안됨. return하면 답 찾고 바로 끝내기 때문에. 이후에 더 있을수도 있음

예외 케이스

2 0
0 0
답 : 3

0, 0 , 0 0

"""
N,S = map(int,input().split())
array = list(map(int,input().split()))
ans = 0

def solve(sum,index):

    if sum == S and index!=0:
        global ans
        ans +=1
        #return # 이거 해서 틀림

    for i in range(index,len(array)):
        solve(sum+array[i],i+1)


solve(0,0)
print(ans)