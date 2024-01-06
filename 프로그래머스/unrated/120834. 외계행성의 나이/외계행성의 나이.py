def solution(age):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    while age > 0:
        remainder = age % 10
        result = alphabet[remainder] + result
        age //= 10
    
    return result