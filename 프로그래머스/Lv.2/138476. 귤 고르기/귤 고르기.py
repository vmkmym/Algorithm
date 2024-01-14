from collections import Counter

def solution(k, tangerine):
    dic = Counter(tangerine)
    dic = sorted(dic.values(), reverse=True)
    r = 0
    
    for i, v in enumerate(dic, 1):
        r += v
        if r >= k:
            return i
        
    return len(dic)