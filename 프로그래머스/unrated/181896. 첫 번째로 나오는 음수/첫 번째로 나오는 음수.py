def solution(num_list):
    return next((idx for idx, num in enumerate(num_list) if num < 0), -1)

# next() 함수는 파이썬의 내장 함수 중 하나로, 이터레이터(iterator)에서 다음 값을 가져오는 역할을 합니다. 주로 이터레이터의 다음 항목을 반환하고, 만약 더 이상 항목이 없으면 기본값(default)을 반환하거나, 예외를 발생시키게 할 수 있습니다.
