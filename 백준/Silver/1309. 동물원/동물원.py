def zoo(n):
    dp = [[0]*3 for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        dp[i][0] = sum(dp[i-1]) % 9901
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

    return sum(dp[n]) % 9901

# 숏코딩
def zoo(n):
    a = b = c = 1
    for _ in range(n-1):
        a, b, c = (a+b+c)%9901, (a+c)%9901, (a+b)%9901
    return (a+b+c)%9901

try:
    print(zoo(int(input())))
except:
    print("Invalid input. Please enter a non-negative integer.")