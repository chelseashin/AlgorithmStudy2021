


def make_dp():
    dp = [0 for _ in range(2501)]
    dp[0], dp[1] = 1, 1
    for i in range(2, 2501):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
        dp[i] %= 1000000007
    return dp

def main():
    dp = make_dp()
    print(dp[0:10])
    for _ in range(int(input().rstrip())):
        num = int(input().rstrip())
        if num % 2 !=0:
            print(0)
        else:
            print(dp[num//2] % 1000000007)


if __name__ == "__main__":
    main()