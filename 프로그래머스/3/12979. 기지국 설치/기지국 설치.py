import math

def solution(n, stations, w):
    answer = 0
    apt = 1 # 아파트의 시작 위치
    for station in stations:
        if station - w > apt:
            answer += math.ceil((station - w - apt) / (w*2 + 1))
        apt = station + w + 1
    if n >= apt: # 마지막 기지국 이후에 아파트가 남아있을 경우
        answer += math.ceil((n - apt + 1) / (w*2 + 1))
    return answer

# 기지국 하나가 커버할 수 있는 거리 w*2+1
# 기지국 사이의 거리 = 현재 기지국의 위치 - w - 다음 아파트의 위치
# 기지국 사이의 거리를 기지국이 커버할 수 있는 거리로 나눈 후 올림하기