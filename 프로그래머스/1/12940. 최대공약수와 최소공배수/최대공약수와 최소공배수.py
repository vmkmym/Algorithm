import math

def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = n * m // gcd
    return [gcd, lcm]

# 왜 최소공배수는 메서드가 없지? 최대공약수로 만들 수 있어서 그런가?