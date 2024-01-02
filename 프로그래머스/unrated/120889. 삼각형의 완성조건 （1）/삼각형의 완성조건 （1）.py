def solution(sides):
    max_side = max(sides)
    remain_side = sum(sides) - max_side
    return 1 if remain_side > max_side else 2
