def solution(num):
    collatz_count = 0
    
    while num != 1:
        num = num // 2 if num % 2 == 0 else 3 * num + 1
        collatz_count += 1
        
    return collatz_count if collatz_count < 501 else -1