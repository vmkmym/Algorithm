def solution(order):
    count = sum(1 for d in str(order) if d in '369')
    return count