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

# 다른 사람 풀이
import math

def solution(balls, share):
    return math.comb(balls, share)

# `math.comb(n, k)` 함수는 파이썬의 `math` 모듈에 포함된 함수로, 조합(Combination)을 계산하는 함수입니다. 
# 이 함수는 주어진 `n`개의 항목 중에서 `k`개의 항목을 선택할 때 발생하는 경우의 수를 계산합니다. 
# 이때, 중복이 없고 순서가 없는 경우의 수를 계산합니다.

# - `n! / (k! * (n - k)!)`의 수식으로 표현됩니다. 여기서 `n!`은 `n` 팩토리얼이며, `n`부터 1까지의 모든 자연수를 곱한 값을 의미합니다.
# - `k`가 `n`보다 작거나 같을 때는 계산이 되며, `k`가 `n`보다 클 때는 0을 반환합니다. 이는 조합을 할 수 없는 경우를 의미합니다.
# - 이 함수는 정수가 아닌 값을 받거나, 음수 값을 받을 경우 `TypeError` 또는 `ValueError`를 발생시킵니다.
# - 또한, 이 함수는 다항식 `(1 + x)ⁿ`의 k번째 항의 계수와 동일하다는 점에서 이항 계수(binomial coefficient)라고도 불립니다.

# 간단히 말해, 주어진 `n`개의 항목 중에서 `k`개의 항목을 순서와 상관없이 고를 때의 경우의 수를 계산하는 함수입니다.
