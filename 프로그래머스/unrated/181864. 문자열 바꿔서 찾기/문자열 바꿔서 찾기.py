def solution(myString, pat):
    # 문자열 내의 특정 문자를 다른 문자로 교체
    swap_str = str.maketrans({'A': 'B', 'B': 'A'})
    
    # 문자열의 특정 문자를 교환
    patten = myString.translate(swap_str)
    
    return 1 if pat in patten else 0