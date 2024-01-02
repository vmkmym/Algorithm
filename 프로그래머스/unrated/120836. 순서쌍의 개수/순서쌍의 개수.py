def solution(n):
    count = 0
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1 if i * i == n else 2
            
    return count
