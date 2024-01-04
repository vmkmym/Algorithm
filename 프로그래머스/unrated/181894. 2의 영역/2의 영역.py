def solution(arr):
    # 2가 없을 때
    if arr.count(2) < 1:
        return [-1]
    
    # 2가 하나일 때
    if arr.count(2) < 2:
        return [2]

    # 2가 2개 이상일 때
    first_index = arr.index(2)
    last_index = arr[::-1].index(2)
    last_index = len(arr) - last_index 

    return arr[first_index:last_index]