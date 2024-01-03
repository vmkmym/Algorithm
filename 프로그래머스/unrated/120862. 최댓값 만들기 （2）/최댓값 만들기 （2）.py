def solution(numbers):
    numbers.sort()

    case1 = numbers[-1] * numbers[-2]

    case2 = numbers[0] * numbers[1]
    
    case3 = numbers[0] * numbers[1]
    
    return max(case1, case2, case3)
