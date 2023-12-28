def solution(numlist, n):
    return sorted(numlist, key = lambda i: (abs(i - n), -i))

# 정수 리스트를 받아서 n과의 거리 비교 : 각 요소에서 n 뺀 절댓값, 거리가 같은 경우 음의 값으로 크기 비교 후 정렬
