def solution(n, times):
    low = 1
    high = max(times) * n  # 최악의 경우, 가장 오래 걸리는 심사관에게 모두 심사받는 경우를 상정
    result = high
    while low <= high:
        mid = (low + high) // 2
        total = sum(mid // time for time in times)  # mid 시간 동안 심사할 수 있는 사람의 수
        if total < n:  # 심사받지 못한 사람이 있다면
            low = mid + 1 # 시간을 늘려서 더 많은 사람을 심사받게 함
        else:  # 모든 사람이 심사받았다면
            high = mid - 1 # 시간을 줄여서 더 적은 사람을 심사받게 함
            result = min(result, mid)  # 최소 시간을 갱신
    return result