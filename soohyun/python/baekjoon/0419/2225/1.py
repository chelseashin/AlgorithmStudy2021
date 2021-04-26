import sys


def main():
    N, K = map(int, sys.stdin.readline().rstrip().split(" "))
    data = list()
    if K < 2:
        return 1
    else:
        data = list(range(1, N+2))
        while K > 2:
            for i in range(1, len(data)):
                data[i] = (data[i]%1000000000)+(data[i-1]%1000000000)
            K -= 1
        #print(data)
        return data[N]%1000000000


if __name__ == "__main__":
    print(main())
