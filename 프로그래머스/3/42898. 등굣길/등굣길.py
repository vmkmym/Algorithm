def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1 # 시작 좌표
    
    for p in puddles:
        dp[p[1]][p[0]] = -1
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1 or dp[i][j] == -1: # 시작 좌표이거나 웅덩이인 경우
                continue
            if dp[i - 1][j] != -1: # 위쪽이 웅덩이가 아닌 경우
                dp[i][j] += dp[i - 1][j]
            if dp[i][j - 1] != -1: # 왼쪽이 웅덩이가 아닌 경우
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= 1000000007

    return dp[n][m]