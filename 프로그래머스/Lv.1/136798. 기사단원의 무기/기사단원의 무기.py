def solution(number, limit, power):
    numbers = [count_divisors(i) for i in range(1, number+1)]
    for i in range(len(numbers)):
        if numbers[i] > limit:
            numbers[i] = power  
    return sum(numbers)

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2 if n // i != i else 1    
    return count