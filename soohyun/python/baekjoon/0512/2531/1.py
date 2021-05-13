import sys
def main():
    start, end = 0, 0
    sushi_set = dict()
    sushi = list()
    max_length = 0
    N, d, k, c = map(int, sys.stdin.readline().rstrip().split(" "))
    for _ in range(N):
        sushi.append(int(sys.stdin.readline().rstrip()))

    while start < N:
        sushi_set[sushi[end%N]] = sushi_set.get(sushi[end%N], 0) + 1
        if end - start == k - 1:
            if max_length <= len(sushi_set):
                max_length = len(sushi_set) if c in sushi_set else len(sushi_set) + 1
            sushi_set[sushi[start]] -= 1
            if sushi_set[sushi[start]] <= 0:
                sushi_set.pop(sushi[start])
            start += 1
        end += 1
    print(max_length)
if __name__ == "__main__":
    main()