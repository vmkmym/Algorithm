def solution(cipher, code):
    key = ""
    
    for i in range(1, len(cipher)+1):
        if i % code == 0:
            key += cipher[i-1]
            
    return key

# 다른 풀이 아직 추가 안함.. 