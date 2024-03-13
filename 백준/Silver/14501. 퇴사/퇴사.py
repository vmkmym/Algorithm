N = int(input()) # 퇴사하기까지 남은 일수
T = [] # 상담을 완료하는데 걸리는 기간
P = [] # 받을 수 있는 금액

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
dp = [0] * (N+1) # 날짜별 최대 수익 저장, 0으로 초기화
for i in range(N-1, -1, -1):
    if i + T[i] <= N: # 상담을 할 수 있는 경우
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]]) # dp[i]일까지 얻는 최대 수익
    else: # 상담을 할 수 없는 경우
        dp[i] = dp[i+1] # 다음 상담으로 넘어감
        
print(dp[0]) 