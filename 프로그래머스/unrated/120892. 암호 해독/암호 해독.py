def solution(cipher, code):
    key = ""
    
    for i in range(1, len(cipher) +1):
        if i % code == 0:
            key += cipher[i-1]
            
    return key
