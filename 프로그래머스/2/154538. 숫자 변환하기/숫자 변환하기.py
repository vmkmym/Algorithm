def solution(x, y, n):
    MAX = 1000001
    dp = [0] + [MAX] * y
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] != MAX:
            if i + n <= y:
                dp[i + n] = min(dp[i + n], dp[i] + 1)
            if i * 2 <= y:
                dp[i * 2] = min(dp[i * 2], dp[i] + 1)
            if i * 3 <= y:
                dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    return dp[y] if dp[y] != MAX else -1