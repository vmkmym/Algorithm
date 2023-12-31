def solution(cipher, code):
    key = ""
    
    for i in range(1, len(cipher)+1):
        if i % code == 0:
            key += cipher[i-1]
            
    return key

# 다른 풀이
def solution(cipher, code):
    key = ''.join(cipher[i-1] for i in range(1, len(cipher)+1) if i % code == 0)
    return key