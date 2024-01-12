def solution(a, b, n):
    bottle = 0
    
    while a <= n:
        bottle += (n // a) * b
        n = (n // a) * b + (n % a)
    
    return bottle