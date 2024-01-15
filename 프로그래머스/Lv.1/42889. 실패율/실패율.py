def solution(N, stages):
     # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    failure_rate = []
    for i in range(1, N+1):
        try:
            player_failure = stages.count(i) # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
            player_success = len([x for x in stages if x >= i]) # 스테이지에 도달한 플레이어 수
            failure_rate.append((i, player_failure / player_success)) # (스테이지 번호, 실패율)
        except ZeroDivisionError:
            failure_rate.append((i, 0))

    failure_rate.sort(key=lambda x: (-x[1], x[0])) # 실패율 내림차순 정렬 후 같다면 스테이지 번호 오름차순 정렬

    return [x[0] for x in failure_rate]