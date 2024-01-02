def solution(strArr):
    result = []
    
    for i, word in enumerate(strArr):
        if i % 2 == 0:
            result.append(word.lower())
        else: 
            result.append(word.upper())
            
    return result
