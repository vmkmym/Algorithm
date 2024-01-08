def solution(n):
    factors = []
    
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
            
    return sum(factors)

# 약수는 주어진 수를 1과 자기 자신으로 나누어 떨어지게 하는 수