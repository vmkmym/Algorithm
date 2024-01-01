import math

def solution(a, b):
    c = b // math.gcd(a,b)
    
    while c % 2 == 0:
        c //= 2

    while c % 5 == 0:
        c //= 5
        
    return 1 if a == b or c == 1 else 2
        
