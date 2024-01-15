import itertools

def solution(k, dungeons):
    # 모든 던전의 순서쌍을 생성
    orders = list(itertools.permutations(dungeons))

    max_dungeons = 0
    # 모든 순서쌍에 대해
    for order in orders:
        energy = k
        count = 0
        # 각 순서에 따라 던전을 탐험
        for dungeon in order:
            if energy >= dungeon[0]:  # 현재 피로도가 해당 던전의 최소 필요 피로도 이상이면
                energy -= dungeon[1]  # 해당 던전을 탐험하고 피로도를 갱신
                count += 1  # 탐험한 던전 수를 증가
            else:
                break  # 현재 피로도가 부족하면 더 이상 탐험할 수 없으므로 반복문을 종료
        max_dungeons = max(max_dungeons, count)  # 탐험한 던전 수가 현재 최대치보다 많으면 갱신

    return max_dungeons  # 모든 경우를 탐색한 후, 탐험한 던전 수가 가장 많은 경우를 반환

print(solution(80, [[80,20],[50,40],[30,10]])) # 3
print(solution(100, [[100,10],[100,10],[100,10]])) # 1
print(solution(100, [[30,10],[30,10],[30,10]])) # 3