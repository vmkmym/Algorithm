# 입력 변수 N, M, K, T가 누락되어 있으므로 가정하에 추가합니다.
N, M, K, T = map(int, input().split())

def solve_advent_ceremony():
    prayer_count = [0] * (N + 1)  # 인덱스 범위 오류 수정: N + 2에서 N + 1로 변경
    
    # 신도들의 기도 시작과 종료 시각 입력 받기
    for _ in range(M):
        start, end = map(int, input().split())
        for i in range(start, end + 1):  # 기도 종료 시각 포함 수정: end에서 end + 1로 변경
            prayer_count[i] += 1
    
    # DP 테이블 초기화
    # dp[i][j]: i번째 시각까지 j명의 친구를 사용했을 때 최대 강림 시간
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # DP 계산
    for i in range(1, N + 1):
        for j in range(K + 1):
            # 이전 상태 그대로 가져오기
            dp[i][j] = dp[i - 1][j]
            
            current_prayers = prayer_count[i]
            if current_prayers >= T:
                # 신도만으로 충분한 경우
                dp[i][j] = dp[i - 1][j] + 1
            elif current_prayers < T and j > 0:
                # 친구를 추가하여 T명 이상이 되는 경우
                friends_needed = min(T - current_prayers, j)
                if current_prayers + friends_needed >= T:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - friends_needed] + 1)
    
    # 최대 강림 시간 찾기
    max_descent_time = max(dp[N])
    
    return max_descent_time

# 문제 해결 및 결과 출력
print(solve_advent_ceremony())