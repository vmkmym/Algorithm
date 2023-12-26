def solution(my_strings, parts):
    result = []
    
    for my_str, part in zip(my_strings, parts):
        s, e = part
        result.append(my_str[s:e + 1])

    return ''.join(result)

        
            