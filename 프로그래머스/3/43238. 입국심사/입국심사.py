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

'''
파이썬 이진 탐색 라이브러리
from bisect import bisect_left, bisect_right 
bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환 
bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
bisect_left는 cpp의 lower_bound와 같고, bisect_right는 cpp의 upper_bound와 같다.
'''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else: 
            start = mid + 1
    return None