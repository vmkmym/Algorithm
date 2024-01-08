def solution(arr, divisor):
    div_arr = []
    
    for i in arr:
        if i % divisor == 0:
            div_arr.append(i)
            
    return sorted(div_arr) if div_arr else [-1]