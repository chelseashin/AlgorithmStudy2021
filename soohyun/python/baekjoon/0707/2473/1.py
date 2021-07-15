import sys
import math
input = sys.stdin.readline

def find_min(idx, liquid, N):
    s_value = liquid[idx]
    end = N-1
    start = idx+1
    min_sum = math.inf
    min_value = [0, 0, 0]

    while start < end:
        lsum = s_value + liquid[start] + liquid[end]
        if min_sum > abs(lsum):
            min_sum = abs(lsum)
            min_value[0] = liquid[idx]
            min_value[1] = liquid[start]
            min_value[2] = liquid[end]
        if lsum > 0:
            end -= 1
        else:
            start += 1
    if min_value[0] == 0 and min_value[1] == 0 and min_value[0] == 0:
        return [-1, -1 ,-1]
    return min_value


def find_zero(N, liquid):
    min_diff = math.inf
    min_liquid = list()
    for idx, _ in enumerate(liquid):
        min_value = find_min(idx, liquid, N)
        if min_value[0] == min_value[1] == min_value[2] == -1:
            continue
        if min_diff > abs(sum(min_value)):
            min_diff = abs(sum(min_value))
            min_liquid = min_value
    return map(str, min_liquid)


def main():
    N = int(input().rstrip())
    liquid = sorted(list(map(int, input().rstrip().split(" "))))
    #print(liquid)
    print(' '.join(find_zero(N, liquid)))


if __name__ == "__main__":
    main()