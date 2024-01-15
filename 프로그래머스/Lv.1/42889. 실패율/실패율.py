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

# 이건 시간복잡도 O(N^2)이라서 효율성 테스트가 있었으면 시간초과가 뜰 것 같음.
# 개선한 코드는 시간 복잡도는 O(N log N), 제출 코드보다 훨씬 효율적임.
def solution(N, stages):
    player_failure = [0] * (N + 2) # 0 ~ N + 1
    for stage in stages: # stage 1 ~ N
        player_failure[stage] += 1  # stage_count[1] ~ stage_count[N]

    player_success = len(stages) 
    failure_rate = []
    for i in range(1, N + 1):
        if player_success == 0:
            failure_rate.append((i, 0))
        else:
            failure_rate.append((i, player_failure[i] / player_success))
            player_success -= player_failure[i]

    failure_rate.sort(key=lambda x: (-x[1], x[0]))

    return [x[0] for x in failure_rate]