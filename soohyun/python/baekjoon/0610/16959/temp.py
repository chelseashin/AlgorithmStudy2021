import sys
from collections import defaultdict
input = sys.stdin.readline
MOVE = {0: [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)], # 나이트
        1: [(1, 1), (-1, 1), (1, -1), (-1, -1)],  #비숍
        2: [(-1, 0), (0, -1), (1, 0), (0, 1)]} #룩


class ChessInfo():
    def __init__(self, start_piece, piece, loc, count, number):
        self.start_piece = start_piece
        self.piece = piece
        self.loc = loc
        self.count = count
        self.number = number

    def __str__(self):
        return f'{self.start_piece}, {self.piece}, {self.loc}, {self.count}'


def make_visit(num, N, start):
    result = dict()
    for i in range(num):
        location_dict = dict()
        for j in range(1, N*N+1):
            location_dict[j] = set()
        result[i] = location_dict
    result[0][2].add(start)
    result[1][2].add(start)
    result[2][2].add(start)
    return result


def is_in_range(nr, nc, N):
    if 0 <= nr < N and 0 <= nc < N:
        return True
    return False


def get_arrive_queue(queue, end, count):
    arr = []
    for chess_info in queue:
        #print("post queue", chess_info)
        if chess_info.loc == end and chess_info.count == count:
            arr.append(chess_info.piece)
        elif chess_info.count != count:
            break
    return arr


def bfs(start, N, num_loc):
    count = 0
    queue = list()
    visited = make_visit(3, N, start)
    #print(visited)

    queue = [ChessInfo(i, i, start, count, 2) for i in range(3)]
    #for q in queue:
    #    print("prequeue:", q)
    while queue:
        chess_info = queue.pop(0)
        #print(chess_info.number)
        if chess_info.number == N*N+1:
            return chess_info.count
        next_destination = num_loc[chess_info.number]

        # 말을 바꾸는 경우
        for i in range(3):
            next_piece = (chess_info.piece + 1 + i) % 3
            if chess_info.loc not in visited[next_piece][chess_info.number]:
                queue.append(ChessInfo(
                                    chess_info.start_piece,
                                    next_piece,
                                    chess_info.loc,
                                    chess_info.count + 1,
                                    chess_info.number
                                ))
                visited[next_piece][chess_info.number].add(chess_info.loc)
                #print("change append queue", queue[-1])

        # 말을 바꾸지 않고 진행하는 경우
        
        if chess_info.piece == 0:
            for i, j in MOVE[chess_info.piece]:
                nr = chess_info.loc[0] + i
                nc = chess_info.loc[1] + j
                if is_in_range(nr, nc, N):
                    if (nr, nc) not in visited[chess_info.piece][chess_info.number]:
                        visited[chess_info.piece][chess_info.number].add((nr, nc))
                        if nr == next_destination[0] and nc == next_destination[1]:
                            #print("correct")
                            queue.append(ChessInfo(
                                chess_info.start_piece,
                                chess_info.piece,
                                (nr, nc),
                                chess_info.count + 1,
                                chess_info.number + 1
                            ))
                        else:
                            queue.append(ChessInfo(
                                chess_info.start_piece,
                                chess_info.piece,
                                (nr, nc),
                                chess_info.count + 1,
                                chess_info.number
                            ))
        else: 
            for i, j in MOVE[chess_info.piece]:   
                for alpha in range(N):
                    nr = chess_info.loc[0] + i * alpha
                    nc = chess_info.loc[1] + j * alpha
                    if is_in_range(nr, nc, N):
                        if (nr, nc) not in visited[chess_info.piece][chess_info.number]:
                            visited[chess_info.piece][chess_info.number].add((nr, nc))
                            if nr == next_destination[0] and nc == next_destination[1]:
                                #print("correct")
                                queue.append(ChessInfo(
                                    chess_info.start_piece,
                                    chess_info.piece,
                                    (nr, nc),
                                    chess_info.count + 1,
                                    chess_info.number + 1
                                ))
                            else:
                                queue.append(ChessInfo(
                                    chess_info.start_piece,
                                    chess_info.piece,
                                    (nr, nc),
                                    chess_info.count + 1,
                                    chess_info.number
                                ))
                                #print("nonchange append queue", queue[-1])
                        
    return 0


def game(N, num_loc):
    result = 0
    result = bfs(num_loc[1], N, num_loc)
    #for i in range(1, N*N):
    #    start = num_loc[i]
    #    end = num_loc[i+1]
    #    #print("from:", i, start, "to:", i+1, end, "end_pieces", end_pieces)
    #    end_pieces, bfs_result = bfs(start, end, N, end_pieces)
    #    result += bfs_result
    #    #print("bfs_result:",bfs_result,"result:", result)
    return result


def main():
    N = int(input().rstrip())
    num_loc = dict()
    for i in range(N):
        for idx, j in enumerate(list(map(int, input().rstrip().split(" ")))):
            num_loc[j] = (i, idx)
    #print(num_loc)
    print(game(N,  num_loc))


if __name__ == "__main__":
    main()
