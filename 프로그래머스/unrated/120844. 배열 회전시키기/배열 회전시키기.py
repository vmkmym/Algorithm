def solution(numbers, direction):
    n = len(numbers)
    return [numbers[n-1]] + numbers[:n-1] if direction == 'right' else numbers[1:] + [numbers[0]]