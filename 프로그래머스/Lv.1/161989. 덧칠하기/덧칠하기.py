def solution(n, m, section):
    paint_count = 0
    max_val = 0
    
    for i in section:
        if i > max_val:
            paint_count += 1
            max_val = i + m - 1
            
    return paint_count