class Road():
    def __init__(self, cur_direct, count, money, prev_direct):
        self.cur_direct = cur_direct
        self.count = count
        self.money = money
        self.prev_direct = prev_direct


def solution(board):
    answer = 0
    N = len(board)
    min_money = 100000000000000000
    # cur_direct, count, money, prev_direct
    stack = [Road((0, 0), 0, 0, (0, 0))]
    visited = {(0,0):0}
    while len(stack):
        #cur_direct, count, money, prev_direct 
        road = stack.pop(0)

        for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nr = road.cur_direct[0] + dr
            nc = road.cur_direct[1] + dc
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc]==0:
                # 방문처리         
                pdr, pdc = road.prev_direct[0], road.prev_direct[1]
                if road.prev_direct == (0, 0) or (dr, dc) == road.prev_direct:
                    money = 100 + road.money
                else:
                    money = 600 + road.money
                if visited.get((nr, nc), float('inf')) > money:
                    visited[(nr, nc)] = money
                    stack.append(Road((nr, nc), road.count+1, money, (dr, dc)))
    return visited[(len(board)-1, len(board-1))]
print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
