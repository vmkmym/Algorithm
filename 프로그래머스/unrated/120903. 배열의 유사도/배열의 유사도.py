def solution(s1, s2):
    count = 0
    
    for char in s1:
        if char in s2:
            count += 1
    
    return count