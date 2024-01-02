def solution(a, b):
    odd_a = a % 2 != 0
    odd_b = b % 2 != 0
    
    if odd_a and odd_b:
        return a**2 + b**2
    elif odd_a or odd_b:
        return (a + b) * 2
    else:
        return abs(a - b)
