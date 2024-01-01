from itertools import combinations

# 조합 라이브러리
def solution(balls, share):
    ball = list(range(1, balls + 1))
    return len(list(combinations(ball, share)))

# 라이브러리 안 쓰고
def factorial(balls):
    if balls == 0 or balls == 1:
        return 1
    else:
        return balls * factorial(balls - 1)

def solution(balls, share):
    return factorial(balls) // (factorial(share) * factorial(balls - share))
