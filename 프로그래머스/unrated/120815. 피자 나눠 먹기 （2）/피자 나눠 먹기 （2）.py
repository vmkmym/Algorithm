import math

def solution(n):
    pizza = n * 6 // math.gcd(n, 6)
    return pizza // 6 