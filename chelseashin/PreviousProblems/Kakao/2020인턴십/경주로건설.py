# 으아아ㅏㅏㅏㅏ 절반 이상의 tc가 틀린다. 
# 문제 자체를 완전 잘못 접근한 것 같다.

from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def solution(board):
    answer = 0
    minCost = float('inf')
    N = len(board)
    for sr, sc, sd, sm in [(1, 0, 1, 100), (0, 1, 3, 100)]:
        visited = [[float('inf')] * N for _ in range(N)]
        visited[0][0] = 0
        visited[sr][sc] = 100
        Q = deque([(sr, sc, sd, sm)])
        while Q:
            r, c, d, cost = Q.popleft()
            if (r, c) == (N-1, N-1): 
                # print("도차아아아악", cost)
                minCost = min(minCost, cost)
                break
            for nd in range(4):
                nr = r + dr[nd]
                nc = c + dc[nd]
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc]:  # 격자 밖이면
                    continue
                temp = 0
                if d == nd: temp = 100
                else: temp = 600
                # 첫 방문이거나 갱신할 수 있을 때에만
                if  visited[nr][nc] == float('inf') or visited[nr][nc] > visited[r][c] + temp:
                    visited[nr][nc] = visited[r][c] + temp
                    Q.append((nr, nc, nd, cost+temp))
        #             print((r, c, d, cost), ">>>>", (nr, nc, nd, cost+temp))
        # for row in visited:
        #     print(row)
        # print("minCost", minCost)
        # print()
    return minCost

# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))