import sys
input = sys.stdin.readline
print = sys.stdout.write

def print_stars(arr):
    for row in arr:
        print(''.join(row)+"\n")


def make_star(N):
    arr = [[' '] * (2*N-1) for _ in range(N)]
    row, col = 0, N-1
    def recursive(row, col, N):
        if N == 3:
            arr[row][col] = '*'

            arr[row+1][col-1] = '*'
            arr[row+1][col+1] = '*'

            arr[row+2][col-2] = '*'
            arr[row+2][col-1] = '*'
            arr[row+2][col] = '*'
            arr[row+2][col+1] = '*'
            arr[row+2][col+2] = '*'
            return

        recursive(row, col, N//2)
        recursive(row + N//2, col + N//2, N//2)
        recursive(row + N//2, col - N//2, N//2)
        return
    recursive(row, col, N)
    print_stars(arr)


def main():
    N = int(input().rstrip())
    make_star(N)


if __name__ == "__main__":
    main()
