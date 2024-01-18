def solution(triangle):
    dp = triangle
    for i in range(1, len(dp)):
        for j in range(i+1): # 현재 행의 각 요소에 대해 순회
            if j == 0: # 맨 왼쪽 요소일 경우
                dp[i][j] += dp[i-1][j] # 바로 위의 요소만 더해줌
            elif j == i: # 맨 오른쪽 요소일 경우
                dp[i][j] += dp[i-1][j-1] # 왼쪽 위의 요소만 더해줌
            else: # 그 외의 경우
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j]) # 바로 위 요소와 왼쪽 위 요소 중 큰 값과 현재 요소 더함
    return max(dp[-1]) # 마지막 행의 최대값을 리턴