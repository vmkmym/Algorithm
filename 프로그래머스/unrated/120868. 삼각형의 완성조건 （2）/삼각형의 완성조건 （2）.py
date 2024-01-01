def solution(sides):
    sides.sort()
    return sum(1 for i in range(1, sum(sides)) if sides[1] < sides[0] + i)

