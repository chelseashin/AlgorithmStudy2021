#1:30
#1:52 코딩
#3:45 시간초과. 디버깅 시작
#4:30 해결

# 3시간 소요

"""

시간초과가 났다. 
1. 배열의 크기가 작을 땐 deque가 메모리와 속도면에서 불리함. list가 유리!
2. 봄에서 나무 여러개면 어린 나이 나무 순으로 처리하는 거. 굳이 정렬할 필요 없다!
   => 가장 뒤에 나무가 계속 나이 어린나무가 된다.

3. 리스트 맨 앞에 삽입: list.insert(0,tree)

"""
import sys

input = sys.stdin.readline

N, M , K =map(int,input().split())
tree_food = [[5]* N for _ in range(N)]
tree_age = [[[] for _ in range(N)] for _ in range(N)] 
A = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    x,y,z = map(int,input().split())
    tree_age[x-1][y-1].append(z)

def spring(tree_food,tree_age):
    
    dead_tree = [] 
    for i in range(N):
        for j in range(N):
            if len(tree_age[i][j]) == 0:
                continue
            
            else :
                
                for _ in range(len(tree_age[i][j])):
                    tre = tree_age[i][j].pop()
                    
                    if tre <= tree_food[i][j]:
       
                        tree_food[i][j] -= tre
                        tre += 1
                        tree_age[i][j].insert(0,tre)
                        
                    else:
                        dead_tree.append((i,j,tre))
    return dead_tree

                
def summer(tree_food,dead_tree):
    for x,y,age in dead_tree:
        tree_food[x][y] += age//2
    
def check_five(tree_age):
    spread_tree = []
    for i in range(N):
        for j in range(N):
            if len(tree_age[i][j]) != 0:
                for age in tree_age[i][j]:
                    if age % 5 == 0:
                        spread_tree.append((i,j))

    return spread_tree



def fall(tree_age):

    spread_tree=check_five(tree_age)
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [1,1,0,-1,-1,-1,0,1]
    if len(spread_tree) >0:
        for x,y in spread_tree:        
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    tree_age[nx][ny].append(1)


def winter(tree_food,A):
    
    for i in range(N):
        for j in range(N):
            tree_food[i][j] += A[i][j]


def survive_check(tree_age):
    answer = 0 
    for i in range(N):
        for j in range(N):
            answer += len(tree_age[i][j])
                
    return answer


def solve():
    global tree_age, tree_food
    for _ in range(K):
        dead_tree=spring(tree_food,tree_age)
        summer(tree_food, dead_tree)
        fall(tree_age)
        winter(tree_food,A)
    result=survive_check(tree_age)

    return result

print(solve())