

def count_turn_on(hutgan, N):
    pass


def main():
    N, M = map(int, input().rstrip().split(" "))
    hutgan = defaultdict(list)
    for _ in range(M):
        start_r, start_c, end_r, end_c = \
            map(int, input().rstrip().split(" "))
        hutgan[(start_r-1, start_c-1)].append((end_r-1, end_c-1))
    print(count_turn_on(hutgan, N))


if __name__ == "__main__":
    main()