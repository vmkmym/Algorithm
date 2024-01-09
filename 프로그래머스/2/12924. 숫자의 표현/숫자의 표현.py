def solution(n):
    count = 0
    
    for i in range(1, n+1):
        total = 0
        
        for j in range(i, n+1):
            total += j
            
            if total == n:
                count += 1
                break
            elif total > n:
                break
                
    return count

# 한 번씩 순회해
# 누적해서 더한 값이 자연수 n이면 count