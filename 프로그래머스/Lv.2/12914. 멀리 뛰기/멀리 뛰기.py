def solution(n):
    if n <= 2:
        return n
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
        return dp[n]

# 동적계획법.. 어렵다