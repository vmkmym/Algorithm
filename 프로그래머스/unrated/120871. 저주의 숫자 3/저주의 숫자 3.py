def solution(n):
    num = 0
    
    for i in range(n):
        num += 1
        while num % 3 == 0 or "3" in str(num):
            num += 1
            
    return num