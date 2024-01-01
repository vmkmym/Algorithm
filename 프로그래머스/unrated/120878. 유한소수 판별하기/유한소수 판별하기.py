import math

def solution(a, b):
    c = b // math.gcd(a,b)
    
    while c % 2 == 0:
        c //= 2

    while c % 5 == 0:
        c //= 5
        
    return 1 if a == b or c == 1 else 2

# a와 b의 최대공약수로 b를 나눈 값을 c에 저장
# c를 2, 5로 나눈 나머지가 0일때까지 2, 5로 나눈 몫을 다시 할당하여 유한소수인지 판별

# 다른 사람 풀이
from math import gcd

def solution(a, b):
    b = b / gcd(a, b)
    
    for i in [2, 5]:
        while not b % i:
            b //= i

    return 1 if b == 1 else 2
