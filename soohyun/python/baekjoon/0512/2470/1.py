def main():
    N = int(input())
    liquids = list(map(int, input().rstrip().split(" ")))
    liquids.sort()
    start = 0
    min_result = float('inf')
    idx_list = (0, 0)
    end = len(liquids) - 1
    #print(liquids)
    while start < end:
        result = liquids[end] + liquids[start]
        if min_result > abs(result):
            min_result = abs(result)
            idx_list = (liquids[start], liquids[end])
        if result < 0:
            start += 1
        elif result > 0:
            end -= 1
        else:
            idx_list = (liquids[start], liquids[end])
            break
    print(idx_list[0], idx_list[1])#, min_result)


if __name__ == "__main__":
    main()