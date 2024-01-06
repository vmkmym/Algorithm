def solution(array, n):
    array.sort()
    closest_number = min(array, key=lambda x: abs(x - n))
    return closest_number
