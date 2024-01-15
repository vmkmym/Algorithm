def solution(k, dungeons):
    # 던전을 최소 필요 피로도를 기준으로 내림차순 정렬
    dungeons.sort(reverse=True)

    # 탐험 가능한 최대 던전 수를 저장할 변수
    max_dungeons = 0

    # 재귀 함수를 정의합니다. 이 함수는 현재 피로도, 탐험한 던전 수, 현재 던전 인덱스를 인자로 받습니다.
    def explore(energy, count, visited):
        nonlocal max_dungeons  # 외부 스코프의 변수를 참조

        # 탐험한 던전 수가 현재 최대치보다 많으면 갱신
        max_dungeons = max(max_dungeons, count)

        # 모든 던전에 대해
        for i in range(len(dungeons)):
            # 이미 탐험한 던전은 건너뛴다.
            if i in visited:
                continue

            # 현재 피로도가 해당 던전의 최소 필요 피로도 이상이면
            if energy >= dungeons[i][0]:
                # 해당 던전을 탐험하고 피로도를 갱신하여 재귀 호출
                explore(energy - dungeons[i][1], count + 1, visited | {i})

    # 처음에는 피로도 k, 탐험한 던전 수 0, 방문한 던전 없음으로 시작
    explore(k, 0, set())

    # 모든 경우를 탐색한 후, 탐험한 던전 수가 가장 많은 경우를 반환
    return max_dungeons