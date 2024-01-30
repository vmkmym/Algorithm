def solution(x, y, n):
    dp = [0] * (y + 1)
    dp[x] = 1

    for i in range(x + 1, y + 1):
        dp[i] = min(dp[i - n], dp[i // 2], dp[i // 3]) + 1 if i % 2 == 0 or i % 3 == 0 else dp[i - n] + 1

    return dp[y] if dp[y] != 0 else -1