class Tile():
    def __init__(self, N, row, col):
        self.N = N
        self.num = 0
        self.tile = [[0]*N for _ in range(N)]
        self.tile[row][col] = -1
    
    def recursive(self, row, col, size):
        self.num += 1
        next_size = size//2
        #print(self.tile)
        if self.check(row, col, next_size): 
            self.tile[row+next_size-1][col+next_size-1] = self.num

        if self.check(row+next_size, col, next_size):
            self.tile[row+next_size][col+next_size-1] = self.num

        if self.check(row, col+next_size, next_size):
            self.tile[row+next_size-1][col+next_size] = self.num

        if self.check(row+next_size, col+next_size, next_size):
            self.tile[row+next_size][col+next_size] = self.num

        if(size==2):
            return

        self.recursive(row, col, next_size)
        self.recursive(row+next_size, col, next_size)
        self.recursive(row, col+next_size, next_size)
        self.recursive(row+next_size, col+next_size, next_size)
        

    def check(self, row, col, size):
        for i in range(row, size+row):
            for j in range(col, size+col):
                if self.tile[i][j] != 0:
                    return False
        return True

    def print_tile(self):
        for i in range(self.N-1, 0, -1):
            result = [str(self.tile[i][j]) for j in range(1, self.N)]
            print(' '.join(result))
            #for j in range(1, self.N):
            #    result.append()



def main():
    N = int(input().rstrip())
    col, row = map(int, input().rstrip().split(" "))
    tile = Tile((2**N)+1, row, col)
    tile.recursive(1, 1, (2**N))
    tile.print_tile()


if __name__ == "__main__":
    main()