import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    time = list()
    for _ in range(N):
        time = int(sys.stdin.readline())
    result = 0
    left = 0
    right = M * max(time)


if __name__ == "__main__":
    print(main())