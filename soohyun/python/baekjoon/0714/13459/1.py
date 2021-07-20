from collections import deque
class Marble:
    def __init__(self, N, M, board, red, blue, out):
        self.board = board
        self.N = N
        self.M = M
        self.red = red
        self.blue = blue
        self.out = out

    def print_board(self, red, blue):
        for i, row in enumerate(self.board):
            for j, _ in enumerate(row):
                if (i,j) == red:
                    print('R', end="")
                elif (i, j) == blue:
                    print("B", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    def move_marble(self, start, other, direction):
        row, col = start[0], start[1]
        while True:
            if self.board[row][col] == '#':
                #print("#")
                #self.board[row-direction[0]][col-direction[1]] = shape
                return (row-direction[0], col-direction[1])
            elif (row, col) == self.out:
                #print("out!")
                return (row, col)
            elif (row, col) == other:
                #print("other", other)
                #self.board[row-direction[0]][col-direction[1]] = shape
                return (row-direction[0], col-direction[1])
            row += direction[0]
            col += direction[1]

    def is_red_first(self, red, blue, dr, dc):
        if dr != 0:
            if dr > 0:
                if red[0] > blue[0]: return True
            else:
                if red[0] < blue[0]: return True
        else:
            if dc > 0:
                if red[1] > blue[1]: return True
            else:
                if red[1] < blue[1]: return True
        return False

    def start_game(self):
        self.board[self.blue[0]][self.blue[1]] = '.'
        self.board[self.red[0]][self.red[1]] = '.'
        visited = set()
        visited.add((self.red[0],self.red[1],self.blue[0],self.blue[1]))
        queue = deque([(self.red, self.blue, 0)])
        while queue:
            red, blue, count = queue.popleft()
            #if red == self.out:
            #    return 1
            if count > 10:
                return 0
            for dr, dc in zip([-1, 1, 0, 0], [0, 0, -1, 1]):  
                if self.is_red_first(red, blue, dr, dc):
                    nred = self.move_marble(red, blue, (dr, dc))
                    nblue = self.move_marble(blue, nred, (dr, dc))
                else:
                    nblue = self.move_marble(blue, red, (dr, dc))   
                    nred = self.move_marble(red, nblue, (dr, dc))
                if nred == self.out and nblue == self.out:
                    continue
                if nblue == self.out:
                    continue

                else:
                    if (nred[0],nred[1],nblue[0],nblue[1]) not in visited:
                        visited.add((nred[0],nred[1],nblue[0],nblue[1]))
                        queue.append((nred, nblue, count+1))
        return 0

def main():
    N, M = map(int, input().rstrip().split(" "))
    board = list()
    blue = tuple()
    red = tuple()
    out = tuple()
    for i in range(N):
        row = list(input().rstrip())
        board.append(row)
        for idx, j in enumerate(row):
            if j == 'B':
                blue = (i, idx)
            elif j == 'R':
                red = (i, idx)
            elif j == 'O':
                out = (i, idx)
    game = Marble(N, M, board, red, blue, out)
    print(game.start_game())

if __name__ == "__main__":
    main()