def solution(n):
    remainder = []
    
    for i in range(1, n+1):
        if n % i == 1:
            remainder.append(i)
            
    return min(remainder)

# 답이 항상 존재함은 증명될 수 있습니다. 
# 문제 설명 뭔가 특이...