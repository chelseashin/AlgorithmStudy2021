# 걸린시간 1시간 30분
import sys
import math

def next_permutation(words):
    number = list(words)
    #find not decrease idx from end
    last_num = number[-1]
    change_idx = len(number) - 1
    is_change = False
    for i in range(len(number)-2, -1, -1):
        if last_num > number[i]:
            change_idx = i
            is_change = True
            break
        last_num = number[i]

    if is_change:
        compare_idx = 0
        # find min diff
        min_diff = math.inf
        for i in range(len(number)-1, change_idx, -1):
            diff = ord(number[i]) - ord(number[change_idx])
            if diff > 0 and diff < min_diff:
                compare_idx = i
                min_diff = diff
        # swap
        number[change_idx], number[compare_idx] = \
            number[compare_idx], number[change_idx]
        # reverse substring
        number[change_idx+1:len(number)] =\
                        number[change_idx+1:len(number)][::-1]
    return number
    

def main():
    words = ''
    N, M, K = map(int, input().rstrip().split(" "))
    words = ['a' for _ in range(N)]
    for _ in range(M):
        words.append('z')
    print(words)
    for _ in range(K-1):
        words = next_permutation(words)
    print(words)

    print(''.join(words))


if __name__ == "__main__":
    main()