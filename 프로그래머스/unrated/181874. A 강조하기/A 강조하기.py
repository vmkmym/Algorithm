def solution(myString):
    answer = ''
    
    for char in myString:
        if char == "a":
            answer += "A"
        elif char != "A" and char.isupper():
            answer += char.lower()
        else:
            answer += char
            
    return answer
