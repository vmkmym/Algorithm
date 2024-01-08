def solution(numbers):
    zero_nine = list(range(10))
    return sum(i for i in zero_nine if i not in numbers)