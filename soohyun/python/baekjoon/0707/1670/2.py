def main():
    N = int(input())
    dp = [0 for _ in range(10005)]
    dp[0] = 1
    for i in range(2, N+1, 2):
        dp[i] = 0
        for j in range(0, i, 2):
            dp[i] = (dp[i] + (1 * dp[j] * dp[i-j-2]) % 987654321) % 987654321
    print(dp[N])


if __name__ == "__main__":
    main()