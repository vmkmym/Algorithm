def solution(n):
    dp = [0] * (n+1) # 길이가 n이고 모든 원소가 0인 리스트 생성
    dp[1], dp[2] = 1, 2 if n > 1 else 1
    for i in range(3, n+1): # 3부터 n까지의 직사각형을 채우는 방법의 수를 구함
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007 
    return dp[n]