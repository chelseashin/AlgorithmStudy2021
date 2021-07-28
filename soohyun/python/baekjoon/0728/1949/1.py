from enum import Enum
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
class Town(Enum):
    EXCELLENT = 0
    NORMAL = 1

def solution(node, weight, N):
    visited = [False for _ in range(N)]
    visited[0] = True
    def dfs(parent, dp):
        dp[parent][Town.EXCELLENT.value] = weight[parent]
        dp[parent][Town.NORMAL.value] = 0
        #print("parent mpde", dp)
        children = node[parent]
        for child in children:
            if not visited[child]:
                visited[child] = True
                #print("before", parent, dp)
                dp = dfs(child, dp)
                dp[parent][Town.EXCELLENT.value] += dp[child][Town.NORMAL.value]
                dp[parent][Town.NORMAL.value] += max(dp[child][Town.EXCELLENT.value], dp[child][Town.NORMAL.value])
                #print("after", parent, dp)
        return dp

    return dfs

    


def main():
    N = int(input().rstrip())
    node = [[] for _ in range(N)]
    weight = list(map(int, input().rstrip().split(" ")))
    for _ in range(N-1):
        m1, m2 = map(int, input().rstrip().split(" "))
        node[m1-1].append(m2-1)
        node[m2-1].append(m1-1)
    value = solution(node, weight, N)
    dp =  [[0, 0] for _ in range(N)]
    dp = value(0, dp)
    #print(dp)
    print(max(dp[0][Town.EXCELLENT.value], dp[0][Town.NORMAL.value]))

   #
   # 

   # 
   # 
        

if __name__ == "__main__":
    main()