def solution(num_list):
    if 20 >= len(num_list) >= 11:
        return sum(num_list)
        
    elif 2 <= len(num_list) <= 10:
        result = 1
        
        for num in num_list:
            result *= num
            
        return result

    