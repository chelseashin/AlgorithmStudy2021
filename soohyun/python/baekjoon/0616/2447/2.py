def print_data(data):
    for row in data:
        print(*row)

def solution(N):
    data = [[''] * N for _ in range(N)]

    def stars(row, col, is_blank):
        print(row, col)
        if row > 0 and col  > 0:
            for i in range(1, 4):
                for j in range(1, 4):
                    blank = is_blank
                    if (i,j) == (2,2):
                        blank=True
                    stars((i * row)//3, (j * col)//3, blank)
        else:
            return
        value = ' ' if is_blank else '*'
        data[row-1][col-1] = value
    stars(N, N, False)
    print_data(data)


def main():
    N = int(input())
    solution(N)

if __name__ == "__main__":
    main()