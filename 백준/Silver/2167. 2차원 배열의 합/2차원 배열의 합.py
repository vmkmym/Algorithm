import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 기준 배열
k = int(sys.stdin.readline())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] 
        
for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    print(dp[i-1][j-1] - dp[i-1][y] - dp[x][j-1] + dp[x][y])