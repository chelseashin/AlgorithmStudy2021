import sys
from collections import defaultdict
input = sys.stdin.readline
MOVE = {0: [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)], # 나이트
        1: [(1, 1), (-1, 1), (1, -1), (-1, -1)],  #비숍
        2: [(-1, 0), (0, -1), (1, 0), (0, 1)]} #룩


class ChessInfo():
    def __init__(self, start_piece, piece, loc, count):
        self.start_piece = start_piece
        self.piece = piece
        self.loc = loc
        self.count = count

    def __str__(self):
        return f'{self.start_piece}, {self.piece}, {self.loc}, {self.count}'


def make_visit(num, start):
    result = defaultdict(set)
    for i in range(num):
        result[i].add(start)
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


def bfs(start, end, N, start_pieces):
    count = 0
    queue = list()
    visited = defaultdict(set)

    if len(start_pieces) == 0:
        visited = make_visit(3, start)
        queue = [ChessInfo(i, i, start, count) for i in range(3)]
    else:
        for start_piece in start_pieces:
            visited[start_piece].add(start)
            queue.append(ChessInfo(start_piece, start_piece, start, count))
    #for q in queue:
    #    print("prequeue:", q)

    while queue:
        chess_info = queue.pop(0)
        #print("POPPED queue", chess_info)
        if chess_info.loc == end:
            arrive_queue = [chess_info.piece]
            arrive_queue.extend(get_arrive_queue(queue, end, chess_info.count))
            return arrive_queue, chess_info.count

        # 말을 바꾸는 경우
        for i in range(3):
            next_piece = (chess_info.piece + 1 + i) % 3
            if chess_info.loc not in visited.get(next_piece, {}):
                queue.append(ChessInfo(
                                    chess_info.start_piece,
                                    next_piece,
                                    chess_info.loc,
                                    chess_info.count + 1
                                ))
                visited[next_piece].add(chess_info.loc)
                #print("change append queue", queue[-1])

        # 말을 바꾸지 않고 진행하는 경우
        for i, j in MOVE[chess_info.piece]:
            for alpha in range(N):
                nr = chess_info.loc[0] + i * alpha
                nc = chess_info.loc[1] + j * alpha
                if is_in_range(nr, nc, N):
                    if (nr, nc) not in visited[chess_info.piece]:
                        visited[chess_info.piece].add((nr, nc))
                        queue.append(ChessInfo(
                            chess_info.start_piece,
                            chess_info.piece,
                            (nr, nc),
                            chess_info.count + 1
                        ))
                        #print("nonchange append queue", queue[-1])
    return 0, 0


def game(N, num_loc):
    result = 0
    end_pieces = []
    for i in range(1, N*N):
        start = num_loc[i]
        end = num_loc[i+1]
        #print("from:", i, start, "to:", i+1, end, "end_pieces", end_pieces)
        end_pieces, bfs_result = bfs(start, end, N, end_pieces)
        result += bfs_result
        #print("bfs_result:",bfs_result,"result:", result)
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
