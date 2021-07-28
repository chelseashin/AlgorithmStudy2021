import sys
from collections import deque
input = sys.stdin.readline

class CircleBoard():
    def __init__(self, row, col, board, rotation):
        self.row = row
        self.col = col
        self.board = board
        self.rotation = rotation

    def rotate(self, multiple, direction, count):
        #print("clockwise", multiple, count) if direction == 0 else print("counter clockwise", multiple, count)
        for i in range(multiple-1, self.row, multiple):
            row_copy = [value for value in self.board[i]]
            for idx, value in enumerate(row_copy):
                count = count % self.col
                if direction == 0:
                    self.board[i][(count+idx)%self.col] = value
                #    self.rotation[i] = (self.col + (self.rotation[i] - (count % self.col))) % self.col
                elif direction == 1:
                    self.board[i][(self.col + idx - count)%self.col] = value
                #    self.rotation[i] = (self.rotation[i] + count) % self.col
        #self.print_board()

    def bfs(self, i, j):
        queue = deque([(i, j)])
        #visited[i][j] = True
        num = self.board[i][j]
        count = 0
        while queue:
            r, c = queue.popleft()
            for dr, dc, in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                nr, nc = r + dr, c + dc
                if dr == 0:
                    nr, nc = r + dr, (c + dc + self.col) % self.col
                if 0 <= nr < self.row and 0 <= nc < self.col:
                    if self.board[nr][nc] != 0 and self.board[nr][nc] == num:
                        #print(r, c, nr, nc, dr, dc)
                        self.board[r][c] = 0
                        self.board[nr][nc] = 0
                        queue.append((nr, nc))
                        count += 1
        return count


    def print_board(self):
        print("=====start===")
        for row in self.board:
            print(*row)
        print("=====end====")


    def find_adjacement(self):
        #visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        count = 0
        num_element = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] != 0:
                    count += self.bfs(i, j)
                    num_element += 1
        #print("remove start")
        #self.print_board()
        #print("remove end", count, num_element)
        
        if not count and num_element != 0:
            avg = self.calc_pan() / num_element
            for i in range(self.row):
                for j in range(self.col):
                    if self.board[i][j] != 0:
                        if self.board[i][j] > avg:
                            self.board[i][j] -= 1
                        elif self.board[i][j] < avg:
                            self.board[i][j] += 1
            #print("no cout")
            #self.print_board()
            #print("no count end")


    def calc_pan(self):
        result = 0
        for row in self.board:
            result += sum(row)
        return result


def inputs():
    return map(int, input().rstrip().split(" "))


def input_circle():
    pan = list()
    row, col , time = inputs()
    rotation = [0 for _ in range(row)]
    for _ in range(row):
        pan.append(list(inputs()))
    return CircleBoard(row, col, pan, rotation), time


def input_time(time):
    for _ in range(time):
        x, d, k = inputs()
        yield x, d, k


def main():
    circle, time = input_circle()
    for multiple, direction, count in input_time(time):
        circle.rotate(multiple, direction, count)
        circle.find_adjacement()
    print(circle.calc_pan())



if __name__ == "__main__":
    main()
