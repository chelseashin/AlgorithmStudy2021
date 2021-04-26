import math
#시작 2시 22분
#끝 4시 10분
def size(n):
    return len(str(n))


def bindfs(n, count):
    min_count = 100000000
    min_num = 100000000
    if size(n) <= 1:
        return count, n
    pow_num = 1
    while True:
        divider = int(math.pow(10.0, float(pow_num)))
        if int(n / divider) < 1:
            break
        if size(n % divider) < pow_num:  
            pow_num += 1
            continue
        acount , an = bindfs(int(n / divider) + n % divider, count + 1)
        if acount < min_count:
            min_count = acount
            min_num = an
        pow_num += 1
    return min_count, min_num


def solution(n):
    return bindfs(n, 0)


print("solution", solution(1234567899))
print("solution", solution(10007))
print("solution", solution(9))
