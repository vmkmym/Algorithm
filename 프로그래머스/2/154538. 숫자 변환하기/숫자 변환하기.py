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

# dp, 메모이제이션 (Memoization)
# 메모이제이션은 이미 계산된 결과를 저장해두고, 나중에 재사용하는 기법 (중복 계산을 피함)
'''
dp 배열은 각 인덱스 i에 대해 x에서 i로 변환하는 데 필요한 최소 연산 횟수를 저장합니다. 
이 값은 dp[i + n], dp[i * 2], dp[i * 3]을 계산할 때 재사용됩니다.

예를 들어, dp[i + n]을 계산할 때, dp[i] + 1과 기존에 dp[i + n]에 저장된 값을 비교하여 더 작은 값을 dp[i + n]에 저장합니다. 
이렇게 하면 i + n을 만드는 데 필요한 최소 연산 횟수를 dp[i + n]에 저장할 수 있습니다.

이런 식으로 이미 계산된 dp[i]의 값을 재사용하므로, 
메모이제이션을 통해 중복 계산을 피하고 프로그램의 성능을 향상시킬 수 있습니다. 
이는 다이나믹 프로그래밍의 핵심 기법 중 하나입니다.
'''