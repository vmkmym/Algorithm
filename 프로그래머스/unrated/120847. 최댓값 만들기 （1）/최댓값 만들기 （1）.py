def solution(numbers):
    m = max(numbers)
    numbers.remove(m)
    n = max(numbers)
    return m*n