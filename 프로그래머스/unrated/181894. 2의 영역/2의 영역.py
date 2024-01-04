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


# 다른 사람 풀이
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]