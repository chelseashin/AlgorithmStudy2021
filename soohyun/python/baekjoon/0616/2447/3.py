import sys
input = sys.stdin.readline
print = sys.stdout.write


def print_stars(arr):
    for row in arr:
        print(''.join(row)+"\n")


def stars(N):

    arr = [[' ']*N for _ in range(N)]
    row, col = 0, 0
    def recursive(N, row, col):
        print(str(row)+" "+str(col)+"\n")

        if N == 3:
            arr[row][col] = '*'
            arr[row][col+1] = '*'
            arr[row][col+2] = '*'
            arr[row+1][col] = '*'
            arr[row+1][col+2] = '*'
            arr[row+2][col] = '*'
            arr[row+2][col+1] = '*'
            arr[row+2][col+2] = '*'
            return
        recursive(N//3, row, col-1)
        recursive(N//3, row, col+1*N//3-1)
        recursive(N//3, row, col+2*N//3-1)

        recursive(N//3, row+1*N//3, col)
        recursive(N//3, row+1*N//3, col+1*N//3)

        recursive(N//3, row+2*N//3, col)
        recursive(N//3, row+2*N//3, col+2*N//3)
        recursive(N//3, row+2*N//3, col+3*N//3)
        return
    recursive(N, row, col)
    print_stars(arr)

def main():
    N = int(input().rstrip())
    stars(N)

if __name__ == "__main__":
    main()