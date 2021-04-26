def solution(num):
    count = 0
    if num == 0:
        return 1
    elif num < 0:
        return 0
    count += solution(num-1)
    count += solution(num-2)
    count += solution(num-3)
    return count


def main():
    N = int(input())
    for idx in range(N):
        num = int(input())
        print(solution(num))


if __name__ == "__main__":
    main()
