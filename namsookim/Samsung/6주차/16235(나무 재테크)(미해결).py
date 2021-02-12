# https://www.acmicpc.net/problem/16235
# 1:21 시작
# 1:57 중단
# 2:05 시작
# 2:59 종료 (시간초과)
# 3:44 종료
# 2시간 23분 소요(시간초과)
# 2시간 42분 시간초과

"""
10%에서 시간초과
"""
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
R = len(tree)
C = len(tree[0])
tree_info = dict()


for _ in range(M):
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)
    tree_info.setdefault((x-1,y-1),1)

def spring(land,tree,tree_info):
    dead_tree = []

    global R,C
    # 번식할 나무
    spread_tree = []

    del_index_tree = []

    # 나무가 자기 나이만큼 양분 먹고 나이 1증가
    for x, y in tree_info.keys():
        last = tree_info[(x, y)]
        for _ in range(last):
            age=tree[x][y].pop()
            if land[x][y] >= age:
                tree[x][y].insert(0,age+1)
                land[x][y] -= age
                if (age+1)%5 == 0:
                    spread_tree.append((x,y))

            else:
                dead_tree.append((x,y,age))
                tree_info[(x,y)] -= 1
                if tree_info[(x,y)] == 0:

                    del_index_tree.append((x,y))

    for tx,ty in del_index_tree:
        del tree_info[(tx,ty)]

    return spread_tree,dead_tree

def summer(land,dead_tree):
    # 죽은 나무가 양분으로 변함. 죽은 나무의 나이를 2로 나눈 값을 양분에 추가 소수점은 버림
    while dead_tree:
        x,y,age=dead_tree.pop()
        land[x][y] += age//2


def fall(tree,spread_tree,tree_info):
    global R,C
    global A

    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]

    for x,y in spread_tree:
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < R and 0 <= ny < C:
                tree[nx][ny].append(1)
                if tree_info.get((nx, ny)) == None:
                    tree_info[(nx, ny)] = 1
                else:
                    tree_info[(nx, ny)] += 1

def winter(land):
    global A
    # 각 칸에 추가되는 양분의 양 A[r][c] 만큼 추가 (입력으로 주어짐)

    for i in range(R):
        for j in range(C):
            land[i][j] += A[i][j]


def check(tree_info):
    global R,C

    answer = 0

    for x in tree_info.values():
        answer +=x

    return answer

def solve(tree):
    global R,C
    land = [[5]*R for _ in range(C)]


    for k in range(K):

        # spring
        spread_tree,dead_tree= spring(land,tree,tree_info)
        # summer
        summer(land,dead_tree)
        # fall
        fall(tree, spread_tree, tree_info)
        # winter
        winter(land)
        #winter(land)


    answer=check(tree_info)
    return answer

print(solve(tree))